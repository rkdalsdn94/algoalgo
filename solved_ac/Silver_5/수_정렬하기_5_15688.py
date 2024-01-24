# 백준 - 실버5 - 수 정렬하기 5 - 15688 - 단순 정렬 문제
'''
단순 정렬 문제

단순 정렬 후 출력하면 된다.
단, 입력을 받을 때 sys에 있는 값들을 이용해서 풀어야 된다. (문제에 시간 누적이라고 적혀있음)
'''

import sys; input=sys.stdin.readline

n = int(input())
n_list = [int(input()) for _ in range(n)]

# 테스트
# n = 5
# n_list = [5, 4, 3, 2, 1] # 1  \  2  \  3  \  4  \  5
# n = 5
# n_list = [1, 2, 1, 2, 1] # 1  \  1  \  1  \  2  \  2
# n = 5
# n_list = [1, 2, 3, 4, 5] # 1  \  2  \  3  \  4  \  5
# n = 6
# n_list = [0, 0, 0, 0, 0, 0] # 0  \  0  \  0  \  0  \  0  \  0

for i in sorted(n_list):
    print(i)
