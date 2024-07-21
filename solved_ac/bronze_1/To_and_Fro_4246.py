# 백준 - 브론즈1 - To and Fro - 4246 - 구현, 문자열 문제
'''
구현, 문자열 문제

풀이 과정
1. 입력받은 문자열을 n 길이로 나누어 세로로 담는다.
2. 세로로 담은 문자열을 n 길이로 나누어 가로로 담는다.
    2.1. 가로로 담을 때, 짝수 번째 행은 왼쪽에서 오른쪽으로, 홀수 번째 행은 오른쪽에서 왼쪽으로 담는다.
3. 가로로 담은 문자열을 출력한다.

in
    5
    toioynnkpheleaigshareconhtomesnlewx
    3
    ttyohhieneesiaabss
    0
out
    theresnoplacelikehomeonasnowynightx
    thisistheeasyoneab
'''

while True:
    n = int(input())
    if n == 0:
        break

    word = input()
    rows = len(word) // n
    res = [[''] * n for _ in range(rows)]
    idx = 0

    for i in range(rows):
        if i % 2 == 0:
            for j in range(n):
                res[i][j] = word[idx]
                idx += 1
        else:
            for j in range(n - 1, -1, -1):
                res[i][j] = word[idx]
                idx += 1

    for j in range(n):
        for i in range(rows):
            print(res[i][j], end='')
    print()
