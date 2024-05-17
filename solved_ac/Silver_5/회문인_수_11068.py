# 백준 - 실버5 - 회문인 수 - 11068 - 구현, 문자열, 완전 탐색 문제
'''
구현, 문자열, 완전 탐색 문제

2부터 64까지의 진법으로 변환했을 때, 회문인 수가 있는지 확인하는 문제이다.
진법 변환만 할 수 있으면 쉽게 풀 수 있다.

풀이 과정
 1. 입력을 받고, 2부터 64까지 반복문을 돌면서 회문인 수가 있는지 확인한다.
 2. 회문인 수가 있으면 1을 출력하고, 없으면 0을 출력한다.

in
    3
    747
    255
    946734
out
    1
    1
    0
'''

t = int(input())
for _ in range(t):
    n = int(input())

    for i in range(2, 65):
        temp = n
        res = []

        while temp > 0:
            res.append(temp % i)
            temp //= i

        if res == res[::-1]:
            print(1)
            break
    else:
        print(0)
