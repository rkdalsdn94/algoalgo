# 백준 - 실버2 - 배고픈 소 - 6193 - dp, 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence, LIS) 문제
'''
dp, 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence, LIS) 문제

입력 예제만 다르고 풀이는 기본적인 가장 긴 증가하는 부분 수열 문제와 똑같다.
문제를 똑바로 안 읽고 예제에 있는 입력 형식만 보고 list(map(int, input().split()))으로 받았다가 index error가 발생했다.

풀이 과정
    1. n을 입력받는다.
    2. cows를 입력받는다.
        2.1. cows의 길이가 n보다 작을 때까지 list 형태로 입력 받는데, 한 줄의 리스트?로 사용하기 위해 extend를 사용했다.
    3. dp를 만들어 1로 초기화한다.
    4. dp를 돌면서 다음을 확인한다.
        4.1. cows[j]가 cows[i]보다 작다면 dp[i]와 dp[j] + 1 중 큰 값을 dp[i]에 넣는다.
    5. dp의 최대값을 출력한다.
'''

n = int(input())
cows = []
while len(cows) < n:
    cows.extend(list(map(int, input().split())))

# 테스트
# n = 11
# cows = [2, 5, 18, 3, 4, 7, 10, 9, 11, 8, 15] # 7

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if cows[j] < cows[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
