# 백준 - 만취한 상범 - 6359 - 브론즈2 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

수학적으로 풀 수 있을거 같은데, n의 범위가 얼마 되지 않아 완전 탐색하는 방법으로 문제를 풀었다.
n의 배수면 1, 0 바꿔가면서 마지막에 1이 몇 개 있는지 확인하는 방법으로 출력하면 된다.

in
    2
    5
    100
out
    2
    10
'''

t = int(input())

for _ in range(t):
    n = int(input())
    res = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            if res[j] == 1:
                res[j] = 0
            else:
                res[j] = 1

    print(res[1:].count(1))
