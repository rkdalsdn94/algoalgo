'''
제일 아래로 풀고 제출 한 후에
다른 사람 풀이 보는데 참고할 코드를 발견해서 그 코드 기반으로 수정했다.
미리 벽의 위치를 다 입력 받고
combinations를 사용해서 3개만 벽을 만든 후 제출 하니까 시간이 3000ms정도 줄었다.. 
제일 아래 4700ms -> 1048ms 로 수정
'''

from collections import deque
from copy import deepcopy
from itertools import combinations

n, m = map(int, input().split())
laboratory = [ list(map(int, input().split())) for _ in range(n) ]
# print(n, m, laboratory)

# 테스트
# n, m = 7, 7 # 27
# laboratory = [[2, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]
# n, m = 4, 6 # 9
# laboratory = [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 2], [1, 1, 1, 0, 0, 2], [0, 0, 0, 0, 0, 2]]
# n, m = 8, 8 # 3
# laboratory = [[2, 0, 0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
q = deque()
res = 0
wall_list = []

for i in range(n):
    for j in range(m):
        if laboratory[i][j] == 2:
            q.append((i, j))
        elif laboratory[i][j] == 0:
            wall_list.append((i, j))

def bfs():
    zero_cnt = 0
    dx, dy = [1,0,-1,0], [0,1,0,-1]

    for combi in combinations(range(len(wall_list)), 3):
        temp_q = deepcopy(q)
        temp_laboratory = deepcopy(laboratory)

        for com in combi:
            temp_x, temp_y = wall_list[com]
            temp_laboratory[temp_x][temp_y] = 1

        while temp_q:
            a, b = temp_q.popleft()

            for i, j in zip(dx, dy):
                nx, ny = a + i, b + j

                if 0 <= nx < n and 0 <= ny < m and temp_laboratory[nx][ny] == 0:
                    temp_laboratory[nx][ny] = 2
                    temp_q.append((nx, ny))

        zero_cnt = max(sum(i.count(0) for i in temp_laboratory), zero_cnt)        

    return zero_cnt
print(bfs())




# 처음에 아래와 같이 풀었다
'''
완전 탐색 + bfs문제이다.

바이러스(2)를 bfs로 퍼지게 하는건 전혀 어렵지않다.
근데 벽을 어떻게 세워야 되는지가 더 고민을 많이 했던 문제이다.
고민 하던 중 n, m의 크기가 최대 8인것을 보고,
빈 칸(0)으로 되어 있는 모든 곳에 벽을 세워보는 방식으로 적용했다.
처음에는 wall_cnt 라는 배열을 만든 뒤 배열의 길이가 3이 되지 않는 이상 append한 후 clear하는 쪽으로 생각하고 구현 중 실행해 보는데,
원하던대로 실행이 안돼서 디버깅을 해보니 0, 1, 2라는 곳에 벽을 세우고 이 다음에는 0, 1, 3 이런 식으로 세워야 되는데,
0, 1, 2 ---> 3, 4, 5 이렇게 나와서 재귀로 바꾼 후 통과했다.
'''

'''
from collections import deque
from copy import deepcopy

# n, m = map(int, input().split())
# laboratory = [ list(map(int, input().split())) for _ in range(n) ]
# print(n, m, laboratory)

# 테스트
# n, m = 7, 7 # 27
# laboratory = [[2, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]
# n, m = 4, 6 # 9
# laboratory = [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 2], [1, 1, 1, 0, 0, 2], [0, 0, 0, 0, 0, 2]]
n, m = 8, 8 # 3
laboratory = [[2, 0, 0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
q = deque()
res = 0

for i in range(n):
        for j in range(m):
            if laboratory[i][j] == 2:
                q.append((i, j))

def bfs():
    zero_cnt = 0
    temp_laboratory = deepcopy(laboratory)
    temp_q = deepcopy(q)
    dx, dy = [1,0,-1,0], [0,1,0,-1]

    while temp_q:
        a, b = temp_q.popleft()

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < n and 0 <= ny < m and temp_laboratory[nx][ny] == 0:
                temp_laboratory[nx][ny] = 2
                temp_q.append((nx, ny))
    
    zero_cnt = sum(i.count(0) for i in temp_laboratory)

    return zero_cnt

def wall_add(wall_add_cnt):
    global res

    if wall_add_cnt == 3:
        res = max(res, bfs())
        return

    for i in range(n):
        for j in range(m):
            if laboratory[i][j] == 0:
                laboratory[i][j] = 1
                wall_add(wall_add_cnt + 1)
                laboratory[i][j] = 0

wall_add(0)
print(res)
'''