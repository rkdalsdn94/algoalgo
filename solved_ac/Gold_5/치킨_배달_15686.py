# 백준 - 골드5 - 치킨 배달 - 15686 - 구현, 완전 탐색, 백 트래킹 문제
'''
구현, 완전 탐색, 백 트래킹 문제

완전 탐색으로만 풀었다. (나중에 백 트래킹 방식으로도 풀어보려고 한다.)
뭔가 설명을 하기 어려워 코드 옆에 주석을 적어놨다.

간단히 설명하면
치킨 집을 m개의 조합으로 만들고
각각의 집에서 치킨 거리를 계산 후 더 작은 값으로 갱신해나가면 된다.

참고할 만한 링크를 
'''

from itertools import combinations as combi

n, m = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n, m = 5, 3
# board = [
#     [0, 0, 1, 0, 0],
#     [0, 0, 2, 0, 1],
#     [0, 1, 2, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 2]
# ] # 5

house, chicken = [], []
res = 999999

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append([i, j])
        elif board[i][j] == 2:
            chicken.append([i, j])

for i in combi(chicken, m): # m 개의 치킨 집의 조합을 만든다.
    temp_city_chicken_len = 0

    for j in house: # 각각의 집을 돌면서
        temp_house_chicken_distance = 9999

        for k in range(m):# 치킨 거리를 계산
            chicken_len = abs(j[0] - i[k][0]) + abs(j[1] - i[k][1]) # |r1-r2| + |c1-c2| -> 치킨 거리 계산
            temp_house_chicken_distance = min(temp_house_chicken_distance, chicken_len) # 거리가 더 작은 값으로 갱신

        temp_city_chicken_len += temp_house_chicken_distance # 치킨 거리를 도시의 치킨 거리에 더한다.

    res = min(res, temp_city_chicken_len) # 도시의 치킨 거리와 새로 구한 temp 도시 치킨 거리를 비교해서 더 작은 값으로 갱신

print(res)
