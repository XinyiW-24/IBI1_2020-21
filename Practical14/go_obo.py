from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree=xml.dom.minidom.parse("go_obo.xml")
print(DOMTree.documentElement)
