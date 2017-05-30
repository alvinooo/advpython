#!/usr/bin/env python
# xml1.py - using xml
# import xml.etree.cElementTree as etree
import xml.etree.ElementTree as etree

xml_string = '<books><book><author>Buffett, Jimmy</author><notes>Autobiography</notes><id>104</id><copies>1</copies><title>Tales From Margaritaville</title></book><book><author>Crichton, Michael</author><notes>Science Fiction</notes><id>102</id><copies>3</copies><title>Jurassic Park</title></book></books>'

root = etree.fromstring(xml_string)
print("Using ElementTree:")
for book in root.findall('book'):
    print("Author:\t%s\nTitle:\t%s\n" 
        %(book.find('author').text, book.find('title').text))

#################################################
#
#   $ xml1.py
#   Using ElementTree:
#   Author:	Buffett, Jimmy
#   Title:	Tales From Margaritaville
# 
#   Author:	Crichton, Michael
#   Title:	Jurassic Park
# 
