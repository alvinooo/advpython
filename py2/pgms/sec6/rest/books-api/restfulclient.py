#!venv/bin/python
# restfulclient.py - show how to write a restful client in python
# runs in virtual environment venv for Python 2
#
# Usage: restfulclient all | add | get book_id | 
#            delete book_id | update book_id
import requests
import sys

auth = ('asgteach', 'python')
url = "http://localhost:5000/bookcatalog/api/json/books"

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
    print(
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
            data = response.json()
            books = data['books']
            for book in books:
                print_book(book)
        else:
            handle_error(response)
    
    elif (sys.argv[1] == 'add'):    # add a new book
        """
        Since we are using JSON as our data format, we use the json 
        argument to post. Then, requests will do the following:
            Convert the data into a JSON representation string using 
            requests parameter json. This automatically sets the content 
            type for us to application/json.
        """
        data = {}
        data['title'] = get_input("enter book title: ")
        data['author'] = get_input("enter book author: ")
        data['notes'] = get_input("enter book category: ")
        data['copies'] = 1
        # when we specify the json argument, 
        # requests automatically sets the header to application/json for us
        response  = requests.post(url, json=data, auth=auth)
        if(response.ok):
            data = response.json()
            print_book(data['book'])
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
            data = response.json()
            print_book(data['book'])
            book = data['book']
            
            # get some possibly-revised data 
            book['title'] = get_revised("enter book title: ", book['title'])
            book['author'] = get_revised("enter book author: ", book['author'])
            book['notes'] = get_revised("enter book category: ", book['notes'])
            copy = get_revised("enter number of copies: ", str(book['copies'])) 
            while (not copy.isdigit()):
                print ("Oops! Copies must be integer")
                copy = get_revised("enter number of copies: ", 
                    str(book['copies'])) 
            book['copies'] = int(copy)
            response  = requests.put(url + "/" + book_id, json=book, auth=auth)
            if(response.ok):
                data = response.json()
                print_book(data['book'])
            else:
                handle_error(response)
        else:
            handle_error(response)
    elif (sys.argv[1] == 'get'):    # get a book
        book_id = sys.argv[2]
        response = requests.get(url+ "/" + book_id)
        if(response.ok):
            data = response.json()
            print_book(data['book'])
        else:
            handle_error(response)

    elif (sys.argv[1] == 'delete'):    # delete a book
        book_id = sys.argv[2]
        response  = requests.delete(url + "/" + book_id, auth=auth)
        if(response.ok and response.json()['result']):
            print("Delete sucessful")
        else:
            handle_error(response)
    else:
        raise SystemExit("Usage: %s bad argument" %sys.argv[1])
