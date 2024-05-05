# 백준 - 실버2 - 황소 다마고치 - 23323 - 수학, 그리디 문제
'''
수학, 그리디 문제

그리디하게 문제를 풀면 된다.
n을 2로 계속 나누면서 0이 되기 전까지 m을 1씩 더하면 된다.
그후 m을 출력하면 되는 간단한, 그리디 문제이다.
즉, 황소의 체력이 1 남았을 때, 1 만큼의 먹이를 주는걸 구하는 것이다.
만약 m이 아니라 cnt를 1씩 더하는 방식을 했다면 출력할 때 cnt + m으로 출력하면 된다.

풀이 과정
 1. 입력을 받는다. (t : 테스트 케이스의 개수)
 2. t만큼 반복하면서 n, m을 입력 받는다.
 3. n이 0이 될 때까지 m을 1씩 더하고, n을 2로 나눈다.
 4. m을 출력하면 된다.

in
    2
    7 1
    8589934591 1

out
    4
    34
'''

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    while n > 0:
        m += 1
        n //= 2

    print(m)
