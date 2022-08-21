'''
그리디, 정렬 문제

문제에 주어진 그대로만 풀면 쉽게 풀 수 있다.
임의의 등수 리스트를 입력받고 정렬을 한 후에
1부터 시작하는 n의 점수 리스트와 절댓값을 res에 더해준 후
res를 출력하면 된다.

주의 : import sys; input = sys.stdin.readline
위 부분이 없으면 시간 초과가 나온다.
'''

import sys; input = sys.stdin.readline

n = int(input())
expected_score = sorted([ int(input()) for _ in range(n) ])

# 테스트
# n = 5
# expected_score = sorted([1,5,3,1,2]) # 3

original_score = [ i for i in range(1, n + 1) ]
res = 0

for i, j in zip(expected_score, original_score):
    res += abs(i - j)

print(res)
