from lxml import etree

xml_string = input()
root = etree.fromstring(xml_string)

# etree.dump(root)


for item in root:
    print(item.text)