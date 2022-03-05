'''
파이썬 내장함수로만 활요한 방법이다
예전 gcd문제를 풀 때 함수로 gcd를 구하는 법(b != 0 아닐 때, gcd(b, a % b) 이런 식으로)을 사용한 적 있어서
이번에는 내장함수 모듈을 다 사용해 보았디.
combinations 를 사용하지 않으려면 아래와 같이 하면 된다

for i in range(1, len(n_list - 1)):
    for j in range(i + 1, len(n_list)): 
        ~~~~~

in 입력
    3
    4 10 20 30 40
    3 7 5 12
    3 125 15 25
out 출력
    70
    3
    35
'''

from itertools import combinations
import math

t = int(input())

for _ in range(t):
    n_list = list(map(int, input().split()))
    n = n_list.pop(0)
    res = 0

    for i in combinations(n_list, 2):
        a, b = i
        res += math.gcd(a, b)

    print(res)
