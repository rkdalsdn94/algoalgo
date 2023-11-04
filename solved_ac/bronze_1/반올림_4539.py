# 백준 - 브론즈1 - 반올림 - 4539 - 단순 구현, 사칙연산 문제
'''
단순 구현, 사칙연산 문제

1의 자리에서부터 1번째 인덱스까지 반올림하면 되는 단순한 문제이다.

풀이 과정
 - 입력으로 들어오는 숫자를 n_list라는 이름으로 int형으로 각 자리수를 가진 리스트로 만든다.
 - 역순으로 리스트의 값을 반복하면서 해당 자리가 5보다 크면 앞 자리(i - 1) 인덱스의 값에 1을 더한다.
 - 검사하던 리스트(i)의 값을 0으로 만든다. (5보다 크든 작든 반올림을 하면 0이 됨)
 - 출력할 때 join 함수를 이용하기 위해 n_list의 값을 map을 이용해 문자열로 바꾼 뒤 출력하면 된다.

in
    9
    15
    14
    4
    5
    99
    12345678
    44444445
    1445
    446
out
    20
    10
    4
    5
    100
    10000000
    50000000
    2000
    500
'''

t = int(input())
for _ in range(t):
    n_list = list(map(int, input()))

    for i in range(len(n_list) - 1, 0, -1):
        if n_list[i] >= 5:
            n_list[i - 1] = n_list[i - 1] + 1
        n_list[i] = 0

    print(''.join(map(str, n_list)))
