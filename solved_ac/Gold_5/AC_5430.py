'''
구현 난이도가 문제 난이도의 비해 어렵진 않았다.
큐 자료구조를 어느정도 이해하고 있고, 문자열 조작을 할 수 있으면
차례대로 풀면 그대로 작성된다.

1. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

2. 함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다.
3. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

문제의 시간제한이 1초에다, n(p_list의 원소)의 개수가 100,000이라서 deque을 사용했다.
'''

from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    p_list = deque(input()[1:-1].split(','))
    # print(p, n, p_list)
    res = ''
    r_cnt, flag = 0, True

    if n == 0:
        p_list = []

    for i in p:
        if i == 'R':
            r_cnt += 1
        elif i == 'D':
            if p_list:
                if r_cnt % 2 != 0: p_list.pop()
                else: p_list.popleft()
            else:
                res = 'error'
                flag = False
                break


    if flag:
        if r_cnt % 2 == 0:
            res += '[' + ','.join(p_list) + ']'
        else:
            p_list.reverse()
            res += '[' + ','.join(p_list) + ']'
        print(res)
    else:
        print(res)
