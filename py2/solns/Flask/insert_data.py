#!venv/bin/python
# insert_data.py - insert data into database
from app import db, models
# create database tables from the models class
# (This destroys all the data)
db.drop_all()
db.create_all()

# add Role objects
admin_role = models.Role(name='Admin', default=False, can_modify=True)
user_role = models.Role(name='User', default=True, can_modify=False)

# add Users
user_gail = models.User(username='gail', password='cat', role=admin_role)
user_paul = models.User(username='paul', password='dog', role=admin_role)
user_joe = models.User(username='joe', password='bear', role=user_role)

db.session.add_all([admin_role, user_role,
    user_gail, user_paul, user_joe])
db.session.commit()

# now add some Books
b1 = models.Book(author='Buffett, Jimmy', title='Tales From Margaritaville',
        category='Autobiography', copies=1)
b2 = models.Book(author='Crichton, Michael', title='Jurassic Park',
        category='Fiction', copies=3)
b3 = models.Book(author='Grisham, John', title='The Firm',
        category='Fiction', copies=2)
b4 = models.Book(author='Hugo, Victor', title='Les Miserables',
        category='Classic', copies=1)
db.session.add_all([b1, b2, b3, b4])
db.session.commit()

users = models.User.query.all()
print('Users:')
for user in users:
    print(user.id, user.username, user.role)
print

print('Roles:')
roles = models.Role.query.all()
for role in roles:
    print('%r\t%r\t Default=%r\tCan Modify=%r' 
        %(role.id, role.name, role.default, role.can_modify))
print

print('Books:')
books = models.Book.query.order_by('author').all()
for book in books:
    print('%r\t%r\t%r\t%r\t%r' 
        %(book.id, book.author, book.title, book.category, book.copies))
print
