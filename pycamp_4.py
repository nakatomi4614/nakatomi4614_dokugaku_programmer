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

