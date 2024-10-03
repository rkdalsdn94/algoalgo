# 백준 - 실버2 - 골드바흐 파티션 - 17103 - 수학, 정수론, 소수 판정, 에라토스테네스의 체 문제
'''
수학, 정수론, 소수 판정, 에라토스테네스의 체 문제

에라토스테네스의 체를 이용하여 소수를 판정하고, 골드바흐 파티션을 구하는 문제이다.

풀이 과정
    1. t를 입력받는다.
    2. n_list를 입력받는다.
    3. n_list의 최댓값을 구한다.
    4. 에라토스테네스의 체를 이용하여 소수를 판정한다.
    5. n_list를 순회하며 골드바흐 파티션을 구한다.
    6. 골드바흐 파티션을 출력한다.
'''

import sys
input = sys.stdin.readline

def goldbach_partition(n):
    prime = [True] * (n + 1)
    prime[0], prime[1] = False, False

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    return prime

t = int(input())
n_list = [int(input()) for _ in range(t)]
max_n = max(n_list)
prime = goldbach_partition(max_n)

for n in n_list:
    cnt = 0

    for i in range(2, n // 2 + 1):
        if prime[i] and prime[n - i]:
            cnt += 1

    print(cnt)
