# 백준 - 골드5 - 개업 - 13910 - dp 문제
'''
dp 문제

dp를 사용하여 풀 수 있는 문제이다.
  웍의 조합을 활용해 가능한 모든 조합을 계싼하고,
  dp 배열을 이용해 주문량을 처리하기 위한 최소 요리 횟수를 계산한다.
  계산 결과를 바탕으로 주문량을 처리할 수 있는지, 최소 몇 번의 요리가 필요한지 출력한다.

풀이 과정
  1. possible을 생성하여 각 웍의 크기와 조합으로 만들 수 있는 모든 크기를 구한다.
  2. dp 배열을 초기화하고, 목표 주문량 n까지 가능한 최소 요리 횟수를 계산한다.
  3. 최종적으로 dp[n] 값을 확인하여 출력한다.
'''

from itertools import combinations

n, m = map(int, input().split())
wok = list(map(int, input().split()))

# 테스트
# n, m = 5, 2
# wok = [1, 3] # 2
# n, m = 6, 2
# wok = [1, 3] # 2

possible = set(wok)
for comb in combinations(wok, 2):
    possible.add(sum(comb))

dp = [10001] * (n+1)    # n그릇의 짜장면을 만들기 위해 필요한 최소 요리 횟수
dp[0] = 0

for i in range(1, n+1):
    for j in possible:
        if (i-j) >= 0 and dp[i-j]+1 < dp[i]:
            dp[i] = dp[i-j]+1

print(dp[n] if dp[n] != 10001 else -1)
