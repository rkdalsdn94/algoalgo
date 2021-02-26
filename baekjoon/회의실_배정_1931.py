# n = 11
# n_list = [ [1, 4],[3, 5],[0, 6],[5, 7],[3, 8],[5, 9],
#     [6, 10],[8, 11],[8, 12],[2, 13],[12, 14] ]
n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 회의가 끝나는 시간을 기준으로 정렬 후, 회의 시작 시간 정렬
n_list = sorted(n_list, key=lambda x: (x[1], x[0]))
temp, res = 0, 0
for i, j in n_list:
    if i >= temp:
        temp = j
        res += 1
print(res)
    