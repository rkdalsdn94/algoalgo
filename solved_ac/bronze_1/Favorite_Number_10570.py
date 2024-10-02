# 백준 - 브론즈1 - Favorite Number - 10570 - 단순 구현 문제
'''
단순 구현 문제

쪽지개수로 들어올 수 있는 수는 1 ~ 1000 이다.
따라서 1001개의 배열을 만들어서 각 숫자의 개수를 세서 가장 많이 나온 숫자를 출력하면 된다.

풀이 과정
    1. t를 입력받는다.
    2. t만큼 반복하며 n을 입력받고, n만큼 반복하며 arr를 입력받는다.
    3. arr를 순회하며 각 숫자의 개수를 센다.
    4. 가장 많이 나온 숫자를 출력한다.

in
    3
    3
    42
    42
    19
    4
    7
    99
    99
    7
    5
    11
    12
    13
    14
    15
out
    42
    7
    11
'''

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    cnt = [0] * 1001

    for i in arr:
        cnt[i] += 1

    print(cnt.index(max(cnt)))
