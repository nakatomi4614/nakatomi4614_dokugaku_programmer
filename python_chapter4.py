#関数定義 def

def f(x):
    return  x * 2

result = f(2) # f(x) に　2を代入した結果
print(result)


def ｇ(x):
    return x + 1
z = g(4)

if z == 5:
    print("z is 5")
else:
    print("z is not 5")

#変数の無いもの
def f_1():
    return 1+1
result = f_1()
print(result)

#変数を複数とる関数
def f_2(x, y, z):
    return x + y + z
result = f_2(1,2,3)
print(result)

#returnがない場合はnone
def f_3():
    z = 1+1
result =f_3()
print(result)
