# 백준 - 브론즈2 - 펫 - 1362 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

E : 펫을 운동, n 만큼의 시간이 지나면 체중 n 감소
F : 펫이 먹음, n 만큼의 시간이 지나면 체중 n 증가

단순하게 사칙연산을 하면서 구현하면 되는 문제이다.

in
    100 100
    F 10
    F 10
    E 20
    # 0
    50 30
    F 5
    E 20
    # 0
    0 0
out
    1 :-)
    2 :-(
'''

cnt = 1
while 1:
    o, w = map(int, input().split())
    if o == 0 and w == 0: break
    flag = False

    while 1:
        a, b = input().split()
        b = int(b)

        if a == '#':
            break
        elif a == 'E':
            w -= b
        elif a == 'F':
            w += b
        
        if w <= 0:
            flag = True

    if flag:
        print(f'{cnt} RIP')
    elif o // 2 < w < o * 2:
        print(f'{cnt} :-)')
    else:
        print(f'{cnt} :-(')
    cnt += 1