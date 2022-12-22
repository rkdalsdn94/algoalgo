# 백준 - 골드5 - 벼락치기 - 14728 - dp, 배낭(knapsack) 문제
'''
dp, 배낭(knapsack) 문제

이 전에 풀었던 '평범한 배낭 - 12865' 문제랑 똑같이 풀면 된다.
풀이 과정도 똑같아서 '백준 - 평범한 배낭 - 12865 - 골드5 - dp, 배낭(knapsack) 문제' 파일 상단을 읽으면 된다.

풀이 과정 대신 느낀점을 간단하게 적어보면. 이 전에는 공부?를 좀 한 뒤에 문제가 풀렸다면,
최근에 몇 번 풀었던 문제라 그런지 너무 바로 풀렸다... 좀 더 익숙해지면 좋을거 같다.
'''

n, m = map(int, input().split())
n_list = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n, m = 3, 310
# n_list = [ [50, 40], [100, 70], [200, 150] ] # 220

dp = [0] * (m + 1)

for i in range(n):
    for j in range(m, 0, -1):
        if n_list[i][0] <= j and j - n_list[i][0] >= 0:
            dp[j] = max(dp[j], dp[j - n_list[i][0]] + n_list[i][1])
        else:
            break

print(dp[m])

'''
2중 배열로 풀기

n, m = map(int, input().split())
n_list = [ list(map(int, input().split())) for _ in range(n) ]

dp = [ [0] * (m + 1) for _ in range(n + 1) ]
n_list.insert(0, [0, 0])

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if n_list[i][0] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - n_list[i][0]] + n_list[i][1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][m])
'''
