# 백준 - 실버3 - 괄호 끼워넣기 - 11899 - 자료 구조(스택), 문자열 문제
'''
자료 구조(스택), 문자열 문제

풀이 과정
1. 입력받은 문자열 s를 순회하면서
2. '('이면 stack에 추가
3. ')'이면 stack의 마지막 원소가 '('이면 pop, 아니면 res += 1
4. 마지막에 res와 stack의 길이를 더한 다음 출력하면 된다.
'''

s = input()

# 테스트
# s = ')))()' # 3
# s = ')(()' # 2
# s = '))()((' # 4
# s = ')(()(()))' # 1

stack = []

res = 0

for i in s:
    if i == '(':
        stack.append(i)
    elif i == ')':
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            res += 1

print(res + len(stack))
