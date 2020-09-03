# 5章　コンテナ
# メソッド

"""
print("hello".upper( ))
# 大文字にするメソッド
print("Hello".replace("o", "@"))
# 文字列を入れ替えるreplace

# list
# 空リスト
fruit = list( )
print(fruit)
fruit = ["Apple", "Orange", "Pear"]
print(fruit)
# 追加　append
fruit.append("Banana")
fruit.append("Peach")
print(fruit)

# どんなobjectでも一つのlistに入る
random = list( )
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")
print(random)

# list tapleは　イテラブルオブジェクト 繰り返し可能
for i in range(3):
    print(fruit[i])
try:
    print(fruit[10])  # 範囲外をしていしたらerror
except IndexError as e:
    print(e)

# listはミュータブル　変更可能です
colors = ["blue", "green", "yellow"]
print(colors)
colors[2] = "red"  # index2をredに入れ替え
print(colors)

# listから末尾を取り除く　pop
# popは空listには使えない
print(colors)
item = colors.pop( )
print(item)
print(colors)

# listの連結　+
colors1 = ["blue", "green", "yellow"]
colors2 = ["orange", "pink", "black"]
print(colors1 + colors2)

# 含まれているか調べる　調べたいもの　in　ソースリスト
print("green" in colors)  # boolを返す

# 含まれていないことを調べる　not in
print("black" not in colors)

# 要素数　len
print(len(colors))

# sample
colors = ["purple", "orange", "green"]
guess = input("何色かな？：")

if guess in colors:
    print("大当たり！")
else:
    print("ハズレやでぇ")

# タプル
# タプルはイミュータブル　変更不可　tuple

my_tuple = tuple( )
print(my_tuple)

rndm = ("M.Jackson", 1958, True)
print(rndm)

# 一つの要素のtupleは,をつけて書く
print(("一つだけのタプル",))
print((9) + 1)
print("上のは計算の（）と認識される")

# tupleに追加すると例外エラー
dys = ("1984", "Brave New World")
try:
    dys[1] = "Handmaid's Tale"
except TypeError as e:
    print(e)
# 要素の取り出しはインデックスで位置を指定
print(dys[1])
# 要素が含まれているかどうかはlistと同じようにin

print("1983" in dys)
print("1984" in dys)
print("1984" not in dys)

# tupleは要素を変更したくない場合やdictのキーに


# 辞書　dict ミュータブル（キー、バリュー）

# 辞書を作る
my_dict = dict( )
print(my_dict)
my_dict = {}
print(my_dict)

# キーバリューペアの追加
fruits = {"Apple": "Red",
          "Banana": "Yellow"}
print(fruits)
# 辞書はキーの順番が保存されるかどうか実装によって違う

facts = dict( )
# 追加と参照
facts["code"] = "fun"
print(facts)
print(facts["code"])
facts["Bill"] = "Gates"  # 追記となる
facts["founded"] = 1776  # int型
print(facts)
# in はキーが含まれるかどうか　バリューを確認するものではない boolを返す
print(1776 in facts)
print("founded" in facts)
# 無いキーでバリューを取り出そうとするとerror
try:
    print(facts["12"])
except KeyError as e:
    print(e)
print("founded" not in facts)

# 辞書の削除　del キーを指定する
print(facts)
del facts["founded"]
print(facts)

# sample
songs = {"1": "fun",
         "2": "blue",
         "3": "me",
         "4": "floor",
         "5": "live"
         }
n = input("数字を入れてね！：")
if n in songs:
    song = songs[n]
    print(song)
else:
    print("見つからないよ")
"""
# コンテナの中のコンテナ
lists = list( )
rap = ["a", "b", "c"]
rock = ["r", "g", "b"]
djs = ["p", "k", "k"]
lists.append(rap)
lists.append(rock)
lists.append(djs)
print(lists)
print(lists[0])
rap.append("BBQ")  # rapに追加したらlistsも更新される
print(lists[0])

# tupleとlistの組み合わせも可能
locations = []
la = (1, 1)
chi = (2, 2)
locations.append(la)
locations.append(chi)
print(locations)

a = ["a", "b"]
x = ["x", "y"]

tuple_data = (a,x)
print(tuple_data)

bday = {"Hemingway": "7.21",
        "Fitz": "9.24"}
my_list = [bday]
print(my_list)
my_tuple =(bday,)
print(my_tuple)

ny = {
    "座標":(1,2),
    "セレブ":["うでぃあれん",
           "ジェイ",
           "ケビン",
    ],
    "事実":{
        "州":"ニューヨーク",
        "国":"アメリカ",
            }
}
print(ny)