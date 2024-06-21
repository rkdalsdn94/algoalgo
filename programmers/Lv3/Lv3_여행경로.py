# 프로그래머스 - Lv3 - 여행경로 - 그래프, dfs, bfs 문제
'''
그래프, dfs, bfs 문제

풀이 과정
    1. 입력을 받고, graph를 defaultdict로 설정한다.
    2. graph를 정렬한다.
    3. dfs 함수를 만들어서 경로를 찾는다.
         3.1. 경로를 찾는 방법은 graph를 통해 경로를 찾는다.
    4. 경로를 찾으면 answer에 추가한다.
    5. answer를 반환한다.
'''

from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)

    for a, b in tickets:
        graph[a].append(b)

    for a in graph:
        graph[a].sort(reverse=True)

    answer = []

    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        answer.append(a)

    dfs("ICN")

    return answer[::-1]

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets)) # ["ICN", "JFK", "HND", "IAD"]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(tickets)) # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
