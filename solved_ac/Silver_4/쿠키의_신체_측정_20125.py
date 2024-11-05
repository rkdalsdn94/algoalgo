# 백준 - 실버4 - 쿠키의 신체 측정 - 20125 - 구현 문제
'''
구현 문제

풀이 과정
  1. 입력을 받아서 보드에 저장한다.
  2. 보드에서 심장의 위치를 찾는다. 심장은 '*'들 중에서 몸통의 시작 부분이므로 이를 기준으로 위치를 결정한다.
  3. 심장을 기준으로 왼팔, 오른팔, 몸통, 왼다리, 오른다리의 길이를 각각 구한다.
     - 왼팔: 심장에서 왼쪽으로 이어지는 '*'의 개수
     - 오른팔: 심장에서 오른쪽으로 이어지는 '*'의 개수
     - 몸통: 심장에서 아래로 이어지는 '*'의 개수
     - 왼다리: 몸통 끝에서 왼쪽 다리 방향으로 이어지는 '*'의 개수
     - 오른다리: 몸통 끝에서 오른쪽 다리 방향으로 이어지는 '*'의 개수
  4. 각 부위의 길이를 계산한 후 출력한다.
'''

n = int(input())
board = [list(input()) for _ in range(n)]

# 테스트
# n = 5
# board = [
#     list('_____'),
#     list('__*__'),
#     list('_***_'),
#     list('__*__'),
#     list('_*_*_'),
# ] # 3 3  \  1 1 1 1 1
# n = 10
# board = [
#     list('__________'),
#     list('_____*____'),
#     list('__******__'),
#     list('_____*____'),
#     list('_____*____'),
#     list('_____*____'),
#     list('____*_*___'),
#     list('____*_____'),
#     list('____*_____'),
#     list('____*_____')
# ] # 3 6  \  3 2 3 4 1
# n = 9
# board = [
#     list('____*____'),
#     list('*********'),
#     list('____*____'),
#     list('____*____'),
#     list('____*____'),
#     list('___*_*___'),
#     list('___*_*___'),
#     list('___*_*___'),
#     list('___*_*___')
# ] # 2 5  \  4 4 3 4 4

heart = []
left_arm, right_arm, body, left_leg, right_leg = 0, 0, 0, 0, 0

heart_flag = False
for i in range(n):
    for j in range(n):
        if board[i][j] == '*':
            heart = [i + 2, j + 1]
            heart_flag = True
            break

    if heart_flag:
        break

for i in range(heart[1] - 1):
    if board[heart[0] - 1][i] == '*':
        left_arm += 1

for i in range(heart[1], n):
    if board[heart[0] - 1][i] == '*':
        right_arm += 1

temp = 0
for i in range(heart[0], n):
    if board[i][heart[1] - 1] == '*':
        body += 1
        temp = i

for i in range(n - 1, temp, - 1):
    if board[i][heart[1] - 2] == '*':
        left_leg += 1

for i in range(n - 1, temp, -1):
    if board[i][heart[1]] == '*':
        right_leg += 1

print(*heart)
print(left_arm, right_arm, body, left_leg, right_leg)
