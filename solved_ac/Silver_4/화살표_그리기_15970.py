# 백준 - 실버4 - 화살표 그리기 - 15970 - 완전 탐색, 정렬 문제
'''
완전 탐색, 정렬 문제

풀이 과정
    1. 입력 값을 입력 받는다.
    2. n_list에 입력 값을 저장한다.
    3. color_points에 defaultdict(list)를 저장한다.
    4. for문을 돌면서 color_points에 값을 저장한다.
    5. total_distance에 0을 저장한다.
    6. for문을 돌면서 total_distance를 계산한다.
    7. total_distance를 출력한다.
'''

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 5
# n_list = sorted([[0, 1], [1, 2], [3, 1], [4, 2], [5, 1]], key=lambda x: (x[1], x[0])) # 13
# n = 7
# n_list = sorted([[6, 1], [7, 2], [9, 1], [10, 2], [0, 1], [3, 1], [4, 1]], key=lambda x: (x[1], x[0])) # 16

from collections import defaultdict

color_points = defaultdict(list)
for x, y in n_list:
    color_points[y].append(x)

total_distance = 0
for color, locations in color_points.items():
    locations.sort()

    for i in range(len(locations)):
        if i > 0:
            left_distance = locations[i] - locations[i - 1]
        else:
            left_distance = float('inf')

        if i < len(locations) - 1:
            right_distance = locations[i + 1] - locations[i]
        else:
            right_distance = float('inf')
        
        total_distance += min(left_distance, right_distance)

print(total_distance)
