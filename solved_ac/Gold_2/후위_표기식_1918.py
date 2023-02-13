# 백준 - 골드2 - 후위 표기식 - 1918 - 구현, 자료 구조(스택) 문제
'''
구현, 자료 구조(스택) 문제

스택을 잘 활용해야 되는 문제이다. 사칙연산 우선순위는 아래와 같다.
 1. 괄호의 값
 2. 곱하기 또는 나누기
 3. 더하기 또는 빼기
위 조건을 가지고, stack을 이용해 문제를 풀어야 된다.

난이도에 비해 단순한 문제인 거 같았는 데 다 풀고 보니까 시간이 꽤 오래 걸렸다(1~2시간 정도 걸림)
처음 내가 푼 방식은 if 문이 너무 많아서 다른 사람의 풀이(아래 주소)를 참고 후 리팩토링 했다. (다 if 조건으로 구했다.)
'https://pannchat.tistory.com/entry/파이썬-백준-후위표기식-python'
'''

word = input()

# 테스트
# word = 'A+B' # AB+
# word = 'A+B*C' # ABC*+
# word = 'A*(B+C)' # ABC+*
# word = 'A+B*C-D/E' # ABC*+DE/-
# word = '(a+(b*c))' # abc*+
# word = 'A*B*C' # AB*C*

res = ''
stack = []

for i in word:
    if i == '(':
        stack.append(i)
    elif i in ['+', '-']:
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.append(i)
    elif i in ['*', '/']:
        while stack and stack[-1] in ['*', '/']:
            res += stack.pop()
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.pop()
    else: # 알파뱃인 경우
        res += i
    
while stack:
    res += stack.pop()

print(res)
