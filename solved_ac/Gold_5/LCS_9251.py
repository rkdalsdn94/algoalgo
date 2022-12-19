# 백준 - 골드5 - LCS - 9251 - LCS, 문자열, dp 문제
'''
LCS, 문자열, dp 문제

LCS 알고리즘을 알고 있다면 쉽게 풀 수 있다. 해당 알고리즘을 잘 모른다면 아래 링크를 통해 공부하면 된다.
https://www.youtube.com/watch?v=z8KVLz9BFIo

풀이 과정
1. x랑 y를 리스트 형식으로 입력받는다.
2. 입력받은 x, y를 인자로 lcs 함수를 실행한다.
    2.1. dp 식에서 i - 1, j - 1의 범위에서 인덱스 에러를 방어하기 위해 x, y의 리스트에 각각 앞에 0을 추가해준다.
    2.2. n, m 이라는 이름으로 x와 y의 길이를 구하고 출력할 때 사용할 dp를 n과 m의 크기만큼 만든다.
    2.3. 1부터 n까지의 범위를 반복하면서 1부터 m까지 2중 반복문을 실행한다.
        2.3.1. 첫 번째 반복문의 x의 i번째 인덱스 값이 두 번째 반복문의 y의 j번째 인덱스의 값이랑 같은지 비교한다.
        2.3.2. 두 값이 같다면 dp[i][j]를 dp[i - 1][j - 1] 에다 1을 더해준다.
        2.3.3. 두 값이 다르면 dp[i][j]를 dp[i][j - 1], dp[i - 1][j] 두 값중 더 큰 값으로 바꿔준다.
    2.4. 위 과정을 n과 m까지의 범위만큼 반복한다.
3. 위 반복문으로 dp값이 구해졌으므로 가장 dp에 가장 마지막에 있는 값이 LSC 이므로 dp[-1][-1]의 값을 출력하면 된다.
'''

x, y = list(input()), list(input())

# 테스트
# x, y = list('ACAYKP'), list('CAPCAK') # 4

def lcs(x, y):
    x, y = [0] + x, [0] + y
    n, m = len(x), len(y)
    dp = [ [0] * m for _ in range(n) ]

    for i in range(1, n):
        for j in range(1, m):
            if x[i] == y[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[-1][-1]

print(lcs(x, y))
