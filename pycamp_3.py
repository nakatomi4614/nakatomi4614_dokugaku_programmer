#データ型
#int 整数型
print(1+2,2-4,6*9,10/3,5%2, 5**2,10//3)
#float 浮動小数点
print(5.0+5.2)
#strは”or'でかこんだものどっちもいっしょ
print("テスト", 'ﾃｽﾄ')
#エスケープシーケンス
print('I\'m Hiroki')
print('Hello\nworld')
print("I'm Hiroki") #ダブルクオートで囲めばシングルクオートが表示される
#対話モードでは'foo\nbar\nbaz\n'
"""foo
bar
baz
"""
print("Mt."+"Fuji")
print("spam" * 5) #文字の繰り返し

print("python"[1])

print("python"[2:5]) #スライス
print("python"[:3])
print("python"[4:])
print(len("python"))

print("t" in "python") #後ろの文字列に前の文字列が含まれるかどうか
print("k" in "python")
print("th" in "python")

#文字列の分割　.split() 区切り文字で区切ってlistを作る
print("pain-au-chocolat".split("-"))

#.join()　結合
print("-".join(["pain", "de", "campagne"]))

