# 백준 - 실버3 - izbori - 3161 - 구현 문제
'''
구현 문제

점수 계산을 위해 비교를 잘하고, 비교한 값을 기준으로 점수를 계산하면 되는 구현 문제이다.

풀이 과정
    1. 입력을 받고, m_list를 만든다.
    2. m이 1이면, m_list[0][0]을 출력하고 종료한다.
    3. 각 후보자 간 비교를 위한 ck 리스트를 만든다.
    4. m_list를 돌면서 각 후보자 간 비교를 하고, ck 리스트에 값을 저장한다.
    5. 각 후보자의 점수를 계산한다.
    6. 최고 점수를 찾고 출력한다.
'''


m, n = map(int, input().split())
m_list = [list(map(int, input().split())) for _ in range(m)]

# 테스트
# m, n = 1, 3
# m_list = [[1, 2, 3]] # 1
# m, n = 3, 4
# m_list = [
#     [4, 3, 2, 1], [1, 4, 3, 2], [2, 1, 4, 3]
# ] # 1  \  4
# m, n = 5, 5
# m_list = [
#     [1, 2, 3, 4, 5],
#     [5, 4, 3, 2, 1],
#     [1, 2, 3, 4, 5],
#     [5, 4, 3, 2, 1],
#     [3, 1, 2, 4, 5]
# ] # 3

if m == 1:
    print(m_list[0][0])
    exit(0)

# 각 후보자 간 비교
ck = [[0] * n for _ in range(n)]
for i in m_list:
    for j in range(n):
        for k in range(j + 1, n):
            ck[i[j] - 1][i[k] - 1] += 1

# 각 후보자의 점수 계산
score_list = [0] * n
for i in range(n):
    for j in range(n):
        if i != j and ck[i][j] > ck[j][i]:
            score_list[i] += 1

# 최고 점수를 찾고 출력
max_score = max(score_list)
for i in range(n):
    if score_list[i] == max_score:
        print(i + 1)
