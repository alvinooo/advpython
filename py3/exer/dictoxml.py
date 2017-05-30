#!/usr/bin/env python3
# dicttoxml.py - dictionary to XML
from collections import OrderedDict
import xml.etree.ElementTree as etree
import xml.dom.minidom as dom

def toXML(tag, dictionary):
    # your code here...

company = OrderedDict()
company["name"] = "IBM"
company["shares"] = 100
company["price"] = 192.05

xml = toXML("stock", company)
xmlstring = etree.tostring(xml)
print(xmlstring)
# your code here...

#################################################
#
#    $ dictoxml.py
#    <stock><name>IBM</name><shares>100</shares><price>192.05</price></stock>
#    <?xml version="1.0" ?>
#    <stock>
#            <name>IBM</name>
#            <shares>100</shares>
#            <price>192.05</price>
#    </stock>
#
