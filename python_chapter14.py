# もっとobject指向プログラミング

"""
まとめ
すべてのオブジェクトはクラスのインスタンス
クラスから作られるオブジェクトをインスタンスと呼ぶ
オブジェクトと言ったときはインスタンスのことを指す
Pyrhonではクラスはtypeクラスから作られるオブジェクト
クラスをつくるクラスをメタクラスという
"""

"""
class Square:
    pass
print(Square)
#インスタンス変数　は　インスタンス
#self.[変数名]　=　[値]

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} かける {}".format(self.width, self.len))

my_rectangle = Rectangle(10,24)
my_rectangle.print_size()
#widthとlenがインスタンス変数
"""


class Rectangle:
    recs = [] #これがクラス変数　__init__メソッドの外から定義する

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("{} かける {}".format(self.width, self.len))


r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)
#クラス変数の更新はできるだけ避けるべき。クラス変数に定数を持たせるのは一般的に行われる

#特殊メソッド
class Lion:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return self.name

lion = Lion("らいおん丸")
print(lion)
#print関数は__repr__呼び出す。__repr__が返してきた値を出力する。

class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)
x = AlwaysPositive(-20)
y = AlwaysPositive(10)
print(x+y)
#__add__に絶対値の関数abs()を組み込んでいる

# is　同一のオブジェクトならTrueを返す　違うならFalse
class Person:
    def __init(self):
        self.name = "Bob"

bob = Person()
same_bob = bob
print(bob is same_bob)
#こちらはPersonから作られた一つのオブジェクトを指している
another_bob = Person()
print(bob is another_bob)
#こちらは二つの変数が別のオブジェクトを指している

#is はNoneかどうか調べるのにも使える
x = 10
if x is None:
    print("xはNone:(")
else:
    print("xはNoneじゃない")

x= None
if x is None:
    print("xはNone:(")
else:
    print("xはNoneじゃない")


