#5章　コンテナ
#メソッド

print("hello".upper())
#大文字にするメソッド
print("Hello".replace("o","@"))
#文字列を入れ替えるreplace

#list
#空リスト
fruit = list()
print(fruit)
fruit = ["Apple", "Orange", "Pear"]
print(fruit)
#追加　append
fruit.append("Banana")
fruit.append("Peach")
print(fruit)

#どんなobjectでも一つのlistに入る
random = list()
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")
print(random)

#list tapleは　イテラブルオブジェクト 繰り返し可能
for i in range(3) :
    print(fruit[i])
try:
    print(fruit[10]) #範囲外をしていしたらerror
except IndexError as e:
    print(e)

#listはミュータブル　変更可能です
colors = ["blue", "green", "yellow"]
print(colors)
colors[2] = "red" #index2をredに入れ替え
print(colors)

#listから末尾を取り除く　pop
#popは空listには使えない
print(colors)
item = colors.pop()
print(item)
print(colors)

#listの連結　+
colors1 = ["blue", "green", "yellow"]
colors2 = ["orange", "pink", "black"]
print(colors1+colors2)

#含まれているか調べる　調べたいもの　in　ソースリスト
print("green" in colors) #boolを返す

#含まれていないことを調べる　not in
print("black" not in colors)

#要素数　len
print(len(colors))

#sample
colors = ["purple", "orange", "green"]
guess = input("何色かな？：")

if guess in colors:
    print("大当たり！")
else:
    print("ハズレやでぇ")




