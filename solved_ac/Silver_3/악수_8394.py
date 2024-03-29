# 백준 - 실버3 - 악수 - 8394 - dp 문제
'''
dp 문제

dp 문제는 손으로 풀다보면 점화식이 생각난다.
이 문제 역시 n이 1일 때부터 5까지만 계산해도 점화식이 그려진다.

n = 1 -> 1, (악수를 안 할 경우 1가지)
n = 2 -> 2, (악수를 할 경우, 안 할 경우 2가지)
n = 3 -> 3, (그림으로 그려보면 이해가 됨)
n = 4 -> 5,           . (문제 예제)
n = 5 -> 8,           .

여기까지만 봐도 피보라치랑 유사하다는 느낌이 온다.
단, 조심해야 할 부분으로 문제에서 '마지막 자리만 출력한다.' 라고 되어 있다.
즉, 피보나치를 구하면서 % 10 을 통해 마지막 자리만 계산하면 된다.

다른 사람 풀이에선 속도가 엄청 빠르게 풀길래 확인해보니, n을 60으로 나머지 연산을 하는데 이렇게 하는게 속도가 훨씬 빠르다.
왜 그렇게 하는지 이유는 잘 모르겠는데, 속도가 훨씬 빨랐다.

n = int(input()) % 60 --> 이렇게 하면 속도가 엄청 빨라짐
'''

n = int(input())

# 테스트
# n = 1 # 1
# n = 2 # 2
# n = 3 # 3
# n = 4 # 5
# n = 5 # 8

dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10

print(dp[n])
