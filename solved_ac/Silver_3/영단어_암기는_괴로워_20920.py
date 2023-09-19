# 백준 - 실버3 - 영단어 암기는 괴로워 - 20920 - 문자열, 정렬, 자료 구조(해시, 딕셔너리) 문제
'''
문자열, 정렬, 자료 구조(해시, 딕셔너리) 문제

해시(파이썬에서는 딕셔너리라고 한다.)를 이용해서 입력받는 단어의 횟수를 카운트한다.
    단, m 길이 이상일 때만 딕셔너리에 저장해야 된다.
카운트 된 수 즉, 몇 번 입력될 때마다 1씩 더만 값을 기준으로 정렬을 한 뒤 출력하면 된다.
    정렬을 할 때에는 문제에 나온 다음을 기준으로 정렬해다 한다.
        1. 자주 나오는 단어일수록 앞에 배치한다.
        2. 해당 단어의 길이가 길수록 앞에 배치한다.
        3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
    lambda 를 이용해서 위 순서에 맞게 정렬했다. (-x[1], -len(x[0]), x[0]) 정렬 순서, 숫자는 -를 붙인 뒤 역순으로 만들어줘야 된다.

PyPy3로 제출하거나, 다음과 같이 입력 받식을 바꿔야 시간 초과가 안난다.
    import sys; input=sys.stdin.readline
    n, m = map(int, input().rstrip().split())
        .
        .
    for _ in range(n):
        word = input().rstrip()

        .
        생략
        .


in
    7 4
    apple
    ant
    sand
    apple
    append
    sand
    sand
out
    sand
    apple
    append

in
    12 5
    appearance
    append
    attendance
    swim
    swift
    swift
    swift
    mouse
    wallet
    mouse
    ice
    age
out
    swift
    mouse
    appearance
    attendance
    append
    wallet
'''

import sys; input=sys.stdin.readline

n, m = map(int, input().rstrip().split())
res = dict()

for _ in range(n):
    word = input().rstrip()

    if len(word) < m:
        continue

    if word in res:
        res[word] += 1
    else:
        res[word] = 1

for i, j in sorted(res.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
    print(i)
