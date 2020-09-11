# chapter13
# object指向プログラミングの4大要素
# カプセル化　抽象化　ポリモーフィズム　継承

# カプセル化
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len


# width lenがインスタンス変数　オブジェクトという単位にまとめられている
# areaも同様
rectangle = Rectangle(10, 20)  # global変数に代入して
print(rectangle.area( ))  # .area()メソッドで面積計算


class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n


# 直接書き換え
data_one = Data( )
data_one.nums[0] = 100  # tupleだとこういうことはできない
print(data_one.nums)

# change_dataメソッド
data_two = Data( )
data_two.change_data(0, 100)
print(data_two.nums)


class PublicPrivateExample:  # PPEって感じで大文字にする。自動修正できない
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        # clientがつかってよい
        pass  # 文が必須な構文で何もしないときにpassを使う

    def _unsafe_method(self):
        # clientは使うべきではない
        pass


# _(アンダースコア）から始まって売り変数やメソッドは使わない

# 抽象化　必要なものだけにしたもの。いらないものは取り除くこと。

# ポリモーフィズム
# 同じインターフェース（関数やメソッド）でありながら、データ型に合わせて異なる動作をする機能
print(type("Hello, World!"))
print(type(200))
print(type(200.1))


# ダックタイピング　期待通り動くならそれでよいという考え方

# 継承　継承元を親クラス　継承先を子クラス
class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} かける {}".format(self.width, self.len))


# 子クラス
# 親クラスの変数とメソッドと引き継いでいる
class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("私は　{} かける　{}　です。".format(self.width, self.len))


my_shape = Shape(20, 25)
print(my_shape.print_size( ))
a_square = Square(20, 20)
print(a_square.area( ))
print(a_square.print_size( ))


# 子クラスが親クラスのメソッドを別の実装で置き換えることをメソッドオーバーライド
# print_size()もオーバーラードして別メッセージになっている

# コンポジション　has-a関係？ 別クラスのオブジェクトを変数として持たせる
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Person:
    def __init__(self, name):
        self.name = name


mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner.name)
