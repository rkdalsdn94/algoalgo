# 백준 - 브론즈1 - 더하기 2 - 10823 - 수학, 문자열, 사칙연산, 파싱 문제
'''
수학, 문자열, 사칙연산, 파싱 문제

단순히 풀면 되는 문제이다.

in
    10,20,
    3
    0,50
    ,1
    00
out
    210
'''

res = ''

while 1:
    try:
        s = input()
        res += s
    except:
        break

print(sum(map(int, res.split(','))))
