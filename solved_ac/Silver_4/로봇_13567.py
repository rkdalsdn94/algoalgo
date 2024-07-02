# 백준 - 실버4 - 로봇 - 13567 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

0 : 동쪽
1 : 남쪽
2 : 서쪽
3 : 북쪽

풀이 과정
 1. 명령어를 입력받는다.
 2. 명령어에 따라 로봇을 이동시킨다.
 3. 로봇이 이동할 때마다 경계를 넘어가는지 확인한다.
 4. 경계를 넘어가면 -1을 출력하고 종료한다.
 5. 경계를 넘어가지 않으면 로봇의 위치를 출력한다.
'''

m, n = map(int, input().split())
command = [input().split() for _ in range(n)]

# 테스트
# m, n = 11, 14
# command = [
#     'MOVE 10'.split(), 'TURN 0'.split(), 'MOVE 2'.split(),
#     'TURN 0'.split(), 'MOVE 5'.split(), 'TURN 1'.split(),
#     'MOVE 5'.split(), 'TURN 1'.split(), 'MOVE 2'.split(),
#     'TURN 1'.split(), 'MOVE 3'.split(), 'TURN 0'.split(),
#     'TURN 0'.split(), 'MOVE 6'.split()
# ] # 7 10
# m, n = 11, 7
# command = [
#     'MOVE 5'.split(), 'TURN 0'.split(), 'MOVE 4'.split(),
#     'TURN 1'.split(), 'MOVE 2'.split(), 'TURN 1'.split(),
#     'MOVE 5'.split()
# ] # -1
# m, n = 2, 7
# command = [
#     'MOVE 2'.split(), 'TURN 0'.split(), 'MOVE 3'.split(),
#     'TURN 0'.split(), 'MOVE 2'.split(), 'TURN 0'.split(),
#     'MOVE 2'.split()
# ] # -1

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

x, y = 0, 0
d = 0

for i, j in command:
    if i == 'MOVE':
        dist = int(j)
        x += dx[d] * dist
        y += dy[d] * dist
    else:
        if j == '0':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
    
    if not (0 <= x <= m and 0 <= y <= m):
        print(-1)
        exit(0)

print(x, y)

