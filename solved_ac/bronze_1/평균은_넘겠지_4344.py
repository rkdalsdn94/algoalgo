# 백준 - 브론즈1 - 평균은 넘겠지 - 4344 - 단순 구현, 수학 문제
'''
단순 구현, 수학 문제

평균을 구할 수 있는 방법만 알면 되는 문제이다.
처음에 n_list 중에서 average 와 크거나 같다로 생각했는데 그게 아니라 average 보다 커야 된다.
문제가 간단해서 따로 설명은 안적으려고 한다.

in
    5
    5 50 50 70 80 100
    7 100 95 90 80 70 60 50
    3 70 90 80
    3 70 90 81
    9 100 99 98 97 96 95 94 93 91
out
    40.000%
    57.143%
    33.333%
    66.667%
    55.556%
'''

t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    n, n_list = a[0], a[1:]

    average = sum(n_list) / n
    temp = 0
    for i in n_list:
        if i > average:
            temp += 1

    print('{:.3f}'.format(temp / n * 100) + '%')
