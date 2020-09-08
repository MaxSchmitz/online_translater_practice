from lxml import etree


def find_password(xml_string):
    root = etree.fromstring(xml_string)
    # etree.dump(root)

    for item in root.iter():
        if item.get('password'):
            return item.get('password')


# sample_1 = '<profile><account login="login" password="secret"/></profile>'
# sample_2 = '''<result>
#   <webpage link="hyperskill.com"></webpage>
#   <users>
#     <!-- Random comment -->
#     <user id="239" password="qwerty"><info email="a@a.a"/></user>
#   </users>
# </result>'''
#
# print(find_password(sample_2))