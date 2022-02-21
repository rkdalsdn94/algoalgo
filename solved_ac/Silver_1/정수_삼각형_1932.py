'''
dp 문제이긴 한데, 난이도가 높지 않아 손으로 예제를 풀다가 감이 왔다.
j == 0 --> 삼각형 중에 제일 왼쪽
i == j --> 삼각형 중에 제일 오른쪽
else -->   삼각형 중 가운데
'''

n = int(input())
n_list = [ list(map(int, input().split())) for _ in range(n) ]
# print(n, n_list)

# 테스트
# n, n_list = 5, [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]] # 30

for i in range(1, n):
    for j in range(i + 1):
        if j == 0: # 제일 왼쪽
            n_list[i][j] = n_list[i-1][j] + n_list[i][j]
        elif i == j: # 제일 오른쪽
            n_list[i][j] = n_list[i-1][j-1] + n_list[i][j]
        else: # 가운데 부분
            n_list[i][j] = max(n_list[i-1][j-1] + n_list[i][j], n_list[i-1][j] + n_list[i][j])

print(max(n_list[-1]))

