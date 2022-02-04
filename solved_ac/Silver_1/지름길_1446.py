'''
문제 상에서는 지름길의 시작 위치는 도착 위치보다 작다고 되어 있는데, 여기에 함정이 있는거 같다.
지름길에 시작 위치가 지름길의 도착 위치보단 작다.
다시 말해 지름길의 시작 위치가 최종 도착 위치보다 작을지 클지는 모른다.
g의 범위(d + 1)를 만들고 append할 때 시작 위치가 d보다 작거나 같을때만 추가하도록 수정하니까 잘 통과 됐다.

in
    5 150
    0 50 10
    0 50 20
    50 100 10
    100 151 10
    110 140 90
out
    70
'''

n, d = map(int, input().split())
g = [ [] for _ in range(d + 1) ]
distance = [ i for i in range(d + 1) ]

for _ in range(n):
    a, b, c = map(int, input().split())

    if a <= d:
        g[a].append((b, c))


# print(g, n, d, distance)

for i in range(d + 1):
    if i > 0: distance[i] = min(distance[i], distance[i-1] + 1)

    for x, y in g[i]:
        if x <= d and distance[i] + y < distance[x]:
            distance[x] = distance[i] + y
    
print(distance[d])

