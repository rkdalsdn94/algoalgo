# 백준 - 브론즈1 - 도비의 난독증 테스트 - 2204 - 문자열, 정렬 문제
'''
문자열, 정렬 문제

테스트 케이스 만큼 문자열을 입력받고 대문자(또는 소문자)로 만들고, 정렬한 다음 제일 앞에 있는 원소를 출력하면 되는 단순한 문제이다.
단, 원본 값으로 출력해야 되므로 res에 원본 값과 같이 대문자로 만드는 작업을 추가한다.
출력할 때 원본 값으로 출력하면 된다.

in
    3
    Cat
    fat
    bAt
    4
    call
    ball
    All
    Hall
    0
out
    bAt
    All
'''

while 1:
    n = int(input())
    if n == 0:
        break

    word_list = [input() for _ in range(n)]
    res = []

    for i in word_list:
        res.append([i.upper(), i])
    res.sort()
    print(res[0][1])
