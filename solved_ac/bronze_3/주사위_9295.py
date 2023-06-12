# 백준 - 브론즈3 - 주사위 - 9295 - 단순 구현, 사칙연산 문제
'''
단순 구현, 사칙연산 문제

테스트 케이스만큼 입력으로 들어온 두 수의 합을 출력하면 되는 단순한 구현 문제이다.

in
    5
    1 2
    1 3
    3 5
    2 6
    3 4
out
    Case 1: 3
    Case 2: 4
    Case 3: 8
    Case 4: 8
    Case 5: 7
'''

t = int(input())
for i in range(1, t + 1):
    a, b = map(int, input().split())
    print(f'Case {i}: {a + b}')
