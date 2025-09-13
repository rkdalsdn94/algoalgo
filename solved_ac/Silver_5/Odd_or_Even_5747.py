# 백준 - 실버5 - Odd or Even - 5747 - 그리디 문제
"""
그리디 문제

[핵심 아이디어]
    John이 Mary에게 가장 불리하게 매칭하더라도 Mary가 확실히 이길 수 있는
    최소 게임 수를 계산. Mary가 이기려면 합이 짝수가 되어야 하므로
    (홀수+홀수) 또는 (짝수+짝수) 조합이 필요함.

[풀이 과정]
    1. Mary와 John의 홀수/짝수 개수를 각각 계산
    2. 전체 게임 수에서 Mary가 확실히 질 수밖에 없는 게임 수를 제외
    3. Mary가 확실히 이길 수 있는 게임 수 = 전체 - 확실히 지는 게임 수

in
    3
    1 0 4
    3 1 2
    9
    0 2 2 4 2 1 2 0 4
    1 2 3 4 5 0 1 2 3
    0
out
    0
    3
"""

while True:
    n = int(input())
    if n == 0:
        break

    mary_fingers = list(map(int, input().split()))
    john_fingers = list(map(int, input().split()))

    # Mary와 John의 홀수/짝수 개수 계산
    mary_odd = sum(1 for x in mary_fingers if x % 2 == 1)
    mary_even = n - mary_odd

    john_odd = sum(1 for x in john_fingers if x % 2 == 1)
    john_even = n - john_odd

    # Mary가 확실히 질 수밖에 없는 경우들 계산
    # (Mary 홀수 + John 짝수 = 홀수) 또는 (Mary 짝수 + John 홀수 = 홀수)
    certain_losses = min(mary_odd, john_even) + min(mary_even, john_odd)

    # Mary가 확실히 이기는 최소 게임 수
    res = n - certain_losses
    print(res)
