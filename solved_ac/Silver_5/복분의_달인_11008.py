# 백준 - 실버5 - 복붙의 달인 - 11008 - 단순 구현, 문자열 문제
'''
단순 구현, 문자열 문제

풀이 과정
    1. 입력을 받는다.
    2. s글자의 p가 몇 번 나오는지 count 한 값을 cnt에 담는다.
    3. s에서 p를 제거하고, (cnt + p를 제거하고 남은 s의 길이) 출력하면 된다.

in
    2
    banana bana
    asakusa sa
out
    3
    5
'''

t = int(input())
for _ in range(t):
    s, p = input().split()
    cnt = s.count(p)
    s = s.replace(p, '')
    print(cnt + len(s))
