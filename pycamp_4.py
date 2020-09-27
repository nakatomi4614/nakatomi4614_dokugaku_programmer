#データ型　list tuple dict

#list
examplelist = ["spam","egg","0.5"]
print(examplelist)

print(['spam', 'ham'] + ['egg'])              # リストの結合
print(['spam'] * 5)                           # リストの繰り返し
print(['spam', 'ham', 'egg'][0])              # リストの0番目を取得する
print(['spam', 'ham', 'egg'][1:])             # リストのスライス(1番目以降)
print(len(['spam', 'ham', 'egg']))            # リストの長さ
print('ham' in ['spam', 'ham', 'egg'])        # リストに特定の文字列が含まれるか

for animal in ['cat', 'dog', 'snake']:
    print(animal)

#追加　.append()
animals = ['cat', 'dog', 'snake']
animals.append("elephant")
print(animals)

#内包表記
#通常表記
ret = []
for animal in animals:
    ret.append(len(animal))
print(ret)
#リスト内包表記 一番前の処理をする　二番目に取り出す　三番目がイテレータ
print([len(animal) for animal in animals])

#アンパック
dog , cat = ["dog","cat"]
print(dog,cat)

#tupleもリストと同様
#listとの違い
#１要素tupleの場合でもカンマがいる
print(("spam",))
#かっこがない場合はtupleとなる
exampletuple = "dog","cat"
print(exampletuple)

#tupleを返す関数
def head_splitter(seq):
    return seq[0], seq[1:]

head, tail = head_splitter(['head', 'body', 'tail'])
print(head)
print(tail)

def bad_implementation():
    return 'username', 'user_password', 'user_id', 'user_permission1', 'user_permission2'

print(bad_implementation())

#dict　要素にindexを持っていない　keyとvalueを持つ
user_info = {'user_name': 'taro', 'last_name': 'Yamada'}
print(user_info)
print(user_info["user_name"])
#追加は辞書[key]="value"
user_info["first_name"] = "Taro"
print(user_info)
#in演算子 含まれるかどうか
print("user_name" in user_info)
print("bio" in user_info)
#.get()でvalueを獲得する。ない場合はNone
print(user_info.get('user_name'))
bio = user_info.get('bio')
print(bio)
bio = user_info.get('bio' ,'') #二番目はデフォルト値
print(bio)

#for
user_info = {'user_name': 'taro', 'last_name': 'Yamada'}
for key in user_info:
    print(key)
    print(user_info[key])
#keyを抜き出す

#.keys()メソッド、.values()メソッド、.items()メソッド
d = {'foo': 'spam', 'bar': 'ham'}
print(d.items()) #key valueをtupleで
d = {'foo': 'spam', 'bar': 'ham'}
#keyとvalueを分けて受け取る
for key, value in d.items():
    print(key, value)
#set 順序を持たない　追加はできる
print({'spam', 'ham'})
print({'spam', 'spam', 'spam'})
#同じものは一つとみなす　一意の値しかとらない
unique_users = {'dog', 'cat'}
unique_users.add('snake')
print(unique_users)
print(len(unique_users))
unique_users.add('snake')
print(len(unique_users))

#集合の積和 積and & 和or |
allowed_permissions = {'edit', 'view'}
requested_permissions = {'view', 'delete'}
print(allowed_permissions & requested_permissions)

editor = {'edit', 'comment'}
reviewer = {'comment', 'approve'}
print(editor | reviewer)

