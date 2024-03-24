# 백준 - 골드5 - 무한 수열 - 1351 - dp, 자료 구조(해시를 사용한 집합과 맵) 문제
'''
dp 문제

문제에 주어진 다음의 식을 구하면 되는 문제이다.
 - 무한 수열 A는 다음과 같다.
    - A[0] = 1
    - A[i] = A⌊i/P⌋ + A⌊i/Q⌋ (i ≥ 1)
 - N, P와 Q가 주어질 때, A[N]을 구하는 프로그램을 작성하시오.

풀이 과정
 - 풀이는 단순하다. 단, 평소처럼 dp를 사용하면 메모리 초과가 발생한다. (dp = [0] * (n + 1)을 사용하면 메모리 초과, n의 범위가 0 ≤ N ≤ 10^12 이렇게 되므로)
 - 따라서, 빈 객체(해시 테이블)를 둔 뒤 재귀함수로 n의 범위를 줄여가며(n // p, n // q 이런 식으로 범위를 줄임) 계산하면 된다.
'''

import sys; sys.setrecursionlimit(10 ** 7)

n, p, q = map(int, input().split())

# 테스트
# n, p, q = 7, 2, 3 # 7
# n, p, q = 0, 2, 3 # 1
# n, p, q = 10000000, 3, 3 # 32768
# n, p, q = 256, 2, 4 # 89
# n, p, q = 1, 1000000, 1000000 # 2

hash_table = {}
hash_table[0] = 1

def dfs(n):
    if n not in hash_table:
        hash_table[n] = dfs(n // p) + dfs(n // q)
        return hash_table[n]
    return hash_table[n]

print(dfs(n))
