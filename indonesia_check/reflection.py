#!C:\python3_6\python.exe
# coding: utf-8

# import
import csv
from pprint import pprint
import sys

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
tmp = []

v = 1
i = 0

def fwrite(output):
    with open('list.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
        # writer.writerow(list)     # list（1次元配列）の場合
        writer.writerows(output) # 2次元配列も書き込める

maxLength = len(list)

while i < maxLength:
    #インデックスが超えたときは、強制的に書き出す
    try:
        j = i + 1
        test = list[j]
    except IndexError:
        # print(1111)
        fwrite(output)
        sys.exit()
    # j = i + 1

    # sys.exit()
    #primakeyとsecondary keyが異なるまでループ
    while list[i][1] == list[j][1] and list[i][2] == list[j][2]:
        # if list[i][2] == list[j][2]:
        if list[i][3] != list[j][3] and list[i][4] != list[j][4]:
            tmp = [list[i][0], 0]
            output.append(tmp)
            tmp = [list[j][0], 0]
            output.append(tmp)
        # else:
            # print(list[j][3])
            # tmp = [list[j][0], 1]

        # else:
        #     tmp = [list[j][0], 1]


        try:
            j+=1
            test = list[j]
            # print(j)
        except IndexError:
            print("error")
            i = maxLength
            break

    else:
        tmp = []
        # tmp = [list[i][0], 0]
        i = j

else:
    print("fin")
# print(output)
fwrite(output)

sys.exit()
