#!/usr/bin/env python3
# books_multicall_client.py - show a sample client that uses XML-RPC protocol
# with multicall option
#           
import xmlrpc.client
# if the verbose flag is True, XML output is 
# returned by the Server.
server = xmlrpc.client.ServerProxy("http://localhost:9000", verbose=True)
#server = xmlrpc.client.ServerProxy("http://localhost:9000")

multicall = xmlrpc.client.MultiCall(server)
multicall.get_books()
multicall.get_authors()
multicall.get_titles()

for i, results in enumerate(multicall()):
    if i == 0:
       print("Books ")
       for book in results:
           sorted_keys = sorted(book.keys())
           # id, author, title, notes, copies
           print(book[sorted_keys[2]],
                book[sorted_keys[0]],
                book[sorted_keys[4]],
                book[sorted_keys[3]],
                book[sorted_keys[1]])
       print()
    elif i == 1:
        print("Authors ")
        for author in results:
            print(author)
        print()
    else:
        print("Titles ")
        for title in results:
            print(title)
        print()

##################################################
#
# $ books_multicall_cclient.py
# (verbose is True, so we get the server/client XML)
# send: b'POST /RPC2 HTTP/1.1\r\nHost: localhost:9000\r\nAccept-Encoding: gzip\r\nContent-Type: text/xml\r\nUser-Agent: Python-xmlrpc/3.5\r\nContent-Length: 784\r\n\r\n'
# send: b"<?xml version='1.0'?>\n<methodCall>\n<methodName>system.multicall</methodName>\n<params>\n<param>\n<value><array><data>\n<value><struct>\n<member>\n<name>params</name>\n<value><array><data>\n</data></array></value>\n</member>\n<member>\n<name>methodName</name>\n<value><string>get_books</string></value>\n</member>\n</struct></value>\n<value><struct>\n<member>\n<name>params</name>\n<value><array><data>\n</data></array></value>\n</member>\n<member>\n<name>methodName</name>\n<value><string>get_authors</string></value>\n</member>\n</struct></value>\n<value><struct>\n<member>\n<name>params</name>\n<value><array><data>\n</data></array></value>\n</member>\n<member>\n<name>methodName</name>\n<value><string>get_titles</string></value>\n</member>\n</struct></value>\n</data></array></value>\n</param>\n</params>\n</methodCall>\n"
# reply: 'HTTP/1.0 200 OK\r\n'
# header: Server header: Date header: Content-type header: Content-Encoding header: Content-length body: b"<?xml version='1.0'?>\n<methodResponse>\n<params>\n<param>\n<value><array><data>\n<value><array><data>\n<value><array><data>\n<value><struct>\n<member>\n<name>_Book__notes</name>\n<value><string>Autobiography</string></value>\n</member>\n<member>\n<name>_Book__title</name>\n<value><string>Tales From Margaritaville</string></value>\n</member>\n<member>\n<name>_Book__copies</name>\n<value><int>1</int></value>\n</member>\n<member>\n<name>_Book__author</name>\n<value><string>Buffett, Jimmy</string></value>\n</member>\n<member>\n<name>_Book__id</name>\n<value><int>104</int></value>\n</member>\n</struct></value>\n<value><struct>\n<member>\n<name>_Book__notes</name>\n<value><string>Science Fiction</string></value>\n</member>\n<member>\n<name>_Book__title</name>\n<value><string>Jurassic Park</string></value>\n</member>\n<member>\n<name>_Book__copies</name>\n<value><int>3</int></value>\n</member>\n<member>\n<name>_Book__author</name>\n<value><string>Crichton, Michael</string></value>\n</member>\n<member>\n<name>_Book__id</name>\n<value><int>102</int></value>\n</memb"
# body: b'er>\n</struct></value>\n<value><struct>\n<member>\n<name>_Book__notes</name>\n<value><string>Fiction</string></value>\n</member>\n<member>\n<name>_Book__title</name>\n<value><string>The Firm</string></value>\n</member>\n<member>\n<name>_Book__copies</name>\n<value><int>2</int></value>\n</member>\n<member>\n<name>_Book__author</name>\n<value><string>Grisham, John</string></value>\n</member>\n<member>\n<name>_Book__id</name>\n<value><int>103</int></value>\n</member>\n</struct></value>\n<value><struct>\n<member>\n<name>_Book__notes</name>\n<value><string>Classic</string></value>\n</member>\n<member>\n<name>_Book__title</name>\n<value><string>Les Miserables</string></value>\n</member>\n<member>\n<name>_Book__copies</name>\n<value><int>1</int></value>\n</member>\n<member>\n<name>_Book__author</name>\n<value><string>Hugo, Victor</string></value>\n</member>\n<member>\n<name>_Book__id</name>\n<value><int>101</int></value>\n</member>\n</struct></value>\n</data></array></value>\n</data></array></value>\n<value><array><data>\n<value><array><data>\n<value><string>Buffet'
# body: b't, Jimmy</string></value>\n<value><string>Crichton, Michael</string></value>\n<value><string>Grisham, John</string></value>\n<value><string>Hugo, Victor</string></value>\n</data></array></value>\n</data></array></value>\n<value><array><data>\n<value><array><data>\n<value><string>Jurassic Park</string></value>\n<value><string>Les Miserables</string></value>\n<value><string>Tales From Margaritaville</string></value>\n<value><string>The Firm</string></value>\n</data></array></value>\n</data></array></value>\n</data></array></value>\n</param>\n</params>\n</methodResponse>\n'
# Books 
# 104 Buffett, Jimmy Tales From Margaritaville Autobiography 1
# 102 Crichton, Michael Jurassic Park Science Fiction 3
# 103 Grisham, John The Firm Fiction 2
# 101 Hugo, Victor Les Miserables Classic 1
# 
# Authors 
# Buffett, Jimmy
# Crichton, Michael
# Grisham, John
# Hugo, Victor
# 
# Titles 
# Jurassic Park
# Les Miserables
# Tales From Margaritaville
# The Firm
# 

