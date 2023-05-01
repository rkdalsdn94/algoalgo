# 백준 - 실버1 - 안정적인 문자열 - 4889 - 자료 구조(스택), 문자열, 그리디 문제
'''
자료 구조(스택), 문자열, 그리디 문제

자료구조 중에서 스택을 구현하는 문제이다.
닫는 괄호가 나왔을 때 스택이 값이 있는지랑 마지막 값이 여는 괄호인지 검사한 후
- 맞으면 올바른 괄호가 되므로 pop한다.
- 아니면 닫는 괄호를 append 한다.

그 다음은 글로 설명하는 것보다 아래 링크에서 어떻게 동작하는지 코드를 실행해보면 이해가 더 편할거 같다.
https://pythontutor.com/visualize.html#mode=edit

in
    }{
    {}{}{}
    {{{}
    ---
out
    1. 2
    2. 0
    3. 1
'''

cnt = 1
while 1:
    data = input()
    res = 0

    if '-' in data:
        break

    stack = []
    for i in data:
        if i == '}' and stack and stack[-1] == '{':
            stack.pop()
        else:
            stack.append(i)
    
    while stack:
        temp_a, temp_b = stack.pop(0), stack.pop(0)

        if temp_a == temp_b:
            res += 1
        else:
            res += 2

    print(f'{cnt}. {res}')
    cnt += 1

