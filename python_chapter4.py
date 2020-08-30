#組み込み関数
#len 文字数を数える
print(len("なかとみはるき"))

#str 文字列を与える
print(str(100))

#int 整数値
print(int("3"))

#float 浮動小数点
print(float(200))

#intとfloatの使い方
a_1 = int("110")
a_2 = int(20.54)
a_3 = float("16.4")
a_4 = float(99)
print(a_1)
print(a_2)#切り捨てられる
print(a_3)
print(a_4)#.0がつく

#例外エラー処理を行い、エラーメッセージを表示している
try:
    print(int("Prince")) #数値でない文字列なのでintで例外
except ValueError as e:
    print(e)

"""
#input データを入力させる　得られるのはstr
age = input("Enter your age:")
int_age = int(age)
if int_age < 21:
    print("Your are Young!")
else:
    print("Wow, you are Old!")

#関数再利用


def even_odd(x):
    if x % 2 == 0:
        print("偶数")
    else:
        print("奇数")
even_odd(2)
even_odd(3)

def even_odd():
    n = input("type a number:")
    n = int(n)
    if n % 2 == 0:
        print("nは偶数")
    else:
        print("nは奇数")
even_odd()
even_odd()
even_odd()
#繰り返しで行う場合は関数に定義してその都度呼び出すようにする

for i in range(3):
    even_odd()
#上記はforを使って3回行った場合
"""

#必須引数（無いと例外エラー）とオプション引数（無くてもいい）
def f(x=2):
    return x ** x
print(f()) #x=2がデフォルト値となるように定義されている　オプション引数となる
print(f(4))

def add_it(x, y=10):
    return x + y
result = add_it(2) # 必須関数が含まれているため引数を与えなかったら実行されない
print(result)

#スコープ
#グローバルスコープ 関数外での変数定義を行ったらどこでも使える
x = 1
y = 2
z = 3

def f():
    print(x)
    print(y)
    print(z)

f()
"""
def f():
    x_1 = 1
    y_1 = 2
    z_1 = 3

print(x_1)
print(y_1)
print(z_1)
#上記のように書くと未定義のerrorが出る
"""

def f():
    x_1 = 4
    y_1 = 5
    z_1 = 6
    print(x_1)
    print(y_1)
    print(z_1)
f()

#定義されていない変数を使うと例外エラー
try:
    if teigishiteinaiyo >100:
        print("100よりも大きいよ")
except NameError as e:
    print(e)

#ローカルスコープ内からグローバル変数に書き込むにはglobal で明示する
#何に使うのかよくわからないｗ

x = 100
def f():
    global x
    x += 1 #x = x + 1と同義
    print(x)
f()

#例外処理　入力した値が想定外のものの時など

try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
#0を入力したらZeroDivisionErrorが出るので下記を追加する
    print(a/b)
except (ZeroDivisionError, ValueError): #二つ以上の時は（）でくくる
    print("ちゃんと0以外の数値を入力してね")

"""
#except節内でtry節で定義された変数を使用しない
try:
    10/0
    c = "I will never get defined."
except ZeroDivisionError:
    print(c)
#定義されていない変数になる可能性がある
""" #この"""で前後囲むとdocstringと呼ばれるコメントとなって実行されない

#必要な時だけ変数を使う

x =100
print(x)
#出力するためだけに整数を変数に格納しない

print(100)
#直接渡す












