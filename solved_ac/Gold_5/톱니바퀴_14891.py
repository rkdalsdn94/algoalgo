# 백준 - 골드5 - 톱니바퀴 - 14891 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

풀이 과정
 - 회전 시킬 후보 표시 (idx, 오른쪽, 왼쪽), 회전
    - 번호, 같은 방향인지(% 2로 구하면 될 듯, 0이면 같은 방향)
 - idx 회전 후보추가 = [idx, 0]
 - 오른쪽 방향처리 단, 극성이 같으면 break
    for i (idx + 1, n + 1)
      # 왼쪽 톱니의 3시(배열에서 + 2)위치, 오른쪽 톱니는 9시(+6)의 위치 (톱니의 숫자가 7이 넘어갈 수 있으므로 % 8같은 걸로 구하는 편이 좋음)
      if arr[i - 1][(top[i-1] + 2) % 8] != arr[i][(top[i] + 6) % 8]

      # 다르다면 후보에 추가해줘야 된다.
      else list.app([i, (i-idx) % 2])
 - 위와 같이 왼쪽도 처리해주면 된다.
 - 실제 회전 처리
    for i, rotation in list
        if rotation == 0 # 같은 방향
            top[i] = (top[i] - dr + 8) % 8
        else # 다른 방향
            top[i] = (top[i] + dr + 8) % 8

참고
 - https://www.youtube.com/watch?v=0VfhMu6s21w
'''

gear_list = [[0] * 8] + [list(input()) for _ in range(4)]
k = int(input())
k_list = [list(map(int, input().split())) for _ in range(k)]

# 테스트
# gear_list = [[0] * 8] + [list('10101111'), list('01111101'), list('11001110'), list('00000010')]
# k = 2
# k_list = [[3, -1], [1, 1]] # 7
# gear_list = [[0] * 8] + [list('11111111'), list('11111111'), list('11111111'), list('11111111')]
# k = 3
# k_list = [[1, 1], [2, 1], [3, 1]] # 15
# gear_list = [[0] * 8] + [list('10001011'), list('10000011'), list('01011011'), list('00111101')]
# k = 5
# k_list = [[1, 1], [2, 1], [3, 1], [4, 1], [1, -1]] # 6
# gear_list = [[0] * 8] + [list('10010011'), list('01010011'), list('11100011'), list('01010101')]
# k = 8
# k_list = [[1, 1], [2, 1], [3, 1], [4, 1], [1, -1], [2, -1], [3, -1], [4, -1]] # 5

top = [0] * 5 # 톱니바퀴가 4개만 들어온다. 입력된 숫자 그대로 사용하기 위해 1을 추가한 5를 곱함

for idx, direction in k_list:
    # idx 톱니를 회전
    temp_list = [[idx, 0]]

    # idx 우측방향 처리 (같은 극성이 나오면 탈출)
    for i in range(idx + 1, 5):
        # 왼쪽 3시 극성이 != 오른쪽 9시 극성과 다르다면 회전 후보(temp_list)의 추가
        if gear_list[i - 1][(top[i - 1] + 2) % 8] != gear_list[i][(top[i] + 6) % 8]:
            temp_list.append([i, (i - idx) % 2])
        else: # 같은 극성이라면 break
            break

    # idx 좌측 방향 처리 (같은 극성 나오면 탈출)
    for i in range(idx - 1, 0, -1):
        # 왼쪽 3시 극성이 != 오른쪽 9시 극성과 다르다면 회전 후보(temp_list)의 추가
        if gear_list[i][(top[i] + 2) % 8] != gear_list[i + 1][(top[i + 1] + 6) % 8]:
            temp_list.append([i, (idx - i) % 2])
        else: # 같은 극성이라면 break
            break

    # 실제 회전 처리
    for i, rotation in temp_list:
        if rotation == 0: # idx 톱니의 dr과 같은 방향
            top[i] = (top[i] - direction + 8) % 8
        else:
            top[i] = (top[i] + direction + 8) % 8

# 점수 계산
res = 0
tbl = [0, 1, 2, 4, 8]
for i in range(1, 5):
    res += int(gear_list[i][top[i]]) * tbl[i]

print(res)
