'''
빛이 "S"가 써진 칸에 도달한 경우, 직진합니다.
빛이 "L"이 써진 칸에 도달한 경우, 좌회전을 합니다.
빛이 "R"이 써진 칸에 도달한 경우, 우회전을 합니다.
빛이 격자의 끝을 넘어갈 경우, 반대쪽 끝으로 다시 돌아옵니다. 예를 들어, 빛이 1행에서 행이 줄어드는 방향으로 이동할 경우, 같은 열의 반대쪽 끝 행으로 다시 돌아옵니다.
'''
from collections import deque

def solution(grid):
    answer =[]
    len_x, len_y = len(grid),len(grid[0])
    ck = [[[0]*4 for _ in range(len_y)] for _ in range(len_x)]
    dx, dy = [1,-1,0,0], [0,0,-1,1]
    light_direction = {'S':{0:0,1:1,2:2,3:3},'L':{0:3,1:2,2:0,3:1},'R':{0:2,1:3,2:1,3:0}}

    for i in range(len_x):
        for j in range(len_y):
            for k in range(4):
                if ck[i][j][k] == 0:
                    queue = deque([(i,j,k,1,[i,j,k])])
                    ck[i][j][k] = 1

                    while queue:
                        a, b, c, cnt, first_time = queue.popleft()
                        nx, ny = a + dx[c], b + dy[c]

                        if nx == len_x: nx = 0
                        elif nx < 0: nx = len_x-1

                        if ny == len_y: ny = 0
                        elif ny < 0: ny = len_y-1

                        temp = light_direction[grid[nx][ny]][c]

                        if [nx,ny,temp] == first_time:
                            answer.append(cnt)
                        else:
                            ck[nx][ny][temp] = 1
                            queue.append((nx,ny,temp,cnt+1,first_time))
    return sorted(answer)
print(solution(["SL","LR"])) # [16]
print(solution(["S"])) # [1,1,1,1]
print(solution(["R","R"])) # [4,4]
