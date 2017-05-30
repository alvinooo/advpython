#!venv/bin/python
# app.py - REST server processing requests & responses with XML
# runs in virtual environment venv for Python 2
from flask import Flask
from flask import abort, make_response, request
from flask import url_for
import sqlite3 
import logging
import xml.etree.ElementTree as etree
import xmltodict

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

app = Flask(__name__)

# set up logging
logging.basicConfig(level=logging.DEBUG)
api_url = '/bookcatalog/api/xml/books'

def dict_to_xml(tag, d):
    elem = etree.Element(tag)
    for key, val in d.items():
        child = etree.Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

# convert integer strings to int values during xml parsing
def postprocessor(path, key, value):
    try:
        return key, int(value)
    except (ValueError, TypeError):
        return key, value

# hard-code the authorization password
@auth.get_password
def get_password(username):
    if username == 'asgteach':
        return 'python'
    return None

# return an unauthorized access error
@auth.error_handler
def unauthorized():
    logging.debug("Error = Unauthorized access (401)")
    err = '<error>Unauthorized access</error>' 
    response = make_response(err, '401')
    response.headers['Content-Type'] = 'text/xml; charset=utf-8' 
    return response

"""
    Flask generates the error response with an HTML message 
    instead of XML by default.  However, client applications 
    will expect a response in XML.
    So we configure our error handler to generate XML.
"""

# error handler for 400 & 404 & 500
@app.errorhandler(404)
@app.errorhandler(400)
@app.errorhandler(500)
def do_error_response(error):
    logging.debug("Error = %s" %error)
    err = '<error>' + error.name + '</error>' 
    response = make_response(err, error.code) 
    response.headers['Content-Type'] = 'text/xml; charset=utf-8' 
    return response

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
            new_book['uri'] = url_for('get_book', book_id=book['id'], 
                _external=True)
        else:
            new_book[field] = book[field]
    return new_book

# get list of books
@app.route(api_url, methods=['GET'])
def get_books():
    logging.debug("GET all books")
    try:
        conn = sqlite3.connect("BookCatalog.db")
        conn.row_factory = sqlite3.Row      # select dictionary cursor
        cursor = conn.cursor()
        cursor.execute("""select * from BookCatalog 
            order by author """)
        books = cursor.fetchall()
        book_list = [make_book_uri(dict(book)) for book in books]
        bookxml = etree.Element("books")
        [bookxml.append(dict_to_xml("book", book)) for book in book_list]
        logging.debug("GET: %s" %etree.tostring(bookxml))
        
        response = make_response(etree.tostring(bookxml))
        response.headers['Content-Type'] = 'text/xml; charset=utf-8' 
        return response
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
        bookxml = dict_to_xml('book', make_book_uri(dict(books[0])))
        logging.debug("GET: %s" %etree.tostring(bookxml))
        response = make_response(etree.tostring(bookxml))
        response.headers['Content-Type'] = 'text/xml; charset=utf-8' 
        return response
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
    # check to make sure we have xml
    if request.content_type != "application/xml":
        abort(400)
    xml_str = request.data
    logging.debug("data = %s" %xml_str)
    book = xmltodict.parse(xml_str)['book']
    logging.debug("create new book for %s" %book)
    if not 'title' in book or \
                not 'notes' in book or \
                not 'author' in book:
        abort(400)      # Bad Request
    try:
        conn = sqlite3.connect("BookCatalog.db")
        conn.row_factory = sqlite3.Row      # select dictionary cursor
        cursor = conn.cursor()
        cursor.execute("select max(id) from BookCatalog")
        __book_id = cursor.fetchone()[0] + 1
        logging.debug("Add: new Max id value = %d" %__book_id)
        book['id'] = __book_id
        book['copies'] = 1
        logging.debug("Add to BookCatalog: %s" %book)
        cursor.execute("""insert into BookCatalog 
            (id, author, title, notes, copies) values 
            (:id, :author, :title, :notes, :copies)""", book)
        conn.commit()
        bookxml = dict_to_xml('book', make_book_uri(book))
        logging.debug("GET: %s" %etree.tostring(bookxml))
        response = make_response(etree.tostring(bookxml), 201)
        response.headers['Content-Type'] = 'text/xml; charset=utf-8' 
        return response
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
        response = make_response("<result>True</result>")
        response.headers['Content-Type'] = 'text/xml; charset=utf-8' 
        return response
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
    if request.content_type != "application/xml":
        abort(400)
    xml_str = request.data
    logging.debug("data = %s" %xml_str)
    target_book = xmltodict.parse(xml_str, postprocessor=postprocessor)['book']
    logging.debug("update book for %s" %target_book)
    if 'title' in target_book and type(target_book['title']) is not unicode:
        abort(400)      # Bad Request
    if 'author' in target_book and type(target_book['author']) is not unicode:
        abort(400)      # Bad Request
    if 'notes' in target_book and type(target_book['notes']) is not unicode:
        abort(400)      # Bad Request
    if 'copies' in target_book and type(target_book['copies']) is not int:
        abort(400)
    try:
        conn = sqlite3.connect("BookCatalog.db")
        conn.row_factory = sqlite3.Row      # select dictionary cursor
        cursor = conn.cursor()
        cursor.execute("select * from BookCatalog where id = ?", (book_id,))
        books = cursor.fetchall()
        if len(books) == 0:
            abort(404)      # Not Found
        book = dict(books[0])
        book['author'] = target_book.get('author', book['author'])
        book['title'] = target_book.get('title', book['title'])
        book['notes'] = target_book.get('notes', book['notes'])
        book['copies'] = target_book.get('copies', book['copies'])
        cursor.execute("""UPDATE BookCatalog SET author = ? , 
            title = ?, notes = ?, copies = ? WHERE id = ? """,
                (book['author'], book['title'], book['notes'], 
                    book['copies'], book_id))
        conn.commit()
        bookxml = dict_to_xml('book', make_book_uri(book))
        logging.debug("PUT: %s" %etree.tostring(bookxml))
        response = make_response(etree.tostring(bookxml))
        response.headers['Content-Type'] = 'text/xml; charset=utf-8' 
        return response
    except sqlite3.Error as ex:
        logging.error("Database Error : %s" %ex)
        conn.rollback()
        abort(500)
    finally:
        logging.debug("closing database");
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)

