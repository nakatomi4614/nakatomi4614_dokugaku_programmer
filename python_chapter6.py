# 6章

# """これ
"""文字列を複数各場合は
    3重quotoで囲む
"""

"""
# インデックス
author = "Kafka"
for i in range(len(author)):
    print(author[i])
print(author[0])  # 0で一番最初の文字　インデックス値

# print(author[5])
# indexのよりも大きな値はerror

# マイナスindex 後ろから数えて1番目が-1
print(author[-1])
author = "あいうえお"
print(author[-2])

# 文字列はイミュータブル　tupleと一緒で追加は削除ができない
ff = "F. Fitzgerald"
ff = "F. Scott Fitzgerald"
print(ff)
# replaceとかそういうメソッドでいくらでも何とでもなる

# 文字列の足し算
print("あ" + "い" + "う ")
print(ff + "テスト")
# 文字列の掛け算　掛け算もできる　文字が増える
print(ff * 3)
# upper()method 大文字にする
print(ff.upper( ))
# lower() method 小文字にする
test = "TEST"
print(test.lower( ))
# capitalize 最初の文字を大文字にする
print(test.capitalize( ))

# 書式化　後で置き換えする　format
print("こんにちは、{}です。".format("なかとみはるき"))
# 変数も渡せる
name = "なかとみのりこ"
print("こんにちは、{}です。".format(name))
# {}はなんども使える
year_born = "1979年"
print("{}は{}に生まれました。".format(name, year_born))

# inputと組み合わせると便利
what = input("何が：")
when = input("いつ：")
where = input("どこで：")
do = input("どうした：")
r = "{}は{}に{}で{}。".format(what, when, where, do)
print(r)

# split　分割 特定の文字を境に分割をする
string = "昨日から台風が近づいています。気を付けてください！"
print(string.split("。"))
# リストを返す

# join 結合 文字列の間に文字列を追加する
first_three = "abc"
result = "+".join(first_three)
print(result)

# joinメソッドの引数にリストを渡す
words = ["The", "fox", "jumped","over","the","fence","."]
one = " ".join(words)
print(one)
#空白文字をリストの間に入れる

#空白除去 strip
s = "   あんドー  ナツ　　　　"
print(s)
print(s.strip())
#.strip()は最初と最後の空白を取り除く 半角全角問わない

#置換　replace
equ = "All animals are equal."
equ = equ.replace("a","@")
print(equ)
#aを@に置換している

#文字を探す
print(equ.index("n"))
#ない場合はValueError
try:
    "animals".index("z")
except ValueError as e:
    print(e)

#包含　in演算子で指定文字列が含まれているかどうか探す　戻り値はbool
s = "Cat in the hat."
print("Cat" in s)
#含まれるのでTrue
print("Catt" in s)
#含まれないのでFalse
#not in で含まれないことを確認できる
print("Cat" not in s)
#含まれているのでFalse
#escape文字
print("彼女は"そうだね"と言った。")
"""
print("彼女は \"そうだね\" と言った。")
# \をエスケープ文字といい、特別な意味を持たせる。
# https://www.javadrive.jp/python/string/index2.html
print("一行目\n二\'行目\"")
# \nは改行

# スライス　一部分を取り出す[開始:終了]
fict = ["トルストイ", "カミュ", "オーウェル", "ハクスリー", "オースティン"]
print(fict[0:3]) #1番目から3番目まで表示　インデックス0,1,2を表示

#文字のスライス
ivan = "死の代わりに一つの光があった。"
print(ivan[0:6])
print(ivan[6:16])
#開始indexが0の場合は省略可
print(ivan[:6])
#最後まで含む場合は終了インデックスを省略できる。
print(ivan[6:])

