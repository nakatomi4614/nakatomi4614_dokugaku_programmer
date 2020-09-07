# chapter8 モジュール

# 組み込みモジュール

import math

print(math.pow(2, 3))

import random

print(random.randint(0, 100))
# 0から100の乱数発生

import statistics

nums = [1, 5, 33, 12, 46, 33, 2]
stat_list = (statistics.mean(nums),
             statistics.median(nums),
             statistics.mode(nums)
             )
#mean 平均 median 中央値　mode　最頻値

for i in stat_list:
    print(i)

import keyword
print(keyword.iskeyword("for")) #Pythonで使われる単語
print(keyword.iskeyword("football"))

#ほかのモジュール　モジュールを作る
def print_hello():
    print("Hello")

import module1
#importしたら実行されるので追加を行う。
#module1.pyに
#if __name__ == "__main__":
#を追加したら、実行されない defだけならいらないか？defが実行されない

#チャレンジ２
import module2
print(module2.cubed(8))
print("確認用:"+str(8**3))

print(statistics.stdev(nums))
