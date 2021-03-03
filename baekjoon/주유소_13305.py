# n = 4
# road = [2, 3, 1]
# oil = [5, 2, 4, 1] # 18
# n = 4
# road = [3, 3, 4]
# oil = [1, 1, 1, 1] # 10
n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))
res = 0
temp = oil[0]
for i in range(len(road)):
    if temp > oil[i]:
        temp = oil[i]
    res += temp * road[i]

print(res)
