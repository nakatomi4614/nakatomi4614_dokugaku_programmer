#https://atcoder.jp/contests/abc129/tasks/abc129_b
n = int(input())
S_list = list(map(int, input().split()))
sum_all = sum(S_list)
sum_1 = 0
sum_list =[]
for i in S_list:
    sum_1 = sum_1 + i
    sum_2 = sum_all - sum_1
    sum_list.append(abs(sum_1-sum_2))
print(min(sum_list))



