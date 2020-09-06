# いろいろなループ　for while break continue

"""
name = "Ted"
for character in name:
    print(character)

shows = ["GOT", "Narcos", "Vice"]  # listの要素を取り出す
for show in shows:
    print(show)

coms = ("A.Development", "Friends", "Always sunny")  # tupleも同じ
for show in coms:
    print(show)

people = {"G.Bluth II": "A. Development",
          "Barney": "HIMYM",
          "Dennis": "Always Sunny"
          }
for character in people:
    print(character)

tv = ["GOT", "Narcos", "Vice"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper( )  # .upper()は文字列を大文字にするメソッド
    tv[i] = new
    i += 1

print(tv)

for i, new in enumerate(tv):

# enumerate()はforループの中でリストやタプルなどの
# イテラブルオブジェクトの要素と同時にインデックス番号（カウント、順番）を取得できる
    new = tv[i]
    new = new.upper( )
    tv[i] = new

print(tv)

tv = ["GOT", "Narcos", "Vice"]
coms = ["Arrested Development", "friends", "Always Sunny"]
all_shows = []

for show in tv:
    show = show.upper( )
    all_shows.append(show)  # append()はリストに追加する関数

for show in coms:
    show = show.upper( )
    all_shows.append(show)

print(all_shows)

# range
for i in range(1, 11):
    print(i)

# whileループ
x = 10
while x > 0:
    # 正の数までループ
    print("{}".format(x))  # {}内に.format()メソッドでひとつづつ表示する
    x -= 1
    # 1づつ減らす
print("Happy New Year!")

# whileの無限ループ
while True:
    print("Hello, World!")
    # breakしないと止まらない
    break

for i in range(0, 100):
    # 0から100回表示するので、99まで表示される
    print(i)

for i in range(0, 100):
    print(i)
    break
    # breakで一回で終わり　　breakまで来たらすぐに終了する

# whileとbreakの組み合わせ
qs = ["What is your name?",
      "What is your fav. color?",
      "What is your quest?"]
n = 0
# nはインデック値
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3
    # nは0,1,2の繰り返しになる

# continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
    # 　i == 3の時にcontinue文が実行される。
    # loopは終了しないで実行されない
# whileとcontinueで同じ内容を
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
        # 3でcontinue
    print(i)
    i += 1

# 入れ子ループ
for i in range(1, 3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)
    # 3は入らない1,2のみ
    # iを1つやった後letterの全ループして、i=2でおわり
"""
# 二つのlistから
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)
# 1+5,1+6って感じ

#whileの入れ子にfor
while input("y or n?") != "n":
    for i in range(1,6):
        print(i)
    #nを押したら終了(nじゃなかったら下のforを実行）


