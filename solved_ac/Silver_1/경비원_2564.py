# 백준 - 실버1 - 경비원 - 2564 - 구현, 많은 조건 분기 문제
'''
구현, 많은 조건 분기 문제

풀이 과정
    1. w, h를 입력받는다.
    2. n을 입력받는다.
    3. n_list를 입력받는다.
    4. dong_dir, dong_dist를 입력받는다.
    5. res를 0으로 초기화한다.
    6. calc_dist 함수를 만들어서 동근이의 거리를 구한다.
    7. dong_distance를 구한다.
    8. n_list를 돌면서 상점의 거리를 구하고, path1과 path2를 구한다.
    9. res에 path1과 path2 중 작은 값을 더해준다.
    10. res를 출력한다.
'''

w, h = map(int, input().split())
n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]
dong_dir, dong_dist = map(int, input().split())

# 테스트
# w, h = 10, 5
# n = 3
# n_list = [[1, 4], [3, 2], [2, 8]]
# dong_dir, dong_dist = 2, 3 # 23

res = 0

def calc_dist(dir, dist):
    if dir == 1:
        return dist
    elif dir == 2:
        return w + h + (w - dist)
    elif dir == 3:
        return w + h + w + (h - dist)
    else:
        return w + dist

dong_distance = calc_dist(dong_dir, dong_dist) # 동근이의 거리
for i in range(n):
    dist2 = calc_dist(n_list[i][0], n_list[i][1]) # 상점의 거리
    path1 = abs(dong_distance - dist2)
    path2 = 2 * w + 2 * h - path1
    res += min(path1, path2)

print(res)
