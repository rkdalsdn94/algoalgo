# 백준 - 골드3 - 웜홀 - 1865 - 그래프, 최단 경로, 벨만 포드 문제
'''
그래프, 최단 경로, 벨만 포드 문제

밸만 포드 알고리즘으로 쉽게 풀 수 있다.
만약 밸만 포드 알고리즘을 모른다면 아래 링크를 통해 공부하면 된다.
 - https://www.youtube.com/watch?v=Ppimbaxm8d8

이 문제에서 주의할 점으론 도로는 양방향이고, 웜홀은 단방향으로 edge를 추가해줘야 한다.

풀이 과정
1. 벨만 포드 알고리즘을 이용하여 음수 사이클이 존재하는지 확인
2. 음수 사이클이 존재하면 YES, 존재하지 않으면 NO 출력
'''

INF = int(1e9)

def bf(start):
    dist[start] = 0

    for i in range(n):
        for j in edges:
            cur, next_node, cost = j

            if dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost

                if i == n - 1:
                    return True
    return False

t = int(input())
for _ in range(t):
    n, m, w = map(int, input().split())
    m_list = [list(map(int, input().split())) for _ in range(m)]
    w_list = [list(map(int, input().split())) for _ in range(w)]

    edges = []
    dist = [INF] * (n + 1)
    for s, e, t in m_list:
        edges.append([s, e, t])
        edges.append([e, s, t])

    for s, e, t in w_list:
        edges.append([s, e, -t])

    negative_cycle = bf(1)

    if negative_cycle:
        print("YES")
    else:
        print("NO")
