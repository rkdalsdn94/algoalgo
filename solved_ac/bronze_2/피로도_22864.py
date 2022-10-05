# 백준 - 피로도 - 22864 - 브론즈2 - 구현, 그리디, 시뮬레이션 문제
'''
구현, 그리디, 시뮬레이션 문제

temp + a의 피로도가 번아웃이 넘는지만 계산하면서 풀면 된다.
'''

a, b, c, m = map(int, input().split())

# 테스트
# a, b, c, m = 5, 3, 2, 10 # 24
# a, b, c, m = 10, 5, 1, 10 # 15
# a, b, c, m = 11, 5, 1, 10 # 0

res, day, temp = 0, 0, 0

if a > m:
    print(0)
else:
    while day != 24:
        day += 1

        if temp + a <= m:
            res += b
            temp += a
        else:
            if temp - c >= 0:
                temp -= c
            else:
                temp = 0
    print(res)
