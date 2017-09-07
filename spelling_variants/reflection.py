#!C:\python3_6\python.exe
# coding: utf-8

import csv
# import
from pprint import pprint

##header
print("Content-Type: text/plain\n")
# print("test")

test = ["aaaa", "bbbbb"]
# pprint(test)

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

# 修正前のデータ
list = readCsv('some.csv', 'utf-8-sig')
# print(list[0][1])
# sys.exit()

list2 = [['abad', 'xxxxx'], ['abu', 'てすと']]
# print(list[1][0])

output = []
tmp = ''

for i, rows in enumerate(list):
    #見出し語とカタカナを半角スペースで区切る
    tmpMidashi = list[i][1].split()
    tmpKatakana =list[i][2].split()
    # print(tmpKatakana)
    # sys.exit()
    # print(rows[i])
    for j, val in enumerate(tmpMidashi):#見出し語
        for k, list2Val in enumerate(list2):#置き換えリスト
            #区切った単語が置き換えのリストと同一で、かつ、カタカナが異なるときにカタカナを置き換える
            if val == list2[k][0] and tmpKatakana[j] != list2[k][1]:
                # print(list2[k][1])
                # print(tmpKatakana[j])
                # print(j)
                tmpKatakana[j] = list2[k][1]
                break
        ###end for
        # print(tmpKatakana)

    tmp = " " . join(tmpKatakana)
    # print(tmp)
    output.append(tmp)

###end for
print(output)
sys.exit()
