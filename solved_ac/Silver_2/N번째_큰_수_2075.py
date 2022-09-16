# 백준 - N번째 큰 수 - 2075 - 실버2 - 자료 구조, 우선순위 큐 
'''
자료 구조, 우선순위 큐 문제

우선순위 큐 문제이긴 하지만 heapq를 사용했다.
이유는 일반적으로 시간복잡도가 heap이 더 작기 때문에 heapq로 사용했다.
heapq에서 push()와 pop()은 O(logN)의 시간복잡도를 가진다.

heapq 저장과 정답 출력을 위한 res 변수를 list로 하나 만든다.
n번 반복하면서 list를 입력 받고, res의 길이가 n보다 작았을 때 heapq를 이용하여 res에 push한다.

길이가 n보다 크거나 같다면 res에 가장 작은 수와 입력 받은(n_list) 수와 비교한 후 res에 있는 수가 작으면
해당 수를 빼고, 값이 큰 수를 heap에다 넣어준다.

n번 반복 후 첫 번째 수를 출력하면 된다.

이 문제를 list로 푸는 방식은 똑같은데 시간 초과가 나온다. 그래서, 자료 구조를 잘 활용해야 된다.

in
    5
    12 7 9 15 5
    13 8 11 19 6
    21 10 26 31 16
    48 14 28 35 25
    52 20 32 41 49
out
    35
'''

import heapq as hq

n = int(input())
res = []

for _ in range(n):
    n_list = list(map(int, input().split()))

    if len(res) < n:
        for i in n_list:
            hq.heappush(res, i)
    else:
        for i in sorted(n_list):
            if res[0] < i:
                hq.heappush(res, i)
                hq.heappop(res)

print(res[0])
