# 백준 - 브론즈2 - Strfry - 11328 - 문자열, 구현 문제
'''
문자열, 구현 문제

단순한 문제이다. 정렬로 해결했다. 정렬이 아니라 count로도 해결할 수 있다.

풀이 과정
    1. 문자열을 입력받는다.
    2. 문자열을 정렬한다.
    3. 정렬된 문자열이 같다면 Possible을 출력한다.
    4. 정렬된 문자열이 다르다면 Impossible을 출력한다.
'''

t = int(input())
for _ in range(t):
    a, b = input().split()

    if sorted(a) == sorted(b):
        print('Possible')
    else:
        print('Impossible')
