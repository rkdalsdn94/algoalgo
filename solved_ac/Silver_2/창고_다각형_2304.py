# 백준 - 실버2 - 창고 다각형 - 2304 - 자료 구조(스택), 완전 탐색 문제
'''
자료 구조(스택), 완전 탐색 문제

참고
 - https://www.youtube.com/watch?v=CRSGqnTsKWk

풀이 과정
 1. 기둥들(n_list)에서 가장 높은 기둥(max_pillar)과 해당 기둥의 인덱스를 구한다. (인덱스 값으로 계산하기 때문에 정렬은 필요하지 않음)
 2. 가장 높은 기둥의 인덱스 값을 기준으로 왼쪽과 오른쪽을 따로 계산한 뒤 출력하면 된다. (이 부분을 완전 탐색으로 풀면 됨)
    2.1 - 왼쪽과 오른쪽을 구할 때 가장 높은 기둥이 왼쪽과 오른쪽 각각의 범위 내에서 바뀔 수 있으므로 다시 0으로 초기화해야 된다.

in
    7
    2 4
    11 4
    15 8
    4 6
    5 3
    8 10
    13 6
out
    98
'''

n = int(input())
n_list = [0] * 1001
max_idx = max_pillar = 0
res = 0

for _ in range(n):
    l, h = map(int, input().split())
    n_list[l] = h

    if max_pillar < h:
        max_idx, max_pillar = l, h


# 왼쪽
max_pillar = 0 # 왼쪽 범위 내애서 가장 높은 기둥이 바뀔 수 있으므로 초기화
for i in range(max_idx + 1):
    max_pillar = max(max_pillar, n_list[i])
    res += max_pillar

# 오른쪽
max_pillar = 0 # 왼쪽 범위 내애서 가장 높은 기둥이 바뀔 수 있으므로 초기화
for i in range(1000, max_idx, -1):
    max_pillar = max(max_pillar, n_list[i])
    res += max_pillar

print(res)
