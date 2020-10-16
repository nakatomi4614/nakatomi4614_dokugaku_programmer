# https://atcoder.jp/contests/abc114/tasks/abc114_b
# S_list = list(map(int, input( ).split( )))
n = input()
result_list = []
for i in range(len(n)):
    result_list.append(abs(int(n[i:i+3])- 753))
print(min(result_list))
