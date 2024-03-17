# 백준 - 브론즈2 - 커맨드 - 17838 - 단순 구현, 문자열 문제
'''
단순 구현, 문자열 문제

단순히 문자열을 비교하면 되는 문제이다.

in
    1
    AABBABB
out
    1
in
    1
    ABBAABB
out
    0
in
    1
    ABCAFAGHWWE
out
    0
'''

t = int(input())
for _ in range(t):
    word = input()

    if len(word) == 7 and word[0] == word[1] == word[4] and word[2] == word[3] == word[-1] == word[-2] and len(set(word)) == 2:
        print(1)
    else:
        print(0)
