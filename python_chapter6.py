#6章

# """これ
"""文字列を複数各場合は
    3重quotoで囲む
"""

#インデックス
author = "Kafka"
for i in range(len(author)):
    print(author[i])
print(author[0]) #0で一番最初の文字　インデックス値

#print(author[5])
#indexのよりも大きな値はerror

#マイナスindex 後ろから数えて1番目が-1
print(author[-1])
author = "あいうえお"
print(author[-2])

#文字列はイミュータブル　tupleと一緒で追加は削除ができない
ff = "F. Fitzgerald"
ff = "F. Scott Fitzgerald"
print(ff)
#replaceとかそういうメソッドでいくらでも何とでもなる

#文字列の足し算
print("あ" + "い" +"う ")
print(ff+"テスト")
#文字列の掛け算　掛け算もできる　文字が増える
print(ff * 3)
#upper()method 大文字にする
print(ff.upper())
#lower() method 小文字にする
test = "TEST"
print(test.lower())
#capitalize 最初の文字を大文字にする
print(test.capitalize())

#書式化　後で置き換えする　format
print("こんにちは、{}です。".format("なかとみはるき"))
#変数も渡せる
name = "なかとみのりこ"
print("こんにちは、{}です。".format(name))
#{}はなんども使える
year_born = "1979年"
print("{}は{}に生まれました。".format(name, year_born))
#inputと組み合わせると便利
what = input("何が：")
when = input("いつ：")
where = input("どこで：")
do = input("どうした：")
r = "{}は{}に{}で{}。".format(what, when, where, do)
print(r)






