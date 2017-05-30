#!venv/bin/python
# app.py - REST json server running in virtual environment venv
# runs in Python 2 
from flask import Flask, jsonify
from flask import abort, make_response, request
from flask import url_for
import sqlite3 
import logging

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

app = Flask(__name__)

# set up logging
logging.basicConfig(level=logging.DEBUG)

api_url = '/bookcatalog/api/json/books'

# hard-code the authorization password
@auth.get_password
def get_password(username):
    if username == 'asgteach':
        return 'python'
    return None

# return an unauthorized access error
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

"""
    Flask generates the error response with an HTML message 
    instead of JSON by default.  However, client applications 
    will expect a response in JSON.
    So we configure our error handler to generate JSON.
"""

# error handler for 400 & 404 & 500
@app.errorhandler(404)
@app.errorhandler(400)
@app.errorhandler(500)
def do_error_response(error):
    logging.debug("Error = %s" %error)
    return make_response(jsonify({'error': error.name}), error.code)

"""
    Return the full URI that controls the book, 
    so that clients get the URIs ready to be used.
    This code replaces the field 'id' with the
    field 'uri' and includes the full URI.
"""
def make_book_uri(book):
    new_book = {}
    for field in book:
        if field == 'id':
            new_book['uri'] = url_for('get_book', 
                book_id=book['id'], _external=True)
        else:
            new_book[field] = book[field]
    return new_book

# get list of books
@app.route(api_url, methods=['GET'])
def get_books():
    logging.debug("GET all books")
    try:
        conn = sqlite3.connect("BookCatalog.db")
        conn.row_factory = sqlite3.Row      # select a dictionary cursor
        cursor = conn.cursor()
        cursor.execute("""select * from BookCatalog 
            order by author """)
        books = cursor.fetchall()
        book_list = [dict(book) for book in books]
        return jsonify({'books': [make_book_uri(book) for book in book_list]})
    except sqlite3.Error as ex:
        logging.error("Database Error : %s" %ex)
        abort(500)
    finally:
        logging.debug("closing database");
        conn.close()

# get book corresponding to book_id
@app.route(api_url + '/<int:book_id>', methods=['GET'])
def get_book(book_id):
    logging.debug("GET book from id: %s" %book_id)
    try:
        conn = sqlite3.connect("BookCatalog.db")
        conn.row_factory = sqlite3.Row      # select a dictionary cursor
        cursor = conn.cursor()
        cursor.execute("select * from BookCatalog where id = ?", (book_id,))
        books = cursor.fetchall()
        if len(books) == 0:
            abort(404)      # Not Found
        return jsonify({'book': make_book_uri(dict(books[0]))})
    except sqlite3.Error as ex:
        logging.error("Database Error : %s" %ex)
        abort(500)
    finally:
        logging.debug("closing database");
        conn.close()

# create a new book, data is in request object
@app.route(api_url, methods=['POST'])
@auth.login_required
def add_book():
    logging.debug("create new book")
    if not request.json or \
                not 'title' in request.json or \
                not 'notes' in request.json or \
                not 'author' in request.json:
        abort(400)      # Bad Request
    try:
        conn = sqlite3.connect("BookCatalog.db")
        conn.row_factory = sqlite3.Row      # select a dictionary cursor
        cursor = conn.cursor()
        cursor.execute("select max(id) from BookCatalog")
        __book_id = cursor.fetchone()[0] + 1
        logging.debug("Add: new Max id value = %d" %__book_id)
        book = {
            'id':       __book_id,
            'author':   request.json['author'],
            'title':    request.json['title'],
            'notes':    request.json['notes'],
            'copies':   1
        }
        logging.debug("Add to BookCatalog: %s" %book)
        cursor.execute("""insert into BookCatalog 
            (id, author, title, notes, copies) values 
            (:id, :author, :title, :notes, :copies)""", book)
        conn.commit()
        return jsonify({'book': make_book_uri(book)}), 201
    except sqlite3.Error as ex:
        logging.error("Database Error : %s" %ex)
        conn.rollback()
        abort(500)
    finally:
        logging.debug("closing database");
        conn.close()

# delete the book corresponding to book_id
@app.route(api_url + '/<int:book_id>', methods=['DELETE'])
@auth.login_required
def delete_book(book_id):
    logging.debug("DELETE book from id: %s" %book_id)
    try:
        conn = sqlite3.connect("BookCatalog.db")
        cursor = conn.cursor()
        cursor.execute("delete from BookCatalog where id = ?", (book_id,))
        if cursor.rowcount ==  0:
            abort(404)      # Not Found
        conn.commit()
        return jsonify({'result': True})
    except sqlite3.Error as ex:
        logging.error("Database Error : %s" %ex)
        conn.rollback()
        abort(500)
    finally:
        logging.debug("closing database");
        conn.close()

# update the book corresponding to book_id
@app.route(api_url + '/<int:book_id>', methods=['PUT'])
@auth.login_required
def update_book(book_id):
    logging.debug("PUT: update book from id: %s" %book_id)
    # check input
    if not request.json:
        abort(400)
    if 'author' in request.json and type(request.json['author']) is not unicode:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'notes' in request.json and type(request.json['notes']) is not unicode:
        abort(400)
    if 'copies' in request.json and type(request.json['copies']) is not int:
        abort(400)
    try:
        conn = sqlite3.connect("BookCatalog.db")
        conn.row_factory = sqlite3.Row      # select a dictionary cursor
        cursor = conn.cursor()
        cursor.execute("select * from BookCatalog where id = ?", (book_id,))
        books = cursor.fetchall()
        if len(books) == 0:
            abort(404)      # Not Found
        book = dict(books[0])
        book['author'] = request.json.get('author', book['author'])
        book['title'] = request.json.get('title', book['title'])
        book['notes'] = request.json.get('notes', book['notes'])
        book['copies'] = request.json.get('copies', book['copies'])
        cursor.execute("""UPDATE BookCatalog SET author = ? , 
            title = ?, notes = ?, copies = ? WHERE id = ? """,
                (book['author'], book['title'], book['notes'], 
                    book['copies'], book_id))
        conn.commit()
        return jsonify({'book': make_book_uri(book)})
    except sqlite3.Error as ex:
        logging.error("Database Error : %s" %ex)
        conn.rollback()
        abort(500)
    finally:
        logging.debug("closing database");
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
