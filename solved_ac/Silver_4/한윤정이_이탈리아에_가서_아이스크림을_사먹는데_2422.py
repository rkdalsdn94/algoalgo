# 백준 - 실버4 - 한윤정이 이탈리아에 가서 아이스크림을 사먹는데 - 2422 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

한윤정이 이탈리아에 가서 아이스크림을 사먹는데, 서로 다른 세 가지의 맛을 골라야 한다.
이때, 섞어먹으면 안 되는 조합의 개수를 출력하는 문제이다.

풀이 과정
    1. n, m을 입력받는다.
    2. range를 이용해 n_list를 만든다.
    3. m_list를 입력받는다.
    4. ck를 0으로 초기화 한 board를 만든다.
    5. m_list를 순회하며 m_list의 값을 ck[i][j]에 1로 변경한다.
    6. res를 0으로 초기화한다.
    7. n_list에서 3개의 조합을 구한다.
    8. ck[i[0] - 1][i[1] - 1], ck[i[0] - 1][i[2] - 1], ck[i[1] - 1][i[2] - 1]을 비교한다.
        8.1. 0이 아니면 continue하고, 0이면 res에 1을 더한다.
    9. res를 출력한다.
'''

from itertools import combinations

n, m = map(int, input().split())
n_list = list(range(1, n + 1))
m_list = [list(map(int, input().split())) for _ in range(m)]

# 테스트
# n, m = 5, 3
# n_list = list(range(1, n + 1))
# m_list = [[1, 2], [3, 4], [1, 3]] # 3

ck = [[0] * n for _ in range(n)]
for i, j in m_list:
    ck[i - 1][j - 1] = 1
    ck[j - 1][i - 1] = 1

res = 0
for i in combinations(n_list, 3):
    if ck[i[0] - 1][i[1] - 1] or ck[i[0] - 1][i[2] - 1] or ck[i[1] - 1][i[2] - 1]:
        continue
    res += 1

print(res)
