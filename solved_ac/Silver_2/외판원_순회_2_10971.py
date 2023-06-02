# 백준 - 실버2 - 외판원 순회 2 - 10971 - 완전 탐색, 백 트래킹, 외판원 순회(Traveling Salesman Problem, TSP) 문제
'''
완전 탐색, 백 트래킹, 외판원 순회(Traveling Salesman Problem, TSP) 문제

문제를 이해하고 풀었다기 보다는 손으로 많이 계산해보고 다른 사람들 코드들을 참고해서 이해하려다가 다른 사람코드들이 외워져서 문제를 이해하기 전에 풀렸다...
  - (뭔가 이상하게 해당 문제가 이해가 잘 되지 않는다. 유튜브도 찾아보고 글도 찾아봤는데... 느낌이 빡 오는 만족스러운 글을 못 찾았다.)
https://pythontutor.com/visualize.html#mode=edit 여기 링크에서 아래 코드로 문제에 주어진 예제를 실행하면 895 step이 나오는 데
stop 하나 씩 모두 돌려보고, 손으로도 풀어보고 어느정도 감은 잡혔는 데, 아직 설명한 실력은 안돼서 며칠동안 dfs 또는 재귀 문제들을 연습하려고 한다.
재귀에 대한 이해를 좀 더 높이면 해당 문제도 감이 잡힐거 같아서 이 문제에 대한 설명은 그때 다시 적겠다.
'''

n = int(input())
board = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n = 4
# board = [ [0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0] ] # 35

ck = [0] * n
res = int(1e9)

def dfs(start, now, cost, cnt):
    global res
    if cnt == n:
        if board[now][start]:
            cost += board[now][start]
            res = min(res, cost)
        return
    if cost > res:
        return
    
    for i in range(n):
        if ck[i] == 0 and board[now][i]:
            ck[i] = 1
            dfs(start, i, cost + board[now][i], cnt + 1)
            ck[i] = 0

for i in range(n):
    if ck[i] == 0:
        ck[i] = 1
        dfs(i, i, 0, 1)
        ck[i] = 0

print(res)
