#!C:\python3_6\python.exe
# coding: utf-8

### flagとタイトルが同一のとき、wordと音声IDを繋げる処理
###

# import csv
# from pprint import pprint
from graphviz import Digraph

##header
# print("Content-Type: text/plain\n")
# print("test")

from graphviz import Digraph

# g = Digraph('G', filename='hello.png')
#
# g.edge('Hello', 'World')
#
# g.view()
# sys.exit()

G = Digraph(format='pdf')
G.attr('node', shape='circle')
# G.node(str(0), str(0))
G.edge('_01', '_01_01')
G.edge('_01', '_01_02')
G.edge('_01_01', '_01_01_01')
G.edge('_01_01', '_01_01_02')
G.edge('_01_02', '_01_02_01')
G.edge('_01_02', '_01_02_02')
G.edge('_01_01_01', '_01_01_01_01')
G.edge('_01_01_01', '_01_01_01_02')
G.edge('_01_01_02', '_01_01_02_01')
G.edge('_01_02_01', '_01_02_01_01')
G.edge('_01_02_01', '_01_02_01_02')
G.edge('_01_02_02', '_01_02_02_01')
G.edge('_01_02_02', '_01_02_02_02')
G.edge('_01_02_01_01', '_01_02_01_01_01')
G.edge('_01_02_01_01', '_01_02_01_01_02')
G.edge('_01_02_01_02', '_01_02_01_02_01')
G.edge('_01_02_01_02', '_01_02_01_02_02')
G.edge('_01_02_02_01', '_01_02_02_01_01')
G.edge('_01_02_02_01', '_01_02_02_01_02')
G.edge('_01_02_02_02', '_01_02_02_02_01')
G.edge('_01_02_01_02_01', '_01_02_01_02_01_01')
G.edge('_01_02_01_02_01', '_01_02_01_02_01_02')
G.edge('_01_02_01_02_02', '_01_02_01_02_02_01')
G.edge('_01_02_01_02_02', '_01_02_01_02_02_02')
G.edge('_01_02_02_01_01', '_01_02_02_01_01_01')
G.edge('_01_02_02_01_01', '_01_02_02_01_01_02')
G.edge('_01_02_02_01_02', '_01_02_02_01_02_01')
G.edge('_01_02_02_02_01', '_01_02_02_02_01_01')
G.edge('_01_02_02_02_01', '_01_02_02_02_01_02')
G.edge('_01_02_02_01_02_01', '_01_02_02_01_02_01_01')
G.edge('_01_02_02_01_02_01', '_01_02_02_01_02_01_02')

# print(G)

# binary_tree.pngで保存
G.render('test')

G = Digraph(format='pdf')
G.attr('node', shape='circle')
# G.node(str(0), str(0))
G.edge('_01', '_01_01')
G.edge('_01', '_01_02')
G.edge('_01_01', '_01_01_01')
G.edge('_01_01', '_01_01_02')
G.edge('_01_02', '_01_02_01')
G.edge('_01_02', '_01_02_02')
G.edge('_01_01_02', '_01_01_02_01')
G.edge('_01_01_02', '_01_01_02_02')
G.edge('_01_02_01', '_01_02_01_01')
G.edge('_01_02_01', '_01_02_01_02')
G.edge('_01_02_02', '_01_02_02_01')

# binary_tree.pngで保存
G.render('食事1')

# # formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
# G = Digraph(format='png')
# G.attr('node', shape='circle')
#
# N = 15    # ノード数
#
# # ノードの追加
# for i in range(N):
#     G.node(str(i), str(i))
#
# # 辺の追加
# for i in range(N):
#     if (i - 1) // 2 >= 0:
#         G.edge(str((i - 1) // 2), str(i))
#
# # print()するとdot形式で出力される
# print(G)
#
# # binary_tree.pngで保存
# G.render('binary_tree')
# print('処理終了')
# sys.exit()
