# 백준 - 골드5 - 빗물 - 14719 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

풀이 과정
    1. 입력을 받는다.
    2. blocks의 최대값을 찾는다.
    3. res를 0으로 초기화한다.
    4. 1부터 w - 1까지 반복한다.
        4.1. i번째 블록을 기준으로 왼쪽, 오른쪽 블록 중 최댓값을 찾는다.
        4.2. 빗물의 높이를 구한다.
            4.2.1. 빗물의 높이는 왼쪽, 오른쪽 블록 중 작은 값에서 i번째 블록을 뺀 값이다.
        4.3. 빗물의 높이가 0보다 크면 res에 더한다.
    5. res를 출력한다.
'''

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

# 테스트
# h, w = 4, 4
# blocks = [3, 0, 1, 4] # 5
# h, w = 4, 8
# blocks = [3, 1, 2, 3, 4, 1, 1, 2] # 5
# h, w = 3, 5
# blocks = [0, 0, 0, 2, 0] # 0

res = 0

for i in range(1, w - 1):
    left = max(blocks[:i])
    right = max(blocks[i + 1:])
    rain = min(left, right) - blocks[i]

    if rain > 0:
        res += rain

print(res)
