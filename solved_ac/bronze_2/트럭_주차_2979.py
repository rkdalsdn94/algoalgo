'''
구현, 시뮬레이션 문제

문제에 '도착한 시간은 항상 떠난 시간보다 앞선다' 를 다시 말해보면 출차 시간으로 max값을 구할 수 있다. -> max_idx
출차 시간으로 구한 max값으로 temp의 배열의 길이를 초기화 한다. -> temp = [0] * max_idx
그 다음 입차 시간 ~ 출차 시간 - 1의 범위를 돌면서 해당 인덱스(temp의 인덱스)를 더하기 1을 한 후,
temp를 다시 돌면서 1대 주차일 땐 + a, 2대 주차일 땐 2(차가 2대) * b, 3대 일 땐 3(차가 3대) * c를 각각 더한 후 res를 출력했다.

현재 코드에선 parking_log의 각 길이의 범위가 100씩 3개만 있어서 막 구현해도 가능했는데, 조건이 더 많을 땐 수정해야 될거 같다.
'''

a, b, c = map(int, input().split())
parking_lot = [ list(map(int, input().split())) for _ in range(3) ]

# 테스트
# a, b, c = 5, 3, 1
# parking_lot = [ [1, 6], [3, 5], [2, 8] ] # 33
# a, b, c = 10, 8, 6
# parking_lot = [ [15, 30], [25, 50], [70, 80] ] # 480

max_idx = max(parking_lot[0][1], parking_lot[1][1], parking_lot[2][1])
temp = [0] * max_idx
res = 0

for i in parking_lot:
    for j in range(i[0], i[1]):
        temp[j] += 1

for i in temp[1:]:
    if i == 1:
        res += a
    if i == 2:
        res += 2 * b
    if i == 3:
        res += 3 * c

print(res)
