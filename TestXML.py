
xmltext = "<myroot><OneThing><Under /></OneThing></myroot>"

import xml.etree.ElementTree as ET
tree = ET.fromstring(xmltext)

for elem in tree.iter():
    print(elem)
