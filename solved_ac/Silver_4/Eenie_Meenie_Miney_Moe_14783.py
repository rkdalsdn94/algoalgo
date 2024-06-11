# 백준 - 실버4 - Eenie Meenie Miney Moe - 14783 - 구현, 시뮬레이션, 자료 구조(큐) 문제
'''
구현, 시뮬레이션, 자료 구조(큐) 문제

큐(deque)를 이용해서 풀 수 있는 문제이다.
문제를 다 풀고 다른 사람의 코드를 확인해보니 큐를 돌리는 부분을 rotate 함수를 사용하는 것이 더 좋아보였다.

풀이 과정
    1. 입력을 받고, 입력받은 n의 크기만큼 1부터 n + 1 크기의 큐를 만든다.
    2. 큐를 돌면서 l_list[0] - 1만큼 큐를 돌리고, 큐에서 pop한다.
        2.1. 아래 코드는 직접 popleft()와 append() 함수를 사용해서 큐를 돌렸다.
             (rotate 함수를 사용하면 더 좋을 것 같다.)
        2.2. 큐를 돌린 후, l_list를 돌려야 된다. (따라서 l_list를 deque로 만들었다.)
    3. 위 과정을 큐의 길이가 1이 될 때까지 반복하고, 남은 q를 출력하면 된다.
'''

from collections import deque

n, l = map(int, input().split())
l_list = deque(map(int, input().split()))

# 테스트
# n, l = 8, 2
# l_list = deque([5, 3]) # 7

q = deque(range(1, n + 1))

while len(q) > 1:
    for i in range(l_list[0] - 1):
        q.append(q.popleft())
    q.popleft()
    l_list.append(l_list.popleft())

print(q[0])
