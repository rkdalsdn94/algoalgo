# 백준 - 실버5 - 인기 투표 - 11637 - 구현 문제
'''
구현 문제

풀이 과정
1. 입력을 받고, 각 후보자의 득표 수를 확인한다.
2. 득표 수가 가장 많은 후보자가 2명 이상이면 no winner를 출력한다.
3. 득표 수가 가장 많은 후보자가 1명이면 득표 수가 전체 득표 수의 절반보다 크면 majority winner를 출력하고, 작으면 minority winner를 출력한다.

in
    4
    3
    10
    21
    10
    3
    20
    10
    10
    3
    10
    10
    10
    4
    15
    15
    15
    45
out
    majority winner 2
    minority winner 1
    no winner
    minority winner 4
'''

t = int(input())
for _ in range(t):
    n = int(input())
    n_list = [int(input()) for _ in range(n)]
    max_num = max(n_list)

    if n_list.count(max_num) >= 2:
        print('no winner')

    if n_list.count(max_num) == 1:
        if max_num > sum(n_list) // 2:
            print('majority winner', n_list.index(max_num) + 1)
        else:
            print('minority winner', n_list.index(max_num) + 1)
