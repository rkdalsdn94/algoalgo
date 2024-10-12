# 백준 - 실버1 - 어두운 건 무서워 - 16507 - 누적 합 문제
'''
누적 합 문제

누적 합을 사용하면 쉽게 풀 수 있다. (애초에 누적 합 문제)

풀이 과정
    1. r, c, q를 입력받는다.
    2. r_list를 입력받는다.
    3. q_list를 입력받는다.
    4. 누적 합을 저장할 prefix_sum을 생성한다.
    5. prefix_sum을 계산한다.
    6. q_list를 순회하며 total_sum과 total_cnt를 계산한다.
    7. total_sum을 total_cnt로 나눈 값을 출력한다.
'''

r, c, q = map(int, input().split())
r_list = [list(map(int, input().split())) for _ in range(r)]
q_list = [list(map(int, input().split())) for _ in range(q)]

# 테스트
# r, c, q = 5, 6, 1
# r_list = [
#     [4, 1, 3, 4, 9, 5],
#     [1, 2, 8, 7, 5, 5],
#     [8, 1, 2, 5, 3, 2],
#     [1, 5, 3, 4, 2, 5],
#     [5, 2, 1, 2, 3, 5]
# ]
# q_list = [[2, 2, 4, 5]] # 3
# r, c, q, = 4, 3, 5
# r_list = [[25, 93, 64], [10, 29, 85], [80, 63, 71], [99, 58, 86]]
# q_list = [[2, 2, 2, 3], [3, 2, 3, 3], [1, 2, 2, 2], [1, 2, 4, 3], [2, 3, 2, 3]] # 57  \  67  \  61  \  68  \  85

prefix_sum = [[0] * (c + 1) for _ in range(r + 1)]
for i in range(1, r + 1):
    for j in range(1, c + 1):
        prefix_sum[i][j] = (
            prefix_sum[i - 1][j] + prefix_sum[i][j - 1] + r_list[i - 1][j - 1] - prefix_sum[i - 1][j - 1]
        )

for r1, c1, r2, c2 in q_list:
    total_sum = (
            prefix_sum[r2][c2] - prefix_sum[r1 - 1][c2] - prefix_sum[r2][c1 - 1] + prefix_sum[r1 - 1][c1 - 1]
    )
    total_cnt = (r2 - r1 + 1) * (c2 - c1 + 1)
    print(total_sum // total_cnt)
