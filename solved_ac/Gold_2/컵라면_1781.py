# 백준 - 골드2 - 컵라면 - 1781 - 자료 구조(우선순위 큐), 그리디 문제
'''
자료 구조(우선순위 큐), 그리디 문제

PyPy3로 제출하거나, import sys; input=sys.stdin.readline 처리를 해야 된다.

처음에는 주어진 예제를 보고 문제를 정확히 파악하지 않고 제일 밑에 코드 처럼 작성했다가 틀렸다.
접근을 제대로 못 한 것이여서 우선순위 큐(heap)을 사용해서 다시 풀었다.
즉 정렬 기준이 아닌 컵라면을 얼마나 더 많이 받을 수 있는지가 기준이 된다.

참고
 - 파이썬에선 우선순위 큐인 PriorityQueue를 지원하는데, 어차피 내부적으로 heap 모듈을 사용한다.
 - 따라서 heap으로 구현했다.

풀이 과정
 - 입력 데이터를 잘 입력받고, 데드라인과 컵라면 수의 정보를 담은 리스트(n_list)를 정렬한다.
 - 우선순위 큐로 사용할 res를 빈 리스트를 생성하고, n_list의 값들을 꺼내 for 문을 실행한다.
 - for 문 내에서 heap에 받을 수 있는 컵라면을 넣어준다. (heappush 함수를 통해)
     - 이때 데드라인의 크기가 res의 길이보다 작다면 heappop을 통해 제일 작은 값을 꺼내준다.
 - 위 과정을 반복한 후 res의 총 합을 출력하면 된다.
'''

import heapq

n = int(input())
n_list = sorted([list(map(int, input().split())) for _ in range(n)])

# 테스트
# n = 7
# n_list = [[1, 6], [1, 7], [2, 4], [2, 5], [3, 1], [3, 2], [6, 1]] # 15
# n = 3
# n_list = [[1, 1], [2, 50], [2, 100]] # 150

res = []

for i, j in n_list:
    heapq.heappush(res, j)

    if i < len(res):
        heapq.heappop(res)

print(sum(res))


'''
처음 틀린 코드, 이 코드의 반례는 다음과 같다.
in
    3
    1 1
    2 50
    2 100
out
    150

아래의 코드 풀이는 정렬 순으로 차례대로 진행한다.
하지만, 값이 제일 크게 나오려면 [2, 50]과 [2, 100] 이 두 개를 처리해야 된다.
즉, 정렬 순이 아니라 다른 방식으로 풀어야 된다. (이때 우선순위 큐를 사용해야 됨, Python에선 heap 사용)


n = int(input())
n_list = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[0], -x[1]))

res = []
temp = -1

for i, j in n_list:
    if i <= n and temp != i:
        res.append(j)
        temp = i

print(sum(res))
'''
