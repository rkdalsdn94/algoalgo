'''
뻔한 소수 찾기 알고리즘이다.
그 전에 프로그래머스에서 풀었던 방식(programmers/Lv2/Lv2_소수_찾기.py)으로 제출했는데 통과했다.
전에도 import math를 했지만, 0.5를 제곱하는 방식으로 루트를 씌울수 있다.
더 좋은 방식으로 하자
'''

import math

m, n = map(int, input().split())

# 테스트
# m, n = 3, 16 # 3 5 7 11 13

def isPrime(x):
    if x == 1:
        return False

    z = int(math.sqrt(x)) # 이 방법이 싫다면 int(i ** 0.5) + 1 이렇게 해도 된다 --> 제곱근(루트씌우기)까지만 확인하기
    
    for i in range(2, z + 1):
        if x % i == 0:
            return False
    return True

for i in range(m, n + 1):
    if isPrime(i):
        print(i)

