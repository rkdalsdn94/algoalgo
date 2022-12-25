# 백준 - 브론즈3 - 공 - 1547 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

단순 구현 문제이다.

풀이 과정
1. n을 입력 받은 후, n만큼 반복한다.
2. a, b를 입력받은 후 해당 위치가 res에 어디 있는지 찾은 후 위치를 바꾼다.
3. res의 0 번째를 출력한다.

in
    4
    3 1
    2 3
    3 1
    3 2
out
    3

in
    2
    1 2
    3 1
out
    2

in
    5
    2 3
    1 3
    2 3
    2 1
    3 1
out
    3

in
    9
    1 2
    3 2
    1 2
    2 1
    2 1
    3 2
    1 3
    3 1
    1 2
out
    1
'''

n = int(input())
res = [1, 2, 3]

for _ in range(n):
    a, b = map(int, input().split())

    x1, y1 = res.index(a), res.index(b)
    res[x1], res[y1] = res[y1], res[x1]

print(res[0])