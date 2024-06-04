# 백준 - 골드3 - 별자리 만들기 - 4386 - 그래프, 최소 신장 트리, 크루스칼 알고리즘 문제
'''
그래프, 최소 신장 트리, 크루스칼 알고리즘 문제

기존에 풀었던 크루스칼 알고리즘과 똑같이 풀면 된다.
단, 가중치를 계산할 때, 루트를 씌워야 한다.

풀이 과정
 1. 입력을 받고, 별의 좌표를 저장한다.
 2. 별의 좌표를 이용하여 간선을 저장한다.
 3. 간선을 가중치를 기준으로 정렬한다.
 4. 부모를 찾는 find 함수와 부모를 설정하는 union 함수를 정의한다.
 5. 간선을 돌면서 find(a)와 find(b)가 다른 경우 union을 수행하고, res에 가중치를 더한다.
 6. res를 출력한다.
'''

n = int(input())
star = [list(map(float, input().split())) for _ in range(n)]

# 테스트
# n = 3
# stars = [[1.0, 1.0], [2.0, 2.0], [2.0, 4.0]] # 3.41

edges = []
for i in range(n):
    for j in range(i+1, n):
        a, b = stars[i], stars[j]
        edges.append([i, j, ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5])

edges.sort(key=lambda x: x[2])

parent = [i for i in range(n)]
res = 0

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

for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        res += c

print(round(res, 2))
