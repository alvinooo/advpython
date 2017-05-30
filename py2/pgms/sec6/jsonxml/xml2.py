#!/usr/bin/env python
# xml2.py - using xml
import xml.dom.minidom

xml_string = '<books><book><author>Buffett, Jimmy</author><notes>Autobiography</notes><id>104</id><copies>1</copies><title>Tales From Margaritaville</title></book><book><author>Crichton, Michael</author><notes>Science Fiction</notes><id>102</id><copies>3</copies><title>Jurassic Park</title></book></books>'

doc = xml.dom.minidom.parseString(xml_string)

books = doc.getElementsByTagName("book")
print("Using MiniDom:")
for book in books:
    author = book.getElementsByTagName("author")[0].childNodes[0].data
    title = book.getElementsByTagName("title")[0].childNodes[0].data
    print("Author:\t%s\nTitle:\t%s\n" %(author, title))

print(doc.toprettyxml())

#################################################
#
#   $ xml2.py
#   Using MiniDom:
#   Author:	Buffett, Jimmy
#   Title:	Tales From Margaritaville
# 
#   Author:	Crichton, Michael
#   Title:	Jurassic Park
# 
#   <?xml version="1.0" ?>
#   <books>
# 	    <book>
#           <author>Buffett, Jimmy</author>
#           <notes>Autobiography</notes>
#           <id>104</id>
#           <copies>1</copies>
#           <title>Tales From Margaritaville</title>
#       </book>
#       <book>
#           <author>Crichton, Michael</author>
#           <notes>Science Fiction</notes>
#           <id>102</id>
#           <copies>3</copies>
#           <title>Jurassic Park</title>
#       </book>
#   </books>
