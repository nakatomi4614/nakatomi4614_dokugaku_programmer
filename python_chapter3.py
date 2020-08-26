#条件文

"""
もし　おなかすいている　なら:
    ご飯を食べる
そうでなければ:
    ご飯は食べない
"""

home = "アメリカ"
if home == "アメリカ":
    print("Hello, America!")
else:
    print("Hello, World!")

home = "日本"
if home == "アメリカ":
    print("Hello, America!")
else:
    print("Hello, World!")

x = 2
if x == 2:
    print("数値は２です")
if x % 2 == 0:
    print("偶数です")
if x % 2 != 0:
    print("奇数です！")

x = 10
y = 11
if x == 10:
    if y == 11:
        print(x+y)

home = "タイ"
if home == "日本":
    print("Hello, Japan!")
elif home == "タイ":
    print("Hello, Thailand!")
elif home == "インド":
    print("hello, India!")
elif home == "中国":
    print("hello, China!")
else:
    print("Hello, World!")

home = "タイ"
if home == "日本":
    print("Hello, Japan!")
elif home == "南極":
    print("Hello, Thailand!")
elif home == "インド":
    print("hello, India!")
elif home == "中国":
    print("hello, China!")
else:
    print("Hello, World!")

x = 100
if x == 10:
    print("10")
elif x == 20:
    print("20")
else:
    print("わからないです")
if x == 100:
    print("100")

if x % 2== 0:
    print("偶数")
else:
    print("奇数")