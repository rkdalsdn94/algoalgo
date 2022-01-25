n = int(input())
n_list = [ list(map(int, list(input().split()))) for _ in range(n) ]
# 테스트
# n = 5
# n_list = [[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]] # 2 2 1 2 5
res = []

for i in n_list:
    cnt = 1
    
    for j in n_list:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1

    res.append(cnt)

print(*res)
