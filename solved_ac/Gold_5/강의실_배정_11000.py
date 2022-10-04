# 백준 - 강의실 배정 - 골드5 - 11000 - 자료 구조(힙), 그리디, 정렬, 우선순위 큐 문제
'''
자료 구조(힙), 그리디, 정렬, 우선순위 큐 문제

input = sys.stdin.readline 이게 없으면 시간 초과가 나온다.

수업들의 시작 시간이 다른 수업들의 종료 시간보다 크면 강의실을 추가해야 된다.

풀이 과정
1. 입력받은 n_list를 첫 번째 인덱스(s) 순으로 정렬한다. -> 수업의 시작 시간을 기준으로 정렬을 먼저 진행한다.
2. heap으로 활용하기 위한 res 리스트를 만들고, 가장 처음 시작하는 수업의 종료 시간(t)를 넣어준다.
3. 1부터 n까지 반복문을 돌면서 res에 가장 처음에 있는 시간의 종료 시간(t)이 현재 반복하고 있는 시간보다 크면 해당 수업의 종료 시간을 넣어준다.
    3.1 현재 반복하고 수업의 시작 시간이 res에 있는 종료 시간보다 크지 않다면 heap을 이용해서 res를 pop하고, 현재 수업시간의 종료 시간을 넣어준다.

heap을 사용하지 않고 list로 풀면 매번 정렬을 한 후에 비교해야 돼서 시간 초과가 나온다.
'''

import sys; input = sys.stdin.readline
import heapq as hq

n = int(input())
n_list = sorted([ list(map(int, input().split())) for _ in range(n) ])

# 테스트
# n = 3
# n_list = sorted([[1, 3], [2, 4], [3, 5]]) # 2

res = []
hq.heappush(res, n_list[0][1])

for i in range(1, n):
    if res[0] > n_list[i][0]:
        hq.heappush(res, n_list[i][1])
    else:
        hq.heappop(res)
        hq.heappush(res, n_list[i][1])

print(len(res))
