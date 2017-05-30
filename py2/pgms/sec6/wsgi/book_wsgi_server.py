#!/usr/bin/env python
# Basic WSGI application - book_wsgi_server.py
#     Save the form data to an sqlite3 database
#     Parse the URL and Retrieve books
#     Build correct HTML pages
#
from wsgiref.simple_server import make_server
from io import BytesIO
from urllib import unquote_plus
import logging
import sqlite3

# set up logging
logging.basicConfig(level=logging.DEBUG)

ADD_ACTION = "Add"
SEARCH_ACTION = "Search"
__book_id = 100

header = "<html><header><title>Book Catalog</title></header><body>"
footer = "<p>provided by your Book Catalog company!</body></html>"

def html_page(content):
    page = ("%s\n%s\n%s" % (header, content, footer)).encode("utf-8")
    return page

def get_form_values(post_str):
    form_vals = { item.split("=")[0]: item.split("=")[1] 
        for item in post_str.split("&") }
    logging.debug('post string: %s' %post_str)
    return form_vals

def check_for_add(form_vals):
    if not form_vals['author'] \
        or not form_vals['title'] \
            or not form_vals['category']:
        return False
    return True

def check_for_search(form_vals):
    if not form_vals['author'] \
            and not form_vals['title'] \
                and not form_vals['category']:
        return False
    return True

def do_book_add(form_vals):
    cursor.execute("select max(id) from BookCatalog")
    __book_id = cursor.fetchone()[0] + 1
    logging.debug("Add: new Max id value = %d" %__book_id)
    form_vals['id'] = __book_id
    form_vals['copies'] = 1
    logging.debug("Add to BookCatalog: %s" %form_vals)
    cursor.execute("""insert into BookCatalog 
        (author, title, notes, copies, id) values 
        (:author, :title, :category, :copies, :id)""", form_vals)
    conn.commit()

def do_book_search(form_vals):
    cursor.execute("""select * from BookCatalog where author like ?
        and title like ? and notes like ? order by author""",
            ("%" + form_vals['author'] + "%",
                "%" + form_vals['title'] + "%",
                    "%" + form_vals['category'] + "%"))
    return book_table(cursor.fetchall())

def get_post_markup():
    result = """<p><form method="POST">Author: <input type="text" 
    name="author">  Title: <input type="text" 
    name="title">   Category: <input type="text" 
    name="category">
    <input type="submit" name="action" value=%s>
    <input type="submit" name="action" value=%s></form>""" \
        %(ADD_ACTION, SEARCH_ACTION)
    return result

def do_error_msg(err_msg):
    return "<h2>" + err_msg + "</h2>"

def book_table(books):
    table = "<table>\n"
    table += "<tr><th>Author</th><th>Title</th><th>Category</th><th>Copies</th></tr>"
    for book in books:
        row_str = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td></tr>\n"
        table += row_str.format(book[1], book[2], book[3], book[4])
    table += "</table>"
    return table

def book_catalog_app(environ, start_response):
    search_completed = False
    output = BytesIO()
    status = '200 OK'   # HTTP Status
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)
    print >>output, "<h1>Book Catalog</h1>"
    
    if environ['REQUEST_METHOD'] == 'POST':
        size = int(environ['CONTENT_LENGTH'])
        post_str = environ['wsgi.input'].read(size)
        # post_str = unquote_plus(post_str.decode())
        post_str = unquote_plus(post_str)
        form_vals = get_form_values(post_str)

        # process POST
        if form_vals['action'] == ADD_ACTION:
            logging.debug("Add Action for %s" %form_vals)
            if not check_for_add(form_vals):
                error_msg = "%s Error: All fields must have values." \
                    %(ADD_ACTION)
                logging.debug(error_msg)
                print >>output, do_error_msg(error_msg)
            else:
                do_book_add(form_vals)
        elif form_vals['action'] == SEARCH_ACTION:
            logging.debug("Search Action for %s" %form_vals)
            if not check_for_search(form_vals):
                error_msg = \
                    "%s Error: At least one search field must have a value." \
                        %(SEARCH_ACTION)
                logging.debug(error_msg)
                print >>output, do_error_msg(error_msg)
            else:
                print >>output, do_book_search(form_vals)
                search_completed = True
                logging.debug("Search: search database completed")
    if not search_completed:
        logging.debug("READ: regular database read")
        cursor.execute("""select * from BookCatalog 
            order by author """)
        print >>output, book_table(cursor.fetchall())

    print >>output, get_post_markup()
    return [html_page(output.getvalue())]

httpd = make_server('', 8000, book_catalog_app)

try:
    print("Serving on port 8000 ... ")
    conn = None

    # establish connection with database
    # and get cursor
    conn = sqlite3.connect("BookCatalog.db")
    cursor = conn.cursor()

    # start the server
    httpd.serve_forever()
except KeyboardInterrupt:
    print('\nExiting . . . ')
finally:
    if conn is not None:
        conn.close()
