# 백준 - 실버3 - 거북이 - 8911 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

구현의 난이도는 크게 어렵지 않는데, 문제에서 요구하는 조건들이 까다로운 문제이다.
확실히 시뮬레이션이라 젹혀있는 문제들은 괜히 빡구현(?)이라는 별명이 붙은게 아닌거 같다.

문제에 주어진 요구사항대로 계산하고 넓이를 구하기 위해 절댓값을 이용해 가로 세로의 길이를 구한 뒤 두 길이의 곱을 출력하면 된다.
문제에 주어진 요구사항은 다음과 같다.
1. F: 한 눈금 앞으로
2/ B: 한 눈금 뒤로
3. L: 왼쪽으로 90도 회전
4. R: 오른쪽으로 90도 회전

in
    3
    FFLF
    FFRRFF
    FFFBBBRFFFBBB
out
    2
    0
    9
'''

t = int(input())
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0] # 북, 서, 남, 동

for _ in range(t):
    command = list(input())
    direction = 0
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    x, y = 0, 0

    for i in command:
        if i == "F":
            x, y = x + dx[direction], y + dy[direction]
        elif i == "B":
            x, y = x - dx[direction], y - dy[direction]
        elif i == "L": # 거북이의 방향을 바꾸기 위해
            if direction == 3: # 3 이면 현재 방향이 동쪽이므로 위 순서대로 봤을 때 다시 0(북쪽)을 보게 해야된다.
                direction = 0
            else:
                direction += 1
        elif i == "R": # L의 반대라고 생각하면 된다.
            if direction == 0:
                direction = 3
            else:
                direction -= 1
        min_x, max_x = min(x, min_x), max(x, max_x)
        min_y, max_y = min(y, min_y), max(y, max_y)

    print(abs(max_x - min_x) * abs(max_y - min_y))
