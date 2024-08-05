# 백준 - 실버1 - 본대 산책 - 12849 - dp 문제
'''
dp 문제

dp를 활용해서 풀면 된다.

손으로 풀다보면 감이 오는데, 그래도 어렵다면 다음의 블로그 내용 중 표를 참고해보자.
    - https://codingwonny.tistory.com/310 (표를 보면 이해가 쉬움)

풀이 과정
    1. 입력을 받는다.
    2. dp를 0으로 초기화한다.
    3. dp[0]을 1로 초기화한다.
    4. dp를 8번 반복한다.
        4.1. dp[0] = dp[1] + dp[2]
        4.2. dp[1] = dp[0] + dp[2] + dp[3]
        4.3. dp[2] = dp[0] + dp[1] + dp[3] + dp[4]
        4.4. dp[3] = dp[1] + dp[2] + dp[4] + dp[5]
        4.5. dp[4] = dp[2] + dp[3] + dp[5] + dp[7]
        4.6. dp[5] = dp[3] + dp[4] + dp[6]
        4.7. dp[6] = dp[5] + dp[7]
        4.8. dp[7] = dp[4] + dp[6]
    5. dp[0]을 출력한다.
'''

d = int(input())

# 테스트
# d = 10 # 9857

MOD= 1_000_000_007

dp = [1, 0, 0, 0, 0, 0, 0, 0]

for i in range(d):
    temp = [0] * 8
    temp[0] = dp[1] + dp[2]
    temp[1] = dp[0] + dp[2] + dp[3]
    temp[2] = dp[0] + dp[1] + dp[3] + dp[4]
    temp[3] = dp[1] + dp[2] + dp[4] + dp[5]
    temp[4] = dp[2] + dp[3] + dp[5] + dp[7]
    temp[5] = dp[3] + dp[4] + dp[6]
    temp[6] = dp[5] + dp[7]
    temp[7] = dp[4] + dp[6]

    for j in range(8):
        dp[j] = temp[j] % MOD

print(dp[0])
