# 백준 - 실버5 - 파스칼의 삼각형 - 16395 - 수학, dp, 조합론 문제
'''
수학, dp, 조합론 문제

손으로 구하다보면 풀이가 나온다. dp 식으론 아래와 같다.
1로 초기화한 dp배열에 dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] 단, 1 ~ i 반복문을 돌아야 된다.

다른 사람 풀이에 되게 직관적인 풀이가 있어서 제일 아래 첨부한다. 이해가 안가면 해당 코드를 보면 좋을거 같다.(시간도 제일 빠름..)
'''

n, k = map(int, input().split())

# 테스트
# n, k = 5, 3 # 6
# n, k = 11, 3 # 45

dp = [ [1] * i for i in range(1, n + 1) ]

for i in range(2, n):
    for j in range(1, i):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

print(dp[n - 1][k - 1])

'''
백준 'gogotnals' 님의 풀이
직관적이면서 시간도 제일 빠르게 동작한다.

n,k = map(int,input().split())
dp =[[] for i in range(n)]
dp[0].append(1)

for i in range(1,n):
    dp[i].append(1)

    for j in range(i-1):
        dp[i].append(dp[i-1][j]+dp[i-1][j+1])

    dp[i].append(1)

print(dp[n-1][k-1])
'''