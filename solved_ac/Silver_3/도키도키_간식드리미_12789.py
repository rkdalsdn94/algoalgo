# 백준 - 실버3 - 도키도키 간식드리미 - 12789 - 자료 구조(스택) 문제
'''
자료 구조(스택) 문제

stack을 활용하면 되는 문제이다.

입력으로 들어온 학생들의 번호표(n_list)의 값들을 스택에 담아두고 다음 계산을 진행한다.
    - stack이 비어있지 않고, 마지막 값이 temp와 같을 때마다 pop하고 temp를 1 증가한다.
위 과정을 n_list 모든 값까지 반복하고, stack이 비어있다면 'Nice'를 출력하고, 값이 들어있다면 'Sad'를 출력하면 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 5
# n_list = [5, 4, 1, 3, 2] # Nice

stack = []
temp = 1

for i in n_list:
    stack.append(i)

    while stack and stack[-1] == temp:
        stack.pop()
        temp += 1

if stack:
    print('Sad')
else:
    print('Nice')
