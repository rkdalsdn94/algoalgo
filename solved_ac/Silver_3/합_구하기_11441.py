# 백준 - 실버3 - 합 구하기 - 11441 - 누적 합 문제
'''
누적 합 문제

누적 합을 미리 구해놓고, 나중에 구해야 할 누적 합의 마지막 위치에서 시작 위치를 빼면 된다.

입력으로 들어온 값을 인덱스 그대로 사용하기 위해 n_list와 prefix_sum 배열을 n 보다 1씩 크게 잡아놓은 생태다.
따라서, 출력할 때 시작 위치를 1 더 빼야 된다. (prefix_sum[마지막_위치] - prefix_sum[시작_위치 - 1]) -> 1을 더 크게 잡음
'''

import sys; input = sys.stdin.readline

n = int(input())
n_list = [0] + list(map(int, input().split()))
m = int(input())
m_list = [list(map(int, input().split())) for _ in range(m)]

# 테스트
# n = 5
# n_list = [0] + [10, 20, 30, 40, 50]
# m = 5
# m_list = [[1, 3], [2, 4], [3, 5], [1, 5], [4, 4]] # 60  \  90  \  120  \  150  \  40
# n = 3
# n_list = [0] + [1, 0, -1]
# m = 6
# m_list = [[1, 1], [2, 2], [3, 3], [1, 2], [2, 3], [1, 3]] # 1  \  0  \  -1  \  1  \  -1  0

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1): # 누적 합 구하는 로직
    prefix_sum[i] = prefix_sum[i - 1] + n_list[i]

for i, j in m_list: # 구해놓은 누적 합의 (마지막 위치 - 시작 위치)를 출력하면 된다.
    print(prefix_sum[j] - prefix_sum[i - 1])
