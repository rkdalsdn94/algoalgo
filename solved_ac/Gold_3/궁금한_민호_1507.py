'''
처음 문제를 접하고 너무 어려웠다. 그래서 플로이드 와샬의 개념을 다시 잡으려고
나동빈님의 블로그를 참고했다.(https://blog.naver.com/ndb796/221234427842)
그래서 한 번에 이동할 수 있는 간선이 없을 때(거쳐가는 노드가 있을 경우) 출발 노드와 도착 노드를 false로 만들고,
간선을 정리한 후(ck) 최종 노드들의 합을 구했다.(ck의 1이 되어 있는 부분)

-1을 리턴하는 경우는 문제 입력 조건에서 최단 거리로 입력된다고 하는데 최단 거리가 아닐 경우 -1을 리턴했다.
'''

# n = int(input())
# n_list = [ list(map(int, input().split())) for _ in range(n) ]
# print(n_list)

# 테스트
n = 5
n_list = [ [0, 6, 15, 2, 6], [6, 0, 9, 8, 12], [15, 9, 0, 16, 18], [2, 8, 16, 0, 4], [6, 12, 18, 4, 0] ] # 55
# n = 3
# n_list = [ [0, 2, 2], [2, 0, 2], [2, 2, 0] ] # 6
# n = 8
# n_list = [ [0, 1, 6, 17, 26, 13, 7, 16], [1, 0, 5, 16, 25, 12, 7, 15], [6, 5, 0, 21, 21, 8, 12, 11],
#         [17, 16, 21, 0, 41, 28, 23, 31], [26, 25, 21, 41, 0, 13, 32, 10],
#         [13, 12, 8, 28, 13, 0, 19, 3], [7, 7, 12, 23, 32, 19, 0, 22], [16, 15, 11, 31, 10, 3, 22, 0] ] # 69
# n = 3
# n_list = [ [0, 1, 3], [1, 0, 1], [3, 1, 0] ] # -1

res = 0
ck = [ [1] * n for _ in range(n) ]

for k in range(n): # 거쳐가는 노드
    for i in range(n): # 촐발 노드
        for j in range(n): # 도착 노드
            if k == i or i == j or k == j:
                continue

            if n_list[i][j] == n_list[i][k] + n_list[k][j]: # 한 번에 이동할 간선이 없을 경우 false를 만들기 위함
                ck[i][j] = 0

            if n_list[i][j] > n_list[i][k] + n_list[k][j]: # 최단 거리가 아닐 경우
                res = -1

if res != -1:
    for i in range(n):
        for j in range(i, n):
            if ck[i][j]:
                res += n_list[i][j]

print(res)

