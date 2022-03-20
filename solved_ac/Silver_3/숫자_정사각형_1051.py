'''
구현, 완전 탐색 문제
'''

n, m = map(int, input().split())
rectangle = [ list(map(int, input())) for _ in range(n) ]

# 테스트
# n, m, rectangle = 3, 5, [[4,2,1,0,1], [2,2,1,0,0], [2,2,1,0,1]] # 9
# n, m, rectangle = 2, 2, [[1,2], [3,4]] # 1
# n, m, rectangle = 2, 4, [[1,2,5,5], [3,4,5,5]] # 4
# n, m, rectangle = 1, 10, [[1,2,3,4,5,6,7,8,9,0]] # 1
# n, m = 11, 10
# rectangle = [[9,7,8,5,4,0,9,5,0,7], [2,0,5,5,1,0,3,6,9,4], [0,8,6,1,3,9,6,7,6,1],
#             [3,0,7,3,2,0,7,6,6,9], [1,2,3,3,0,4,9,4,9,3], [2,3,0,0,2,4,8,9,6,8],
#             [9,7,6,9,2,3,9,5,4,8], [7,9,8,4,1,3,0,0,0,1], [1,6,7,0,0,2,0,0,9,5],
#             [8,8,9,4,2,3,9,8,8,9], [4,0,5,3,9,7,1,0,7,2]] # 49

ck = min(n, m)
res = 0

for i in range(n):
    for j in range(m):
        for k in range(ck):
            if ((i + k) < n) and ((j + k) < m):
                if (rectangle[i][j] == rectangle[i][j + k] == rectangle[i + k][j] == rectangle[i + k][j + k]):
                    res = max(res, (k + 1) ** 2)

print(res)
