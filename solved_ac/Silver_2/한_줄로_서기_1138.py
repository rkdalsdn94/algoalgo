n = int(input())
n_list = list(map(int, input().split()))
# 테스트 
# n = 4
# n_list = [2,1,1,0] # 4 2 1 3
# n = 5
# n_list = [0,0,0,0,0] # 1 2 3 4 5
# n = 6
# n_list = [5,4,3,2,1,0] # 6 5 4 3 2 1
# n = 7
# n_list = [6,1,1,1,2,0,0] # 6 2 3 4 7 5 1
res = [0] * n

for i in range(n):
    cnt = 0

    for j in range(n):
        if res[j] == 0 and cnt == n_list[i]:
            res[j] = i + 1
            break
        elif res[j] == 0:
            cnt += 1

print(*res)


'''
res = []
for i in range(n):
    res.insert(n_list[n-1-i], n-i)

다른 사람 풀이를 보니까 위와 같이 푸는게 더 좋아 보인다.
'''
