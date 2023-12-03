# 백준 - 브론즈1 - 나는 학급회장이다 - 2456 - 구현, 많은 조건분기 문제
'''
구현, 많은 조건분기 문제

처음에 if 문을 많이 사용해서 풀었는데(80줄 정도 됨), 다른 사람 코드풀이에 엄청 좋은 풀이가 있어서 해당 방식으로 바꿨다.
모든 경우를 분기처리 하지 않고, 제곱을 이용해서 문제를 풀면 된다.

입력으로 들어오는 수의 합을 total_list 라는 이름으로 담고,
입력으로 들어오는 수의 제곱을 total_square_list 라는 이름으로 담는다.

total_list 에서 max 값이 1이면 해당 인덱스 + 1과 max 값을 출력하면 되고,
그게 아니라면 제곱된 값의 리스트를 이용해 답을 구하면 된다.
'''

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 6
# n_list = [
#     [3, 1, 2], [2, 3, 1], [3, 1, 2],
#     [1, 2, 3], [3, 1, 2], [1, 2, 3]
# ] # 1 13
# n = 6
# n_list = [
#     [1, 2, 3], [3, 1, 2], [2, 3, 1],
#     [1, 2, 3], [3, 1, 2], [2, 3, 1]
# ] # 0 12

total_list = []
total_square_list = []

for i in zip(*n_list):
    total_list.append(sum(i))
    total_square_list.append(sum([j * j for j in i]))

max_value = max(total_list)
if total_list.count(max_value) == 1:
    for i in range(3):
        if total_list[i] == max_value:
            print(i + 1, max_value)
            exit(0)

next_max_value = max(total_square_list)
idx = total_square_list.index(next_max_value)
if total_square_list.count(next_max_value) == 1:
    print(idx + 1, total_list[idx])
else:
    print(0, total_list[idx])
