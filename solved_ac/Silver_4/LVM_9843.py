# 백준 - 실버4 - LVM - 9843 - 구현, 시뮬레이션, 자료 구조(스택) 문제
'''
구현, 시뮬레이션, 자료 구조(스택) 문제

PUSH x: x라는 정수를 스택의 최상단에 추가합니다.
STORE: 스택의 최상단 값을 제거하고 레지스터에 저장합니다.
LOAD: 레지스터의 값을 스택의 최상단에 복사합니다.
PLUS: 스택의 상위 두 개의 값을 더하고 그 결과를 스택에 넣습니다.
TIMES: 스택의 상위 두 개의 값을 곱하고 그 결과를 스택에 넣습니다.
IFZERO n: 스택 최상단의 값이 0이면 n번째 명령어로 이동합니다.
DONE: 스택 최상단의 값을 출력하고 프로그램을 종료합니다.

[핵심 아이디어]
    1. 스택은 리스트로, 레지스터는 단일 변수로 구현
    2. 명령어 실행을 while 루프로 단순하게 구현
    3. 각 명령어의 동작을 직관적으로 구현

[풀이 과정]
    1. 스택, 레지스터, 명령어 포인터 초기화
    2. while 루프로 명령어 순차 실행
    3. 각 명령어별 조건문으로 분기 처리
    4. DONE 명령어 실행 시 결과 출력 후 종료
'''

def run_program(commands):
    stack = []
    register = 0
    ip = 0

    while ip < len(commands):
        command = commands[ip].split()  # 새로운 변수에 저장

        if command[0] == "PUSH":
            stack.append(int(command[1]))
            ip += 1

        elif command[0] == "STORE":
            register = stack.pop()
            ip += 1

        elif command[0] == "LOAD":
            stack.append(register)
            ip += 1

        elif command[0] == "PLUS":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
            ip += 1

        elif command[0] == "TIMES":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
            ip += 1

        elif command[0] == "IFZERO":
            value = stack.pop()
            if value == 0:
                ip = int(command[1])
            else:
                ip += 1

        elif command[0] == "DONE":
            return stack[-1]

n = int(input())
commands = [input() for _ in range(n)]

# 테스트
# n = 14
# commands = [
#     'PUSH 5', 'STORE', 'LOAD', 'LOAD', 'PUSH -1',
#     'PLUS', 'STORE', 'LOAD', 'IFZERO 13', 'LOAD',
#     'TIMES', 'PUSH 0', 'IFZERO 3', 'DONE'
# ] # 120

result = run_program(commands)
print(result)
