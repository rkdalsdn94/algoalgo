# 백준 - 브론즈3 - IBM 빼기 1 - 6321 - 단순 구현, 문자열 문제
'''
단순 구현, 문자열 문제

단순 구현문제 이다. ord와 chr로 해당 글자를 찾으면 된다.
단, 90이 넘으면 26을 빼는거만 생각하면 된다.
'''

n = int(input())

for i in range(1, n + 1):
    word = input()
    res = ''

    for j in word:
        a = ord(j)

        if a >= 90:
            a -= 26

        res += chr(a + 1)
    
    print(f'String #{i}')
    print(res)
    print()
