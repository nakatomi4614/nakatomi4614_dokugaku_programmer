#インタープリタ直接入力を行った。
#変数に代入して演算を行った。

#文字列 listは複数の型のものをいっしょにできる
a = 1 #コメントできる
#関数
def add(a,b):
    return a+b
print(add(1,3))
#インデント自体が構造となる

#組み込み関数
print(round(10.4)) #小数点を丸める

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)
    return num
for num in range(1,101):
    print(fizzbuzz(num))

n1 = 100
s1 = "hello"
l1 = [1, 2, 3]
print(type(n1))
print(type(s1))
print(type(l1))
print(isinstance(n1,int)) #isinstanceは二番目の項と一番目の項が同じならTrue

import collections.abc
print(isinstance(s1,collections.abc.Sequence))
