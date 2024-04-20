# 백준 - 브론즈2 - 오타맨 고창영 - 2711 - 단순 구현, 문자열 문제
'''
단순 구현, 문자열 문제

단순한 문자열 구현 문제이다.
n - 1의 위치의 문자를 제거하면 된다.

풀이 과정
1. 입력을 받는다.
2. 입력받은 문자열을 리스트로 변환한다.
3. 리스트에서 n - 1 번째 인덱스를 제거한다.
4. 리스트를 문자열로 변환하여 출력한다.

in
    4
    4 MISSPELL
    1 PROGRAMMING
    7 CONTEST
    3 BALLOON
out
    MISPELL
    ROGRAMMING
    CONTES
    BALOON
'''

t = int(input())
for _ in range(t):
    n, m = input().split()

    n = int(n)
    m = list(m)
    m.pop(n - 1)

    print(''.join(m))
