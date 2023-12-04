# 백준 - 브론즈2 - 수학은 비대면강의입니다 - 19532 - 수학, 완전 탐색 문제
'''
수학, 완전 탐색 문제

    ax + by = c
    dx + dy = f
위 두 식을 완전 탐색으로 구하는 간단한 문제이다.

수식으로 풀고 싶다면 다음과 같이 하면 된다.
    x = (c * e - b * f) // (a * e - b * d)
    y = (a * f - d * c) // (a * e - b * d)
'''

a, b, c, d, e, f = map(int, input().split())

# 테스트
# a, b, c, d, e, f = 1, 3, -1, 4, 1, 7 # 2 -1
# a, b, c, d, e, f = 2, 5, 8, 3, -4, -11 # -1 2

x, y = 0, 0
flag = False

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a * i) + (b * j) == c and (d * i) + (e * j) == f:
            x, y = i, j
            flag = True
            break
    if flag:
        break

print(x, y)
