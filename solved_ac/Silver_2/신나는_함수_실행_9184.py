# 백준 - 실버2 - 신나는 함수 실행 - 9184 - dp, 재귀 문제
'''
dp, 재귀 문제

문제에 있는 요구사항을 그대로 구현하면 되는데, dp를 활용해야 한다.
재귀함수로만 하면 매번 값을 계산해야 돼서 시간이 만힝 걸리게 된다.
따라서, dp의 메모이제이션 기법을 활용해서 한 번 계산된 값은 저장할 수 있도록 구현하면 된다.
'''

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
    dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]

dp = [[[0]*(21) for _ in range(21)] for _ in range(21)]
while 1:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break
    
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')