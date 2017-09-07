#!C:\python3_6\python.exe
# coding: utf-8

# import
import csv
import numpy as np
# import pandas as pd
import sys
from pprint import pprint

##header
# print("Content-Type: text/plain\n")
# print("test")

# csv読み込み関数
def readCsv(file, enc):
    tmp = []
    try:
        # bom付きutf-8は、'utf-8-sig'
        with open(file, 'r', encoding=enc) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter= ',', quotechar='"')
            for row in csv_reader:
                #配列にpush
                tmp.append(row)

    # 起こりそうな例外をキャッチ
    except FileNotFoundError as e:
        print(e)
    except csv.Error as e:
        print(e)
    return tmp
##readCsv終了

##書き込み関数
def fwrite(output, fileName):
    with open(fileName, 'w', encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
        # writer.writerow(output)     # list（1次元配列）の場合
        writer.writerows(output) # 2次元配列も書き込める
##fwrite終了

# 修正前のデータ
list = readCsv('list.csv', 'utf-8-sig')

# lie = pd.read_csv('list.csv')

output=[]

for val  in list:
    output.append(set(val))
    # print(set(val))

# print(output)
fwrite(output, 'output.csv')
sys.exit()
