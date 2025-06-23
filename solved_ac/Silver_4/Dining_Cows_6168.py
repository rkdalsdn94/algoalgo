# 백준 - 실버4 - Dining Cows - 6186 - 완전 탐색, 누적 합 문제
"""
완전 탐색, 누적 합 문제

[핵심 아이디어]
    1. 어떤 분할점 k를 기준으로 앞의 k개는 모두 1그룹, 뒤의 (n-k)개는 모두 2그룹으로 만든다.
    2. 각 분할점에서 필요한 변경 횟수 = 앞쪽의 2개수 + 뒤쪽의 1개수
    3. 모든 가능한 분할점(0~n)에 대해 변경 횟수를 계산하고 최소값을 구한다.

[풀이 과정]
    1. 각 위치에서 왼쪽 구간의 2의 개수와 오른쪽 구간의 1의 개수를 효율적으로 계산하기 위해 prefix sum 활용
    2. 분할점 k에 대해: left_twos[k] + right_ones[k] 계산
    3. 모든 분할점 중 최소값 반환
"""

n = int(input())
cows = [int(input()) for _ in range(n)]

# 테스트
# n = 7
# cows = [2, 1, 1, 1, 2, 2, 1] # 2

# 각 위치에서 왼쪽에 있는 2의 개수 계산
left_twos = [0] * (n + 1)
for i in range(n):
    left_twos[i + 1] = left_twos[i] + (1 if cows[i] == 2 else 0)

# 각 위치에서 오른쪽에 있는 1의 개수 계산
right_ones = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    right_ones[i] = right_ones[i + 1] + (1 if cows[i] == 1 else 0)

# 모든 분할점에 대해 최소 변경 횟수 계산
res = float('inf')
for k in range(n + 1):
    # k개를 1그룹으로, 나머지를 2그룹으로 만들 때의 변경 횟수
    changes = left_twos[k] + right_ones[k]
    res = min(res, changes)

print(res)
