# 백준 - 골드3 - 나머지 합 - 10986 - 수학, 누적 합 문제
'''
수학, 누적 합 문제

풀이 과정
1. 누적 합과 나머지 연산의 성질을 이용한 접근
    - (A + B) % M = ((A % M) + (B % M)) % M
    - 두 구간의 누적 합을 각각 S1, S2라고 할 때,
    - S1 % M = S2 % M 이면 (S2 - S1) % M = 0
2. 누적 합의 나머지 값 계산
    - 각 위치까지의 누적 합을 M으로 나눈 나머지를 저장
    - dp[i]는 나머지가 i인 누적 합의 개수를 저장
3. 결과 계산
    - 나머지가 0인 경우는 그 자체로 하나의 구간이므로 더함
    - 같은 나머지를 가진 위치들 중 2개를 선택하는 조합을 계산
      (nC2 = n * (n-1) / 2)

시간 복잡도: O(N)
공간 복잡도: O(M)
'''

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, m = 5, 3
# n_list = [1, 2, 3, 1, 2] # 7

prefix_sum = 0
dp = [0] * m

for i in range(n):
    prefix_sum += n_list[i]
    dp[prefix_sum % m] += 1

res = dp[0]
for i in range(m):
    res += dp[i] * (dp[i] - 1) // 2

print(res)
