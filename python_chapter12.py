# chapter12
# プログラミングパラダイム

"""
# 手続き型
x = 2
y = 4
z = 8
xyz = x + y + z
print(xyz)
#dataがグローバル変数

pop = []
jpop = []

def collect_songs():
    song = "曲名を入力してください："
    ask = "pかjのどちらかを入力してください。qで終わります。"

    while True:
        genre = input(ask)
        if genre == "q":
            break
        if genre == "p":
            p=input(song)
            pop.append(p)
        elif genre == "j":
            j =input(song)
            jpop.append(j)
        else:
            print("不正な値です。")
    print("pop songs: ",pop)
    print("jpop songs: ", jpop)

collect_songs()
#すべてをグローバル変数に置くと問題が発生する複雑なプログラムだととくに
"""

# 関数型プログラム
# 副作用の例
"""
a = 0
def increment():
    global a
    a += 1



def increment(a):
    return a + 1


print(increment(3))


# グローバルステートを持たないので扱いにくい問題がある

# オブジェクト指向型
# class クラス名：クラス名の最初は大文字で書くのが慣例
#   スイート（中身か？）

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")
    
    def rot(self,days,temp):
        self.mold = days * temp

or2=Orange(8,"dark orange")
or3=Orange(14,"yellow")

print(or1)
print(or2.weight)
print(or3.color)
"""

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp


orange = Orange(200, "orange")
print(orange.mold)
orange.rot(10,37)
print(orange.mold) #days*tempをmoldに渡す

#object指向
class Rectangle:
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def area(self):
        return self.width *self.len

    def change_size(self,w,l):
        self.width = w
        self.len = l

rectangle = Rectangle(10,20)
print(rectangle.area())
rectangle.change_size(20,40)
print(rectangle.area())
