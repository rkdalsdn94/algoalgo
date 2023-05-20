# 백준 - 실버1 - 1로 만들기 2 - 12852 - dp, 그래프 문제
'''
dp, 그래프 문제

'백준 - 1로 만들기(1463)' 문제에서 어느 값을 사용하는지 history만 추가된 문제이다.
dp에 대한 풀이는 해당 과정과 똑같이 1로 만들기에서 1은 아무것도 안해도 되므로 0이고
2부턴 1을 더해가면서 2로 나눠질 때 또는 3으로 나눠질 때 값을 바꾸면 된다.
dp 식은 아래와 같다.
    ㄴ> dp[i] > dp[i // (2 | 3)] + 1 일 때 dp[i] = dp[i // (2 | 3)] + 1

그 과정에서 history를 i // (2 | 3)으로 값을 바꾸면서 n부터 역순으로 0이 되기 전까지 출력하면 된다.
'''

n = int(input())

# 테스트
# n = 2 # 2  \  2 1
# n = 10 # 3  \  10 9 3 1

dp = [0] * (n + 1)
history = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    history[i] = i - 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        history[i] = i // 2
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        history[i] = i // 3

print(dp[n])
temp = n
while 1:
    if temp == 0:
        break
    print(temp, end=' ')
    temp = history[temp]
