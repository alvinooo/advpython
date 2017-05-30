#!venv/bin/python
# xml3.py - using xml
import xmltodict

def postprocessor(path, key, value):
    try:
        return key, int(value)
    except (ValueError, TypeError):
        return key, value

xml_string = '<books><book><author>Buffett, Jimmy</author><notes>Autobiography</notes><id>104</id><copies>1</copies><title>Tales From Margaritaville</title></book><book><author>Crichton, Michael</author><notes>Science Fiction</notes><id>102</id><copies>3</copies><title>Jurassic Park</title></book></books>'

books = xmltodict.parse(xml_string, postprocessor=postprocessor)['books']
print("Using xmltodict:")
for book in books['book']:
    print("Author:\t%s\nTitle:\t%s" %(book['author'], book['title']))
    print(type(book['copies']))

#################################################
#
#   $ xml3.py
#   Using xmltodict:
#   Author:	Buffett, Jimmy
#   Title:	Tales From Margaritaville
#   <type 'int'>
#   Author:	Crichton, Michael
#   Title:	Jurassic Park
#   <type 'int'>
