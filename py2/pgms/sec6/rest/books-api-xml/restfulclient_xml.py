#!venv/bin/python
# restfulclient_xml.py - show how to write a restful client in python
# pass data with xml instead of json
# configured to run in virtual environment venv for Python 2
# Usage: restfulclient all | add | get book_id | 
#           delete book_id | update book_id
import requests
import sys
import xmltodict
import xml.etree.ElementTree as etree

auth = ('asgteach', 'python')
url = "http://localhost:5000/bookcatalog/api/xml/books"

# get some non-zero length string input
def get_input(prompt):
    text_in = ""
    while len(text_in) == 0:
        text_in = raw_input(prompt)
    return text_in

# get some possibly revised input
def get_revised(prompt, old_data):
    text_in = raw_input(prompt + old_data + " <Hit Return to Keep the Same> ")
    if len(text_in) == 0:
        return old_data
    return text_in

# parse the uri and grab the book number
def get_id(uri):
    parts = uri.split('/');
    return parts[-1]

# handle a bad http response
def handle_error(response):
    raise SystemExit(
        "Error: code=%s, %s" %(response.status_code, response.reason))

# print the book nicely
def print_book(book):
    print (
    "BookID:\t\t%s\nAuthor:\t\t%s\nTitle:\t\t%s\nCategory:\t%s\nCopies:\t\t%s\n"
            %(get_id(book['uri']), book['author'], book['title'], 
            book['notes'], book['copies']))

args = len(sys.argv)
if (args == 1 or args > 3):
    usage = "Usage: %s" %sys.argv[0]
    raise SystemExit(usage + "[all] | [update book_id] |\n [get book_id]" +
        " | [add] | [delete book_id]")

if (args == 2):     # all or add
    if (sys.argv[1] == 'all'):      # read all
        response = requests.get(url)
        
        if(response.ok):
            books = xmltodict.parse(response.text)['books']
            for book in books['book']:
                print_book(book)
        else:
            handle_error(response)
    
    elif (sys.argv[1] == 'add'):    # add a new book
        """
        We must do the following
            Convert the data into a XML tree representation 
            from keyboard input.
            Set the requests' content type to 'application/xml' 
            (by adding an HTTP header).
        """
        headers = {'content-type': 'application/xml'}   # specify header

        # get input and build xml tree
        bookxml = etree.Element('book')
        child = etree.Element('title')
        child.text = get_input("enter book title: ")
        bookxml.append(child)
        child = etree.Element('author')
        child.text = get_input("enter book author: ")
        bookxml.append(child)
        child = etree.Element('notes')
        child.text = get_input("enter book category: ")
        bookxml.append(child)
        
        response  = requests.post(url, etree.tostring(bookxml), 
                    headers=headers, auth=auth) 
        if(response.ok):
            data = xmltodict.parse(response.text)['book']
            print_book(data)
        else:
            handle_error(response)
    else:
        raise SystemExit("Usage: %s bad argument" %sys.argv[1])
if (args == 3): # update, get, or delete
    if (sys.argv[1] == 'update'):      # update book
        book_id = sys.argv[2]
        
        # first get the book 
        response = requests.get(url+ "/" + book_id)
        if(response.ok):
            book = xmltodict.parse(response.text)['book']
            print_book(book)
            headers = {'content-type': 'application/xml'} 
            
            # get some possibly-revised data and build xml tree
            bookxml = etree.Element('book')
            child = etree.Element('title')
            child.text = get_revised("enter book title: ", book['title'])
            bookxml.append(child)
            child = etree.Element('author')
            child.text = get_revised("enter book author: ", book['author'])
            bookxml.append(child)
            child = etree.Element('notes')
            child.text = get_revised("enter book category: ", book['notes'])
            bookxml.append(child)
            child = etree.Element('copies')
            copy = get_revised("enter number of copies: ", str(book['copies'])) 
            while (not copy.isdigit()):
                print ("Oops! Copies must be integer")
                copy = get_revised("enter number of copies: ", 
                    str(book['copies'])) 
            child.text = copy
            bookxml.append(child)
            response  = requests.put(url + "/" + book_id, 
                    etree.tostring(bookxml), headers=headers, auth=auth)
            if(response.ok):
                data = xmltodict.parse(response.text)['book']
                print_book(data)
            else:
                handle_error(response)
        else:
            handle_error(response)
    elif (sys.argv[1] == 'get'):    # get a book
        book_id = sys.argv[2]
        response = requests.get(url+ "/" + book_id)
        if(response.ok):
            book = xmltodict.parse(response.text)['book']
            print_book(book)
        else:
            handle_error(response)

    elif (sys.argv[1] == 'delete'):    # delete a book
        book_id = sys.argv[2]
        response  = requests.delete(url + "/" + book_id, auth=auth)
        if(response.ok and xmltodict.parse(response.text)['result']):
            print("Delete sucessful")
        else:
            handle_error(response)
    else:
        raise SystemExit("Usage: bad argument for %s" %sys.argv[1])
