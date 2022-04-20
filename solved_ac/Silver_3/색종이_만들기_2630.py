'''
분할 정복, 재귀 문제

종이의 개수(백준 - 1780)랑 비슷한 문제다.
재귀 조건만 다르고 다른 풀이 방식은 완전 똑같이 했다.
문제 그림상에도 나와 있듯이 / 2 하면서 재귀적으로 접근했다.
'''

n = int(input())
paper = [ list(map(int, input().split())) for _ in range(n) ]
# print(n, paper)

# 테스트
# n = 8 # out: 9 \n 7
# paper =[[1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1],
#         [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0],
#         [1, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
#         [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1]]

white_cnt, blue_cnt = 0, 0

def dfs(x, y, n):
    global white_cnt, blue_cnt
    temp = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != temp:
                new_n = n // 2
                dfs(x, y, new_n)
                dfs(x, y + new_n, new_n)
                dfs(x + new_n, y, new_n)
                dfs(x + new_n, y + new_n, new_n)
                return
    if temp == 0:
        white_cnt += 1
    else:
        blue_cnt += 1

dfs(0, 0, n)
print(white_cnt, blue_cnt, sep='\n')
