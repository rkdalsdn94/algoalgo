'''
단순한 수학 문제

반복문으로 풀면 안된다. (n의 범위가 최대 10억이라서 시간초과가 나온다.)
math.ceil((V-B) / (A-B)) 를 통해서 풀면 된다.
올림을 쓰는 이유는 소수점이 나왔을 때는 달팽이가 못 올라간 상황이라
다음날 올라가야 돼서 + 1 을 해주기 위해 올림을 썻다.
'''

from math import ceil

A, B, V = map(int, input().split())

# 테스트
# A, B, V = 2, 1, 5 # 4
# A, B, V = 5, 1, 6 # 2
# A, B, V = 100, 99, 1000000000 # 999999901

print(ceil((V-B) / (A-B)))
