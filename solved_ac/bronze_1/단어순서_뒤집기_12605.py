# 백준 - 브론즈1 - 단어순서 뒤집기 - 12605 - 자료 구조(스택), 문자열, 파싱 문제
'''
자료 구조(스택), 문자열, 파싱 문제

스택을 사용하기 위해 res를 빈 리스로 둔 후
input 으로 들어오는 글자들을 담아둔 후 join을 이용해서 역순으로 만들고, 스페이스 바을 추가하는 방식으로 풀었다.

in
    3
    this is a test
    foobar
    all your base
out
    Case #1: test a is this
    Case #2: foobar
    Case #3: base your all
'''

n = int(input())

for i in range(1, n + 1):
    word_list = input().split()
    res = ' '.join(word_list[::-1])
    print(f'Case #{i}: {res}')
