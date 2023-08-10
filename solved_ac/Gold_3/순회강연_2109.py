# 백준 - 골드3 - 순회강연 - 2109 - 자료 구조(우선순위 큐), 그리디, 정렬 문제
'''
자료 구조(우선순위 큐), 그리디, 정렬 문제

전형적인 우선순위 큐 문제이다. 단, 입력으로 들어오는 n_list에서 두 번째 값을 기준으로 오름차순 정렬을 해야 된다.
두 번째 수가 같을 경우 더 큰 값을 append 해야 된다. 이 때문에 heapq 를 이용했다.
문제 상에 있는 예제만 봐도 n이 4일 때
p가 50, 10, 20, 30 d가 2, 1, 2, 1 이면 마지막에 하루 걸리는 30의 강연료를 선택해야 되고, 2일이 걸리는 50의 강연료를 선택해야 된다.

즉, 모든 강연료와 걸리는 날짜를 list에 담은 후 날짜를 기준으로 정렬한 다음
d가 같을 때 p가 더 큰 값을 고르면 되는데, 이를 힙으로 구하면 간단히 구할 수 있다. (python에선 min-heap 으로 구성되어 있어 단순히 pop만 하면 된다.)
'''

from heapq import heappush as hqpush, heappop as hqpop

n = int(input())
n_list = sorted([ list(map(int, input().split())) for _ in range(n) ], key=lambda x: (x[1]))

# 테스트
# n = 7
# n_list = sorted([
#     [20, 1],
#     [2, 1],
#     [10, 3],
#     [100, 2],
#     [8, 2],
#     [5, 20],
#     [50, 10]
# ], key=lambda x: (x[1])) # 185

res = []
for i in n_list:
    hqpush(res, i[0])

    if len(res) > i[1]: # d가 같아질 때 더 큰 값을 구하기 위해 힙에서 원소를 꺼낸다.
        hqpop(res)

print(sum(res))

