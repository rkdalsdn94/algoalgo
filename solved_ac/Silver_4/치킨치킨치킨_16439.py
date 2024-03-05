# 백준 - 실버4 - 치킨치킨치킨 - 16439 - 완전 탐색 문제
'''
완전 탐색 문제

m 종류의 치킨에서 3개를 골라야 돼서 combination을 활용했다.

풀이 과정
 - 입력값들을 잘 입력받고, combinations 함수를 이용해 m종류에서 3개의 값을 구한다.
 - 위에서 구한 3개의 값(인덱스)를 a, b, c로 두고 각 사람의 리스트를 돌면서 max값을 구한다.
 - max값에서 temp와 res를 서로 비교한 뒤 최종적으로 구한 res를 출력하면 된다.
'''

from itertools import combinations

n, m = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n, m = 3, 5
# n_list = [
#     [1, 2, 3, 4, 5],
#     [5, 4, 3, 2, 1],
#     [1, 2, 3, 2, 1]
# ] # 13
# n, m = 4, 6
# n_list = [
#     [1, 2, 3, 4, 5, 6],
#     [6, 5, 4, 3, 2, 1],
#     [3, 2, 7, 9, 2, 5],
#     [4, 5, 6, 3, 2, 1]
# ] # 25

combi = combinations(range(m), 3)
res = 0

for a, b, c in combi:
    temp = 0

    for i in range(n):
        temp += max(n_list[i][a], n_list[i][b], n_list[i][c])
    res = max(res, temp)

print(res)
