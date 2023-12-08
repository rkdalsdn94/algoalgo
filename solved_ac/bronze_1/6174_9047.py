# 백준 - 브론즈1 - 6174 - 9047 - 단순 구현, 문자열, 정렬, 시뮬레이션 문제
'''
단순 구현, 문자열, 정렬, 시뮬레이션 문제

입력으로 들어오는 문자열을 내림차순, 오름차순으로 정렬 후 두 수를 빼면 된다.
주의 사항으론 n의 길이가 4보다 작아지면 4까지의 길이를 '0'으로 채워야 한다.
이 부분을 zfill 함수를 이용해 풀었다. (입력오르 들어오는 n이 1000 ~ 9999 이므로 길이가 4까지만 들어옴)

in
    3
    6174
    1789
    2005
out
    0
    3
    7
'''

t = int(input())
for _ in range(t):
    n = input()
    res = 0

    while n != '6174':
        a = int(''.join(sorted(n, reverse=True)))
        b = int(''.join(sorted(n)))
        n = str(a - b).zfill(4)
        res += 1

    print(res)
