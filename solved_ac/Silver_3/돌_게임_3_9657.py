# 백준 - 실버3 - 돌 게임 3 - 9657 - 게임 이론, dp 문제
'''
게임 이론, dp 문제

dp는 보통 1부터 사용하기 위해서 n보다 좀 더 크게 만든다.
근데 이 문제는 돌을 1, 3, 4개 씩 가져갈 수 있으므로 최소 5는 돼야한다.
따라서, dp를 n + 5로 만든 후에 n 번째 돌을 가져가면 되니까 n - 1, n - 3, n - 4 째에 상대턴이 1개라도 SK가 있으면 이길 수 있다.

n이 10 까지의 상황을 본다면 아래와 같다.
n = 1  SK
n = 2  CY
n = 3  SK
n = 4  SK
n = 5  SK
n = 6  SK
n = 7  CY
n = 8  SK
n = 9  CY
n = 10 SK
'''

n = int(input())

# 테스트
# n = 6 # 'SK'

dp = [0] * (n + 5)
dp[1] = 1
dp[3] = 1
dp[4] = 1

for i in range(5, n + 1):
    if not dp[i - 1]:
        dp[i] = 1
    if not dp[i - 3]:
        dp[i] = 1
    if not dp[i - 4]:
        dp[i] = 1
    
if dp[n]: print('SK')
else: print('CY')
