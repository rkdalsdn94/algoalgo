# 백준 - 실버4 - 크림 파스타 - 25214 - dp, 그리디 문제
'''
dp, 그리디 문제

그리 어렵지 않은 dp 문제이다. max와 min 함수를 잘 활용하면 된다.

풀이 과정
1. n과 n_list를 입력 받은 후 temp에 n_list의 0번째 값을 대입한다, 정답으로 출력할 dp의 길이를 0으로 n개까지 만든다.
2. 1 부터 n 까지 반복하면서 dp의 값을 (이 전의 값과 dp[i-1], 현재 값에서 이 전 값을 뺀 (n_list[i] - temp) 두 값중 더 큰 값으로 바꾼다.
3. temp의 값을 temp와 현재 n_list의 값 중 더 작은 값으로 바꾼다.
4. dp를 모두 출력하면 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 6
# n_list = [ 50, 100, 70, 110, 10, 100 ] # 0 50 50 60 60 90
# n = 6
# n_list = [ 3, 3, 2, 8, 3, 1000000000 ] # 0 0 0 6 6 999999998

temp = n_list[0]
dp = [0] * (n)

for i in range(1, n):
    dp[i] = max(dp[i - 1], n_list[i] - temp)
    temp = min(temp, n_list[i])

print(*dp)
