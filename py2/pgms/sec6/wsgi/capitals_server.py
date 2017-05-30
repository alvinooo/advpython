#!venv/bin/python
# Basic WSGI application - capitals_server.py
#   Build an HTML table with the world's countries and capitals
#   Dynamically page through the data
#
from wsgiref.simple_server import make_server
from io import BytesIO
from urllib import unquote_plus
import logging
import requests

# set up logging
logging.basicConfig(level=logging.DEBUG)

# global variables
country_list = []
INDEX_STEP = 20

header = """<html><head>
    <style>
        body    { background-color: #eeffff; 
                  font-family: Arial, sans-serif; }
        table   { border: 2px solid black; }
        th      { border-bottom: 2px solid black; }
        td, th  { text-align: right;padding: 1px 5px 1px 5px; }
    </style>
    <title>Capitals</title></head><body>"""

footer = "<p>provided by your friendly capitals source!</body></html>"

def html_page(content):
    page = ("%s\n%s\n%s" % (header.encode("utf-8"), content, footer.encode("utf-8")))
    return page

def get_form_values(post_str):
    logging.debug('post_str: %s', post_str)
    form_vals = {item.split("=")[0]: item.split("=")[1] for item
                    in post_str.split("&")}
    return form_vals

def do_error_msg(err_msg):
    msg = "<h2>"
    msg += "{0}".format(err_msg)
    msg += "</h2>"
    return msg

def country_table(countries):
    table = "<table>\n"
    table += "<tr><th>Country</th><th>Capital</th><th>Region</th><th>Sub Region</th>"\
    "<th>Population</th><th>LatLng</th></tr>"
    for country in countries:
        row_str = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td>"\
        "<td>{4:,}</td><td>{5}</td></tr>\n"
        table += row_str.format(
            country['name'].encode("utf-8"), 
            country['capital'].encode("utf-8"), 
            country['region'].encode("utf-8"), 
            country['subregion'].encode("utf-8"),
            country['population'],
            country['latlng'])
    table += "</table>"
    return table

def capitals_app(environ, start_response):
    output = BytesIO()
    status = '200 OK'   # HTTP Status
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)
    print >>output, "<h1>World Capitals</h1>"
    
    country_index = 0;

    # get the country data
    # use a REST call
    global country_list
    if not country_list:
        logging.debug("get data from restcountries.eu/rest/v1/all");
        url = 'https://restcountries.eu/rest/v1/all/'
        try:
            response = requests.get(url, timeout=5)
            if (response.ok):
                # country_list is a list of dictionaries
                country_list = response.json()
            else:
                response.raise_for_status()
        except Exception as ex:
            # build response saying there is a problem with
            # the countries web site
            logging.debug('Add Error: %s', ex)
            print >>output, do_error_msg(ex)
            return [html_page(output.getvalue())]
    else:
        logging.debug("already got the data")
    
    last_page = len(country_list) - INDEX_STEP
    if environ['REQUEST_METHOD'] == 'POST':
        size = int(environ['CONTENT_LENGTH'])
        post_str = environ['wsgi.input'].read(size)
        post_str = unquote_plus(post_str)
        form_vals = get_form_values(post_str)
        logging.debug("form_vals = %s", form_vals)
        country_index = int(form_vals['action'])
        if country_index < 0:
            country_index = 0
        elif country_index > last_page:
            country_index = last_page
    
    logging.debug("index = %d", country_index)

    print >>output, country_table(
            country_list[country_index:country_index + INDEX_STEP]), "<p>"
    logging.debug("first index = %d, prev index = %d,"\
            "next index = %d, last index = %d",
            0, country_index-INDEX_STEP, country_index+INDEX_STEP, last_page)
    
    print >>output, """<form method="POST">
    <button type="submit" name="action" value=%s>First Page</button>
    <button type="submit" name="action" value=%s>Previous Page</button>
    <button type="submit" name="action" value=%s>Next Page</button>
    <button type="submit" name="action" value=%s>Last Page</button>
    </form>""" % ("0", str(country_index - INDEX_STEP), 
            str(country_index + INDEX_STEP), str(last_page))
    return [html_page(output.getvalue())]

httpd = make_server('', 8000, capitals_app)

try:
    print("Serving on port 8000 ... ")

    # start the server
    httpd.serve_forever()
except KeyboardInterrupt:
    print('\nExiting . . . ')
