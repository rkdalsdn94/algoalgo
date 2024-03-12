# 백준 - 골드3 - 행렬 곱셈 순서 - 11049 - dp, 수학 문제
'''
dp, 수학 문제

PyPy3로 제출해야 된다.
완전 탐색 방식으로 행렬을 직접 곱셈하면서 cnt하는 방식으로 횟수를 구할 순 있지만 시간 초과가 나온다. 즉, dp를 활용해야 한다.

연쇄 행렬 곱셈에 관한 문제이다.
행렬의 곱셈에서는 n * m 크기와 r * c 이렇게 두 개의 행렬이 있을 때 m과 r의 크기는 같아지만 곱셈을 할 수 있다.
 - m과 r은 각각 '첫 번째 행렬의 열 수'과 '두 번째 행렬의 행 수'이다.
 - 즉, 첫 번째 행렬의 열과 두 번째 행렬의 행이 같아지만 행렬의 곱셈을 진행할 수 있다.
 - 따라서, 행렬의 전체 곱셈 수를 구할 때는 n * m * c를 하면 된다.
    - ex) (2 * 3) 행렬과 (3 * 4) 행렬을 곱하면 2 * 4 행렬이 나오고, 원소를 곱하는 횟수는 2 * 3 * 4 = 24가 된다.
    - 다음은 (2 * 2) 행렬 곱하기 (2 * 2) 행렬의 예제 답은 2 * 2 * 2 = 8이다.
            a1 b1       a2 b2       (a1*a2 + b1*c2), (a1*b2 + b1*b2)
                    *           =>                                    -> 한 원소를 곱할 때 2번 곱하게 된다.
            c1 d1       c2 d2       (c1*a2 + d1*c2), (c1*b2 + d1*d2)
 - 위를 기준으로 풀면 된다.

참고
 - https://www.youtube.com/watch?v=5MXOUix_Ud4
 - 설명이 잘 되어 있는데 이 문제와 똑같진 않다. 이해하고 적절히 응용해야 됨

풀이 과정
 - 글로 적기 어려워서 다음의 링크에서 주석을 해제하고 테스트를 돌려보면 이해하는데 도움이 된다.
     https://pythontutor.com/render.html#mode=display (import sys 부분을 지워야 됨)
'''

import sys; input=sys.stdin.readline

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 3
# n_list = [[5, 3], [3, 2], [2, 6]] # 90

dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        if i + j == n:
            break

        dp[j][i + j] = int(1e9)
        for k in range(j, i + j):
            temp_a = dp[j][j + i]
            temp_b = dp[j][k] + dp[k + 1][i + j] + n_list[j][0] * n_list[k][1] * n_list[i + j][1]

            # 풀이 과정에 있는 링크에서 주석을 해제한 뒤 돌려보면 이해가 잘 된다.
            # print(n_list[j][0], n_list[k][1], n_list[i + j][1])
            # print(dp[j][k], dp[k + 1][i + j], n_list[j][0] * n_list[k][1] * n_list[i + j][1])

            dp[j][i + j] = min(temp_a, temp_b)

print(dp[0][n - 1])
