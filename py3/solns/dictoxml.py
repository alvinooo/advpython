#!/usr/bin/env python3
# dictoxml.py - dictionary to XML
from collections import OrderedDict
import xml.etree.ElementTree as etree
import xml.dom.minidom as dom

def toXML(tag, dictionary):
    element = etree.Element(tag)
    for (key, value) in list(dictionary.items()):
        child = etree.Element(key)
        child.text = str(value)
        element.append(child)
    return element

company = OrderedDict()
company["name"] = "IBM"
company["shares"] = 100
company["price"] = 192.05

xml = toXML("stock", company)
xmlstring = etree.tostring(xml)
print(xmlstring)
doc = dom.parseString(xmlstring)
print(doc.toprettyxml())

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
