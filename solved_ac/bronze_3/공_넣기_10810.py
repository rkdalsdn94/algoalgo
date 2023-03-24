# 백준 - 브론즈3 - 공 넣기 - 10810 - 단순 구현, 시뮬레이션 문제
'''
단순 구현, 시뮬레이션 문제

단순 구현 문제이다. res 리스트를 n + 1의 범위로 만들어 준 후,
해당 리스트의 a부터 b의 값을 c로 바꾸면 된다.
마지막에 출력할 때 res[1:] 이거만 신경쓰면 된다.

in
    5 4
    1 2 3
    3 4 4
    1 4 1
    2 2 2
out
    1 2 1 1 0
'''

n, m = map(int, input().split())
res = [0] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    
    for i in range(a, b + 1):
        res[i] = c

print(*res[1:])
