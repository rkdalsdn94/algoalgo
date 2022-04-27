'''
구현, 그리디 문제

손으로 직접 구해보면 좀 더 쉽게 나온다. 근데, 처음에 어떻게 그래야 될지 모르겠다면
옆의 링크를 참고해보자. (https://velog.io/@dding_ji/baekjoon-1783)
'''

# n, m = map(int, input().split())

# 테스트
n, m = 100, 50 # 48
n, m = 1, 1 # 1
n, m = 17, 5 # 4
n, m = 2, 4 # 2
n, m = 20, 4 # 4

if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m + 1) // 2))
elif m <= 6:
    print(min(4, m))
else:
    print(m - 2)
