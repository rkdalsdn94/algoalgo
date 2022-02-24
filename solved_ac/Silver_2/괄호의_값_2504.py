'''
temp의 값을 스택에 넣을 때(append) * 2, * 3을 하고, --> 여는 괄호가 나오면 넣어 준다
스택에서 뺄 때(pop) // 2, // 3을 하면서 temp의 값을 맞춰준 후에, --> 닫는 괄호가 나올 때, 나누어 준다.
문자열의 길이만큼 반복하면서 닫는 괄호가 나왔을 때 (i - 1)의 값이 해당 괄호의 여는 괄호일 때만 res에 더해준다.

위에 설명이 이해가 잘 안 가면 밑에 코드들을 손으로 예제들 돌려보면 감이 온다. --> (내가 쓰고도 무슨 말인가 싶다...)

이상하게 이 문제는 난이도에 비해 유독 어려운 느낌이 많이 들었다. (작년에 시도했다가 포기했던 문제..)
손으로 좀 풀어보고 했으면 시도 횟수를 더 줄였을 거 같다. (작년 시도했던거 포함해서 21번만에 통과했다....)
'''
# s = input()
s = '(()[[]])([])' # 28
# s = '[][]((])' # 0
stack = []
res = 0
temp = 1

if s[0] == ')' or s[0] == ']': # 시작부터 잘못된 괄호
    res = 0
else:
    for i in range(len(s)):
        if (s[i] == ']' or s[i] == ')') and not stack: # 잘못된 괄호 체크 조건
            res = 0
            break
        elif s[i] == '(':
            stack.append(s[i])
            temp *= 2
        elif s[i] == '[':
            stack.append(s[i])
            temp *= 3
        elif s[i] == ')':
            if stack[-1] == '(':
                if s[i-1] == '(':
                    res += temp
                stack.pop()
                temp //= 2
        elif s[i] == ']':
            if stack[-1] == '[':
                if s[i-1] == '[':
                    res += temp
                stack.pop()
                temp //= 3

    if stack: # 스택이 깨끗하게 비워지지 않았으면 잘못된 괄호이다.
        res = 0

print(res)
