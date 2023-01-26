# 백준 - 실버3 - 모든 순열 - 10974 - 완전 탐색, 백 트래킹 문제
'''
완전 탐색, 백 트래킹 문제

n의 범위가 최대 8이라서 python 내장 함수인 permutations 으로 풀었다.

나중에 직접 permutations 을 구해봐도 재밌을거 같다.
'''

from itertools import permutations

n = int(input())

# 테스트
# n = 3

n_list = [i for i in range(1, n + 1)]
res = sorted(list(permutations(n_list, n)))

for i in res:
    print(*i)
