# 백준 - 실버3 - 후위 표기식2 - 1935 - 자료 구조(스택) 문제
'''
자료 구조(스택) 문제

전에 풀었던 '후위 표기식 - 1918' 문제랑 유사하다.
다른 점은 1918번 문제는 중위 표기식으로 되어 있는 식을 후위 표기식으로 바꾼 뒤 출력하는 문제라면
해당 문제는 후위 표기식으로 들어오는 식을 계산하는 문제이다.

풀이 과정
1918 번과 유사하게 이 문제도 스택을 활용해서 풀어야 한다.
입력으로 들어오는 word의 글자를 반복문으로 실행한다.
    - 글자가 들어왔을 경우 stack에 넣어준다.
        - 단, 해당 스택의 글자를 입력으로 들어오는 숫자로 변형해서 넣어야 편함, ord 함수를 통해 'A'를 빼서 구하면 됨
    - 연산자일 경우 stack에 들어있는 값을 두 개씩 꺼내서 해당 연산을 하고, res에 stack에 담는다.
반복문이 종료되면 스택에 한 개의 숫자만 있으므로 그 값을 소수점 2 번째 자리까지 출력하면 된다.
'''

n = int(input())
word = input()
n_list = [int(input()) for _ in range(n)]

# 테스트
# n = 5
# word = 'ABC*+DE/-'
# n_list = [1, 2, 3, 4, 5] # 6.20
# n = 1
# word = 'AA+A+'
# n_list = [1] # 3.00

stack = []

for i in word:
    if i.isalpha():
        stack.append(n_list[ord(i) - ord('A')])
        continue
    a, b = stack.pop(), stack.pop()

    if i == '+':
        stack.append(b + a)
    elif i == '*':
        stack.append(b * a)
    elif i == '-':
        stack.append(b - a)
    elif i == '/':
        stack.append(b / a)

print(f'{stack[0]:.2f}')
