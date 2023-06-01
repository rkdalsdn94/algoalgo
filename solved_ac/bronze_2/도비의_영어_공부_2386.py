# 백준 - 브론즈2 - 도비의 영어 공부 - 2386 - 단순 구현, 문자열, 완전 탐색 문제
'''
단순 구현, 문자열, 완전 탐색 문제

'#' 이 들어오기 전까지 입력받은 문자열을 0~2 번째 글자(= a)까지, 2번째 글자부터 모두(= b) 이렇게 두 부분으로 쪼갠다.
0~2 번째(a), 2번째 글자부터 모두(b) 에서 b를 upper로 바꿔준 후 a 를 upper했을 때 count를 찾으면 되는 단순 구현 문제이다.

in
    g Programming Contest
    n New Zealand
    x This is quite a simple problem.
    #
out
    g 2
    n 2
    x 0
'''

while 1:
    word = input()

    if word == '#':
        break

    a, b = word[0:2], list(word[2:].upper())
    a = ''.join(a.split())

    print(a, b.count(a.upper()))
