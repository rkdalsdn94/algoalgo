'''
빛이 "S"가 써진 칸에 도달한 경우, 직진합니다.
빛이 "L"이 써진 칸에 도달한 경우, 좌회전을 합니다.
빛이 "R"이 써진 칸에 도달한 경우, 우회전을 합니다.
빛이 격자의 끝을 넘어갈 경우, 반대쪽 끝으로 다시 돌아옵니다. 예를 들어, 빛이 1행에서 행이 줄어드는 방향으로 이동할 경우, 같은 열의 반대쪽 끝 행으로 다시 돌아옵니다.
'''
def solution(grid):
    answer = []
    dx, dy = [1,0,-1,0], [0,1,0,-1]

    ck = [[[0] * 4 for _ in range(len(grid))] for _ in range(len(grid[0])) ]

    return sorted(answer)

print(solution(["SL","LR"])) # [16]
print(solution(["S"])) # [1,1,1,1]
print(solution(["R","R"])) # [4,4]

