#!C:\python3_6\python.exe
# coding: utf-8
import xml.etree.ElementTree as ET

# from bs4 import BeautifulSoup
#
fName ="xxxxxx.xml"

#
# with open(fName, encoding='utf-8') as doc:
#     soup = BeautifulSoup(doc, "xml")
#     print(soup.find_all())

with open(fName, encoding='utf-8') as doc:
    tree = ET.parse(doc)

output = []

for node in tree.iter():
    # output.append(str(node.tag) + "-" + str(node.attrib))
    # タグのアウトプット
    # output.append(str(node.tag))

    # print(node.tag, node.attrib)

    # 特定のタグの属性のみ抽出
    if(str(node.tag) == 'span'):
        output.append(str(node.attrib))



print(sorted(set(output)))
