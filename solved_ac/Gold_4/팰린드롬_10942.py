# 백준 - 골드4 - 팰린드롬? - 10942 - dp 문제
'''
dp 문제

PyPy3로 제출하거나, input을 다음과 같이 바꿔야 된다. (import sys; input=sys.stdin.readline)

2차원 배열을 활용해서 풀아야 되는 문제이다.
n^2 으로 입력으로 들어온 수가 팰린드롬이 가능한지 아닌지를 미리 체크해놓고, 나중에 dp[i][j] 를 출력하는 방식으로 풀었다.
점화식을 이용해서 푸는 것보다 dp 테이블을 이용해서 이 전의 값들을 기억해서 푸는 메모이제이션의 성격이 더 강한 문제인거 같다.
아래 풀이 과정이 이해가 잘 안 간다면 다음의 링크에서 테스트로 적혀진 부분의 주석을 해제해서 실행해면 도움이 된다.
 - https://pythontutor.com/visualize.html#mode=edit

풀이 과정
 - 입력을 미리 다 받아놓고, dp 배열을 2차원으로 n * n 크기로 만들어 준다.
 - dp 배열의 대각선 방향을 1로 만든다. 이유는 m_list에서 같은 범위 일 때는 무조건 팰린드롬이 가능하기 때문에 dp[i][i]를 1로 바꾼다.
    - ex: m_list의 값이 [1, 1], [2, 2] 이런 식으로 들어오는 상황
 - n_list의 i 번째 글자의 다름 글자가 같은지 검사한다. ex: [1, 2], [2, 3] 이러한 상황
 - 다음 글자 이후의 값들에서 팰린드롬이 가능한지 검사한다.
 - 가능하다는 조건을 만족할 때 해당 dp 배열의 값을 1로 바꾼다.
    - 가능한지 확인하는 조건 : n_list[j] == n_list[temp] and dp[j + 1][temp - 1] == 1
        - temp의 값은 i + j + 2 이다. (+2를 하는 이유는 이 전까지 +1의 값들을 이미 검사를 완료함)
        - 이때 index가 범위를 벗어날 수 있으므로 range 함수의 인자로 n - 2의 범위로 제한해야 한다.

in
    7
    1 2 1 3 1 2 1
    4
    1 3
    2 5
    3 3
    5 7
out
    1
    0
    1
    1
'''

import sys; input=sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = [list(map(int, input().split())) for _ in range(m)]

# 테스트
# n = 7
# n_list = [1, 2, 1, 3, 1, 2, 1]
# m = 4
# m_list = [[1, 3], [2, 5], [3, 3], [5, 7]] # 1  \  0  \  1  \  1

dp = [[0] * n for _ in range(n)]

for i in range(n): # 대각선 방향으론 1이다. 즉, 범위가 같을 때는 어차피 한 글자이므로 팰린드롬이 가능
    dp[i][i] = 1

for i in range(n - 1): # 다음 글자가 팰린드롬이 가능한지 확인 (즉, 이 전의 글자랑 다음 글자가 같은지 확인)
    if n_list[i] == n_list[i + 1]:
        dp[i][i + 1] = 1
    else:
        dp[i][i + 1] = 0

for i in range(n - 2): # 검사하고자 하는 글자 + 2의 값부터 팰린드롬이 가능한지 확인
    for j in range(n - 2 - i):
        temp = i + j + 2

        if n_list[j] == n_list[temp] and dp[j + 1][temp - 1] == 1:
            dp[j][temp] = 1

for i, j in m_list:
    print(dp[i - 1][j - 1])
