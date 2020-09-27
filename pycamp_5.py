#file操作とmodule
#作成 w a 読み込みr
f = open('pycamp.txt', 'w', encoding='utf-8')
print(f)
#書き込み
f.write('Hello')
f.write(' Python\n')  # 改行を書き込むには \n を指定する
f.write('こんにちはPython\n')  # 日本語も書き込み可能
#\nは改行

#close 使ったら閉じる
f.close()

#読み込み open r .read()　rは省略できる
f = open('pycamp.txt', 'r', encoding='utf-8')
print(f)
txt = f.read() #.read()はstrを返す
print(txt)
f.close()

#withでのopenするとcloseしなくていい
with open('pycamp.txt', encoding='utf-8') as f:
    txt = f.read()
print(txt)
#a 追記
f = open('pycamp.txt', 'a', encoding='utf-8')
f.write('こんにちは世界\n')

#importでモジュールとして再利用
import calc
print(calc.add(1,2))
#直接インポート　from import
#calcの中からaddだけをインポートしている感じ
from calc import add
print(add(1, 2))
import calc as c #別名はas なんとか
print(c.add(1, 2))
#複数インポート
from calc import add, sub
print(add(1, 2))
print(sub(2, 1))

#標準ライブラリ
#日付
import datetime
d = datetime.date(2016, 12, 23)
print(d.year, d.month, d.day)
today = datetime.date.today() #今日の日付は.today()
print(today)  # 実行する日によって結果が異なる
birthday = datetime.date(1976, 3, 5)  # Python 3.0のリリース日
today = datetime.date.today()
delta = today - birthday  # 日付や時刻の差を表すdatetime.timedeltaオブジェクト
print("生まれてから"+str(delta.days)+"日")  # 実行する日によって結果が異なる

#re 正規表現
import re
m = re.search('(P(yth|l)|Z)o[pn]e?', 'Python')
print(m)
m = re.search('py(thon)', 'python')
print(m.group())
print(m.group(0))
print(m.group(1))
#正規表現にマッチしない場合は、Noneを返します。
print(re.search('py', 'ruby'))
