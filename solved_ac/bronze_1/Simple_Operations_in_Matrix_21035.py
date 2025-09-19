# 백준 - 브론즈1 - Simple Operations in Matrix - 21035 - 구현 문제
"""
구현 문제

[핵심 아이디어]
    행 또는 열 단위로 값을 더하거나 빼는 연산을 수행한 후, 행렬의 합, 최솟값, 최댓값을 계산하는 문제

[풀이 과정]
    1. 행렬과 연산 명령어를 입력받음
    2. 각 연산 명령어에 따라 해당 행 또는 열의 모든 원소에 값을 더하거나 뺌
    3. 모든 연산이 끝난 후, 행렬의 합, 최솟값, 최댓값을 계산하여 출력
"""

n, m = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]
operation_cnt = int(input())
operation_list = [list(input().split()) for _ in range(operation_cnt)]

# 테스트
# n, m = 3, 4
# n_list = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
# operation_cnt = 2
# operation_list = [['row', '1', '3'], ['col', '4', '-2']] # 18 -1 4
# n, m = 4, 3
# n_list = [
#     [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10]
# ]
# operation_cnt = 5
# operation_list = [
#     ['row', '2', '-5'], ['col', '3', '6'], ['col', '1', '-10'], ['row', '4', '7'], ['col', '1', '3']
# ] # 122 -2 23
# n, m = 2, 3
# n_list = [[15, 7, 8], [31, 1, 14]]
# operation_cnt = 3
# operation_list = [['row', '2', '-15'], ['col', '1', '10'], ['row', '1', '2']] # 57 -14 27

res_sum, res_min, res_max = 0, float('inf'), float('-inf')

for command in operation_list:
    op_type, idx, val = command
    idx = int(idx) - 1
    val = int(val)

    if op_type == 'row':
        for j in range(m):
            n_list[idx][j] += val
    elif op_type == 'col':
        for i in range(n):
            n_list[i][idx] += val

for row in n_list:
    for col in range(len(n_list[0])):
        res_sum += row[col]
        res_min = min(res_min, row[col])
        res_max = max(res_max, row[col])

print(res_sum, res_min, res_max)
