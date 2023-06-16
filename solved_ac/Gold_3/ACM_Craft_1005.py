# 백준 - 골드3 - ACM Craft - 1005 - dp, 그래프, 위상 정렬 문제
'''
dp, 그래프, 위상 정렬 문제

PyPy3 로 제출하면 아래 코드가 통과하고,
Python3 로 제출하면 import sys; input=sys.stdin.readline 을 추가해야 된다.

백준 (줄 세우기 - 2252) 문제랑 위상 정렬을 구하는 부분은 같은데, 간단한 dp를 섞어야 된다.
dp 식을 따로 두는건 아니라 memoization 기법을 활용한다.

풀이 방식은 선수 지식을 확인하는 indegree 리스트를 만들어 놓고, 선수 지식이 필요한 부분에 1씩 더한다.
그 다음 진입 차수(indegree)가 0인 값을 q에 담고, 해당 건설 비용(construction_cost)의 값을 dp에 담는다.
다음으로 위상 정렬 함수를 실행 시켜 q의 값을 하나 씩 꺼내면서 꺼낸 값을 그래프의 인덱스로 사용해서 건설 비용을 계산하는데 이때 dp의 memoization이 필요하다.
현재 건설 비용의 값, 전의 건설 비용(dp[x]) + 현재 건설 비용(construction_cost) 값 중 더 큰 값으로 dp[i] 만든다.
현재 진입 차수의 값을 1씩 빼고, 진입 차수가 0이 되면 q에 담는다.
위 과정을 q가 빌 때까지 반복한 후 dp에서 알고싶은 도착지의 건설 비용의 값을 리턴하고 이걸 출력하는 방식으로 풀었다.

뭔가 코드가 돌아가는걸 보면 이해가 쉬운데, 글로 적으려고 하니까 더 이해가 안 되는 느낌이다.
아래 코드를 'https://pythontutor.com/visualize.html#mode=display' 여기 링크에서 한 step 씩 넘겨보면 바로 이해가 된다.

in
    2
    4 4
    10 1 100 10
    1 2
    1 3
    2 4
    3 4
    4
    8 8
    10 20 1 5 8 7 1 43
    1 2
    1 3
    2 4
    2 5
    3 6
    5 7
    6 7
    7 8
    7
out
    120
    39
'''

# import sys; input=sys.stdin.readline # Pyhon3 로 제출할 때 주석 해제
from collections import deque

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    g = [ [] for _ in range(n + 1) ]
    construction_cost = [0] + list(map(int, input().split()))
    indegree = [0] * (n + 1)
    dp = [0] * (n + 1)
    for _ in range(k): # 선수 지식을 위해 몇 번 진입하는지 확인하는 작업
        a, b = map(int, input().split())
        g[a].append(b)
        indegree[b] += 1
    end = int(input())
    # print(g, indegree)

    # 테스트
    # n, k = 4, 4
    # g = [[], [2, 3], [4], [4], []]
    # indegree = [0, 0, 1, 1, 2]
    # construction_cost = [0] + [10, 1, 100, 10]
    # dp = [0] * (n + 1)
    # end = 4 # 120

    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = construction_cost[i]
    
    def topology_sort():
        while q:
            x = q.popleft()

            for i in g[x]:
                indegree[i] -= 1
                dp[i] = max(dp[i], dp[x] + construction_cost[i])

                if indegree[i] == 0:
                    q.append(i)

        return dp[end]

    print(topology_sort())
