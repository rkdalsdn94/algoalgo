# 백준 - 실버3 - 카드 놓기 - 18115 - 자료 구조(덱) 문제
'''
자료 구조(덱) 문제

파이썬 collections 에 있는 deque 을 사용해서 풀었다. (appendleft 사용하기 위해)
단순히 덱을 구현하면 되는 문제이다.

문제를 잘 파악해야 된다. 아래 부분을 제대로 확인하지 못해 몇 번 틀렸다.
    - 기술을 N번 사용하여 카드를 다 내려놓았을 때, 놓여 있는 카드들을 확인했더니 위에서부터 순서대로 1, 2, …, N이 적혀 있었다!'
위를 구현하기 위해선 입력으로 들어온 a_list를 역순으로 만들어야 된다. (이 부분 때문에 틀림)

a_list reverse 시킨 후 해당 값이 1이면 appendleft(제일 앞), 2이면 insert(1 번째 인덱스 뒤), 3이면 append (제일 뒤) 구현하면 된다.
'''

from collections import deque

n = int(input())
a_list = list(map(int, input().split()))

# 테스트
# n = 5
# n_list = [1, 1, 1, 1, 1] # 5 4 3 2 1
# n = 5
# n_list = [2, 3, 3, 2, 1] # 1 5 2 3 4

res = deque()
a_list.reverse()

for i in range(n):
    if a_list[i] == 1:
        res.appendleft(i + 1)
    elif a_list[i] == 2:
        res.insert(1, i + 1)
    elif a_list[i] == 3:
        res.append(i + 1)

print(*res)
