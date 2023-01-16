# 백준 - 실버2 - 스타트와 링크 - 완전 탐색, 백 트래킹, 재귀 문제
'''
완전 탐색, 백 트래킹, 재귀 문제

n // 2 크기로 재귀를 돌면서 ck가 검사 중인 항목을 team_1, ck가 방문하지 않은 부분은 team_2에 값을 담는다.
두 값의 차의 절댓값과, res를 10_000_000 크기보다 작은 값으로 res 값을 갱신한다.
'''

n = int(input())
team = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n = 4
# team = [ [0,1,2,3], [4,0,5,6], [7,1,0,2], [3,4,5,0] ] # 0
# n = 6
# team = [ [0, 1, 2, 3, 4, 5], [1, 0, 2, 3, 4, 5], [1, 2, 0, 3, 4, 5],
#         [1, 2, 3, 0, 4, 5], [1, 2, 3, 4, 0, 5], [1, 2, 3, 4, 5, 0] ] # 2
# n = 9
# team = [ [0, 5, 4, 5, 4, 5, 4, 5], [4, 0, 5, 1, 2, 3, 4, 5],
#         [9, 8, 0, 1, 2, 3, 1, 2], [9, 9, 9, 0, 9, 9, 9, 9],
#         [1, 1, 1, 1, 0, 1, 1, 1], [8, 7, 6, 5, 4, 0, 3, 2],
#         [9, 1, 9, 1, 9, 1, 0, 9], [6, 5, 4, 3, 2, 1, 9, 0] ] # 1

ck = [0] * n
res = 10_000_000

def dfs(depth, idx):
    global res

    if depth == n // 2:
        team_1, team_2 = 0, 0

        for i in range(n):
            for j in range(n):
                if ck[i] and ck[j]:
                    team_1 += team[i][j]
                elif not ck[i] and not ck[j]:
                    team_2 += team[i][j]
        res = min(res, abs(team_1 - team_2))
        return
    
    for i in range(idx, n):
        if not ck[i]:
            ck[i] = 1
            dfs(depth + 1, i + 1)
            ck[i] = 0

dfs(0, 0)
print(res)
