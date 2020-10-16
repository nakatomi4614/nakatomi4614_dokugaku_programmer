# https://atcoder.jp/contests/abc114/tasks/abc114_b
n = int(input())
S_list = list(map(int, input( ).split( )))
i = 1
result_list = []
for H_i in S_list:
    if H_i >= max(S_list[:i]):
        result_list.append(H_i)
    i = i + 1
print(len(result_list))
