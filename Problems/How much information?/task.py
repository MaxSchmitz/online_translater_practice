from lxml import etree

xml_string = input()
root = etree.fromstring(xml_string)

# etree.dump(root)

print(len(root), len(root.keys()))
