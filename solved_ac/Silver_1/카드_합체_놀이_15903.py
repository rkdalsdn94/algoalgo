'''
그리디, 자료 구조, 우선순위 큐 문제


1. x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산한다. (x ≠ y)
2. 계산한 값을 x번 카드와 y번 카드 두 장 모두에 덮어 쓴다.

위의 순서로 문제를 푸는데, 문제 조건 중 '만들 수 있는 가장 작은 점수를 계산하는 프로그램을 만들어보자.'라는 조건이 있다.
위에 조건을 만족하려면, 가장 작은 수를 2개를 뽑은 후 더한 값이 최종으로 가장 작을거 같다.
그래서 heapq를 사용해서 가장 작은 수 2개씩 뽑은 후 m번 추가하는 형식으로 문제를 풀었다.
'''

import heapq as hq

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, m = 3, 1
# n_list = [3,2,6] # 16
# n, m = 4, 2
# n_list = [4,2,3,1] # 19

q = []

for i in n_list:
    hq.heappush(q, i)

for _ in range(m):
    temp_1 = hq.heappop(q)
    temp_2 = hq.heappop(q)

    temp_sum = temp_1 + temp_2
    hq.heappush(q, temp_sum)
    hq.heappush(q, temp_sum)

print(sum(q))
