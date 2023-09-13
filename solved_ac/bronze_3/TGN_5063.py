# 백준 - 브론즈3 - TGN - 5063 - 단순 수학, 사칙연산 문제
'''
단순 수학, 사칙연산 문제

입력으로 들어오는 r, c, e 세 수에서 r < e - c 를 만족하는지 확인하면 되는 문제이다.
만족하다면 'advertise'
만족하지 않다면 'do not advertise'
e - c의 값이 r과 같다면 'does not matter'
이렇게 출력하면 된다.

in
    3
    0 100 70
    100 130 30
    -100 -70 40
out
    advertise
    does not matter
    do not advertise
'''

n = int(input())

for _ in range(n):
    r, e, c = map(int, input().split())

    if r < e - c:
        print('advertise')
    elif r == e - c:
        print('does not matter')
    else:
        print('do not advertise')
