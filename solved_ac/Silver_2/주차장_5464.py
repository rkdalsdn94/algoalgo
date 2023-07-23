# 백준 - 실버2 - 주차장 - 5464 - 구현, 자료 구조, 시뮬레이션, 우선순위 큐, 큐 문제
'''
구현, 자료 구조, 시뮬레이션, 우선순위 큐, 큐 문제

우선순위 큐로 문제를 풀어보려고 했는데, deqeue 를 쓰는게 더 편해서 deque으로 해결했다.
 - 우선순위 큐로 풀었어도 비슷하게 풀었을거 같다.

input 값들을 잘 입력 받은 후 car_in_out_list 의 값이 음수일 때랑 양수일 때 다르게 판단한다.
양수 일때는 in_q에 값을 담아야 되는데, 0이 in_q 에 있을 때 즉, 주차할 수 있을 때만 in_q 해당 위치에 car 정보를 입력해놓는다.
    - 0이 없을 경우엔 temp_q를 deque 으로 만들어 놓은 후(popleft 를 사용하기 위해) 여기에 임시로 append 시켜 놓는다.
음수가 들어오면 in_q에 해당 차량 위치를 찾아 index 라는 변수에 담아 놓은 후 해당 위치를 0으로 초기화하고, 주차 금액을 계산한다. (m_list[-i - 1] * n_list[index])
    - 그리고, temp_q 에 값이 있을 경우 제일 왼쪽 값을 꺼내 in_q에 담아준다.
이 과정을 car_in_out_list 의 값을을 다 반복하면 된다.
'''

import sys; input=sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
n_list = [int(input()) for _ in range(n)]
m_list = [int(input()) for _ in range(m)]
car_in_out_list = [int(input()) for _ in range(m * 2)]

# 테스트
# from collections import deque
# n, m = 3, 4
# n_list = [ 2, 3, 5 ]
# m_list = [200, 100, 300, 800]
# car_in_out_list = [3, 2, -3, 1, 4, -4, -2, -1] # 5300

res = 0
in_q, temp_q = [0] * n, deque()

for i in car_in_out_list:
    if i > 0:
        if 0 in in_q:
            for j in range(n):
                if in_q[j] == 0:
                    in_q[j] = i
                    break
        else:
            temp_q.append(i)
    else:
        index = in_q.index(-i)
        in_q[index] = 0
        res += m_list[-i - 1] * n_list[index]
        if temp_q:
            in_q[index] = temp_q.popleft()

print(res)
