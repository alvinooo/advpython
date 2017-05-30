# views.py - views
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .forms import LoginForm, RegisterForm, CreateBookForm, DeleteBookForm
from .models import User, Role, Book

"""
The views are the handlers that respond to requests 
from web browsers or other clients. 
In Flask, handlers are written as Python functions. 
Each view function is mapped to one or more request URLs.
"""
@app.route('/')
@app.route('/index')
@login_required
def index():
# read database to get list of books
    user = g.user
    print("user is authenticated: %r" % user.is_authenticated)
    books = Book.query.order_by('author').all()
    return render_template("index.html",
    title='Home',
    user=user,
    books=books)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.data['register_me']:
        print("Register me clicked!")
        return redirect(url_for('register'))
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            # register this as a valid login
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password.')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            default_role = Role.query.filter_by(default=True).first()
            user = User(username=form.username.data, 
                password=form.password.data, role=default_role)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('index'))
        flash('Username is already taken. Choose a different username.')
    return render_template('register.html', 
            title='Register Me', form=form)

"""
    This function will be used by Flask-Login to load a user from the database.
    This function is registered with Flask-Login through the 
    lm.user_loader decorator.  Note that user ids in Flask-Login are 
    always unicode strings, so a conversion to an integer is necessary 
    before we can send the id to Flask-SQLAlchemy.
"""

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.after_request
def apply_caching(response):
    response.headers.add('Cache-Control', 
        'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')  
    return response

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    if g.user is not None and not g.user.role.can_modify:
        flash("Sorry. You don't have administrative privileges.")
        return redirect(url_for('index'))
    form = CreateBookForm()
    if form.validate_on_submit():
        book = Book(author=form.author.data, title=form.title.data, 
            category=form.category.data, copies=1)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_book.html', title='Add Book', form=form)

def do_delete(del_books):
    if (len(del_books) == 0):
        flash("No books selected for deletion.")
    else:
        for book in del_books:
            db.session.delete(book)
            flash("Deleted book %s, '%s'" %(book.author, book.title))
        db.session.commit()
        
@app.route('/delete_book', methods=['GET', 'POST'])
@login_required
def delete_books():
    if g.user is not None and not g.user.role.can_modify:
        flash("Sorry. You don't have administrative privileges.")
        return redirect(url_for('index'))
    books = Book.query.order_by('author').all()
    forms = []
    
    # create a checkbox boolean form for each book
    for book in books:
        form = DeleteBookForm(prefix=str(book.id))
        forms.append(form)
    if request.method=='POST':
        del_books = []
        for book,form in zip(books,forms):
            if form.delete_bool.data:
               del_books.append(book) 
        do_delete(del_books)
        return redirect(url_for('index'))
    # Jinja templates don't support zip, so zip our data first!
    return render_template("delete_books.html", 
        title='Delete Book', form=forms[0], data=zip(books,forms))
