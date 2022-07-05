'''
구현, 수학 문제

문제를 푸는 수학은 어렵지 않다.
전체 사각형에서 부분 사각형을 뺀 후에 k를 곱하면 되는데.. 구현이 은근 어려웠다.

바로 아래있는 풀이는 가장 긴 변 좌우의 차를 구해 조각난 부분 변의 정보를 구한 후에
전체 사각형에서 부분 사각형을 뺀 것이다..

'''

k = int(input())
farm = [ list(map(int, input().split())) for _ in range(6) ]

# 테스트
# k = 7
# farm = [[4, 50], [2, 160], [3, 30], [1, 60], [3, 20], [1, 100]] # 47600
# k = 1
# farm = [[3, 60],[2, 20],[3, 100],[1, 50],[4, 160],[2, 30]] # 6800

w, h, w_idx, h_idx = 0, 0, 0, 0

for i in range(len(farm)):
    if (farm[i][0] == 1 or farm[i][0] == 2) and w < farm[i][1]:
        w = farm[i][1]
        w_idx = i

    if (farm[i][0] == 3 or farm[i][0] == 4) and h < farm[i][1]:
        h = farm[i][1]
        h_idx = i

part_w = abs(farm[(w_idx - 1) % 6][1] - farm[(w_idx + 1) % 6][1])
part_h = abs(farm[(h_idx - 1) % 6][1] - farm[(h_idx + 1) % 6][1])
res = (w * h - part_w * part_h) * k

print(res)

'''
풀이 2
farm_keys -> 입력값의 방향만 따로 분리
farm_values -> 입력값의 길이만 따로 분리

방향이 1번만 있는 것은 가장 긴 변이다. -> (6각형이라는 문제 조건 기준)
가장 긴 변이 들어온 다음 세번째에 있는 변의 정보는 조각난 부분의 w아니면 h이다. -> w 인지 h인지 중요하지 않음
 ㄴ> 그림으로 그린 후 가장 긴 변 다음으로 3번째 변의 상태를 보면 알 수 있음

그 후에 가장 긴 변의 곱에서 조각나 있는 변의 정보의 곱을 뺀 후에 k를 다시 곱하면 된다....

k = int(input())
farm = [ list(map(int, input().split())) for _ in range(6) ]

# 테스트
# k = 7
# farm = [[4, 50], [2, 160], [3, 30], [1, 60], [3, 20], [1, 100]] # 47600
# k = 1
# farm = [[3, 60],[2, 20],[3, 100],[1, 50],[4, 160],[2, 30]] # 6800

farm_keys, farm_values, part_area, total_area = [], [], [], []

for i, j in farm:
    farm_keys.append(i)
    farm_values.append(j)

for i in range(1, 5):
    if farm_keys.count(i) == 1:
        total_area.append(farm_values[farm_keys.index(i)])
        temp_idx = farm_keys.index(i) + 3
        part_area.append(farm_values[temp_idx % 6])

res = (total_area[0] * total_area[1] - part_area[0] * part_area[1]) * k

print(res)
'''