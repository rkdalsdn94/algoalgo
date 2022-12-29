# 백준 - 실버3 - 크리스마스 선물 -14235 - 자료 구조(heap), 우선순위 큐 문큐
'''
자료 구조(heap), 우선순위 큐 문제

heap을 활용하여 우선순위 큐를 구하면 되는 문제이다.
대신, 파이썬에서 heap은 min heap으로 동작하므로 -를 붙여 max로 바꾸는 과정이 필요하다.

풀이 과정
1. n을 입력받은 후, 출력할 때 사용할 res 리스트를 초기화 한다.
2. n만큼 반복하면서 a를 리스트 형식으로 입력 받고, 입력받은 a의 0번째 인덱스의 값이 0인지 검사한다.
    2.1. 0이면 res가 있는지 체크한 후, heapq에서 pop을 하면서 출력한다. (대신 -붙인 다음 pop 하면서 출력해야 된다.)
    2.2. 0이 아니면 heapq에 a[0]을 제외한 나머지를 push를 한다. (대신, max heap으로 사용하기 위해 push 할 때 -를 붙여야 한다.)

in
    5
    0
    2 3 2
    0
    0
    0
out
    -1
    3
    2
    -1
'''

import heapq as hq

n = int(input())
res = []

for _ in range(n):
    a = list(map(int, input().split()))

    if a[0] == 0:
        if res:
            print(-hq.heappop(res))
        else:
            print(-1)
    else:
        for i in range(1, a[0] + 1):
            hq.heappush(res, -a[i])
