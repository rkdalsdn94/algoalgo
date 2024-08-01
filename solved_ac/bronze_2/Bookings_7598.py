# 백준 - 브론즈2 - Bookings - 7598 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

문제의 난이도는 높지 않지만 영어 문제는 해석이 어렵다.
영어 공부하는 목적으로 영어 문제를 풀고 있는데 번역을 해도 이해가 잘 안되는 문제들이 종종 있다.
개인적으로 이 문제도 그런 문제 중 하나이다.
입력 값을 보고 유추해서 문제를 풀었다.

풀이 과정
1. 비행기 이름과 기본으로 사용될 좌석을 입력받는다.
    1.1. 해당 입력이 '#'이면 종료한다.
2. 예약을 입력받기 위해 while문을 돌린다.
    2.1. 예약이 'X'이면 종료한다.
3. transaction이 'B'이고, res + seat이 68보다 작거나 같으면 res에 seat을 더한다.
4. transaction이 'C'이고, res - seat이 0보다 크거나 같으면 res에 seat을 뺀다.
5. 위 과정을 반복하고 비행기 이름과 res를 출력한다.
'''

while 1:
    airplane_name, n = input().split()
    n = int(n)
    res = n

    if airplane_name == '#':
        break

    while 1:
        transaction, seat = input().split()
        seat = int(seat)

        if transaction == 'X':
            break

        if transaction == 'B' and res + seat <= 68:
            res += seat
        elif transaction == 'C' and res - seat >= 0:
            res -= seat

    print(airplane_name, res)
