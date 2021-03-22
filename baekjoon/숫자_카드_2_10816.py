from collections import Counter
n = 10
n_list = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
m = 8
m_list = [10, 9, -5, 2, 3, 4, 5, -10]  # 3 0 0 1 2 0 0 2
# n = int(input())
# n_list = list(map(int,input().split()))
# m = int(input())
# m_list = list(map(int, input().split()))

n_list = Counter(n_list)

res = []

for i in m_list:
    res.append(n_list[i])

print(*res)