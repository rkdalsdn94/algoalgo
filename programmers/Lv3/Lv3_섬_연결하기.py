# 프로그래머스 - Lv3 - 섬 연결하기 - 크루스칼 알고리즘, 최소 신장 트리 문제
'''
크루스칼 알고리즘, 최소 신장 트리 문제

전형적인 크루스칼 알고리즘을 사용하여 최소 신장 트리를 찾는 문제이다.

백준 '골드4 - 네트워크 연결'과 똑같이 풀었다.
최소 신장 트리와 크루스칼 알고리즘을 알면 쉽게 풀 수 있다.

풀이 과정
 1. find 함수를 정의한다. 만약 부모가 자기 자신이 아니라면 부모를 찾는다.
 2. union 함수를 정의한다. x, y를 find 함수를 통해 찾고, x가 y보다 작으면 y의 부모를 x로 설정하고, 그렇지 않으면 x의 부모를 y로 설정한다.
 3. costs를 가중치를 기준으로 정렬한다.
 4. parent를 초기화하고, res를 0으로 초기화한다.
 5. costs를 돌면서 find(a)와 find(b)가 다른 경우 union을 수행하고, res에 가중치를 더한다.
 6. res를 반환한다.
'''

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):
    x, y = find(x), find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def solution(n, costs):
    global parent

    res = 0
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]

    for a, b, c in costs:
        if find(a) != find(b):
            union(a, b)
            res += c

    return res

print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])) # 4
