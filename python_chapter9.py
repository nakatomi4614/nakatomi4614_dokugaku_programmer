# chapter9
# ファイル　openとか

# pathを組み立てる

import os
from typing import List

s = os.path.join("Users", "bob", "st.txt")
print(s)

st = open("st.txt", "w")  # wは上書き書き込み
st.write("Hi from Python!")
st.close( )
# 上記を実行したら実行スクリプトと同じフォルダ内にst.txtを作り
# Hi　from　Python!と書き込む
# 日本語を使う場合か下記

st = open("st.txt", "w", encoding="utf-8")  # 日本語の場合はutf-8にencoding形式を指定
st.write("Hi from Python!　\nパイソンの方からきました")
st.close( )

# close()を使わないで閉じ忘れを防止する方法　with
with open("st.txt", "w", encoding="utf-8") as f:
    f.write("withを使ってclose()無し")
# 上書きしてるので結果は最後のスクリプトのみ

# 読み込む
with open("st.txt", "r", encoding="utf-8") as f:
    print(f.read( ))

my_list = []
with open("st.txt", "r", encoding="utf-8") as f:
    my_list.append(f.read( ))

print(my_list)

import csv

# 書き込み
with open("st.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

# 読み込み
with open("st.csv", "r", newline="") as f:
    r = csv.reader(f, delimiter=",")
    row: List[str]
    for row in r:
        print(row)
        print(",".join(row))

path_sample = r"C:\Users\neuph\Downloads\CTAmX1b1.txt"
with open(path_sample, "r", encoding="utf-8") as f:
    print(f.read( ))
"""
path_sample = r"st.txt"
s = input("好きな食べ物を教えて！：")
with open(path_sample,"a",encoding="utf-8") as f:
    f.write(s)
"""

path_sample = r"st1.csv"
sample_list =[["トップガン","risky business","minority report"],
              ["titanic","the revenant","inception"],
              ["trainig day","man on fire","Flight"]]
with open(path_sample,"w",encoding="utf-8") as f:
    w = csv.writer(f,delimiter=",")
    for row in sample_list:
        w.writerow(row)

