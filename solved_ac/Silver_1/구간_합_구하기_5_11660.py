# 백준 - 실버1 - 구간 합 구하기 5 - 11660 - dp, 누적 합 문제
'''
dp, 누적 합 문제

전에 풀었던 '주지수 - 15742' 문제와 비슷하다. 똑같은 방식으로 풀었다.
https://pythontutor.com/visualize.html#mode=display
여기 링크에서 아래 테스트로 적혀있는 부분 주석을 지운 후 한 번씩 돌려보면 누적 합 table이 어떻게 바뀌는지 보여서 이해하기 좋다.
'''

import sys; input=sys.stdin.readline

n, m = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(n) ]
coordinate_list = [ list(map(int, input().split())) for _ in range(m) ]

# 테스트
# n, m = 4, 3
# matrix = [ [1,2,3,4], [2,3,4,5], [3,4,5,6], [4,5,6,7] ]
# prefix_sum = [ [2,2,3,4], [3,4,3,4], [1,1,4,4] ]
# n, m = 2, 4
# matrix = [ [1,2], [3,4] ]
# prefix_sum = [ [1,1,1,1], [1,2,1,2], [2,1,2,1], [2,2,2,2] ]

prefix_sum_table = [ [0] * (n + 1) for _ in range(n + 1) ]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum_table[i][j] = matrix[i - 1][j - 1] + prefix_sum_table[i - 1][j] + prefix_sum_table[i][j - 1] - prefix_sum_table[i - 1][j - 1]

for x1, y1, x2, y2 in coordinate_list:
    res = prefix_sum_table[x1 - 1][y1 - 1] - prefix_sum_table[x1 - 1][y2] - prefix_sum_table[x2][y1 - 1] + prefix_sum_table[x2][y2]
    print(res)