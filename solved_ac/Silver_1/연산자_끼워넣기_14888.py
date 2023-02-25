# 백준 - 실버1 - 연산자 끼워넣기 - 14888 - 완전 탐색, 백 트래킹 문제
'''
완전 탐색, 백 트래킹 문제

재귀로 depth 주면서 해당 연산자 리스트의 값이 있으면 그 연산자를 계산을 진행한다.
재귀는 글로 설명을 적는 거보다 동작 과정을 보는 게 더 좋은 설명이 될 거 같다.
https://pythontutor.com/visualize.html#mode=display 해당 링크에서 아래 코드를 실행해 보자.

in
    2
    5 6
    0 0 1 0
out
    30
    30

in
    3
    3 4 5
    1 0 1 0
out
    35
    17

in
    6
    1 2 3 4 5 6
    2 1 1 1
out
    54
    -24
'''

n = int(input())
n_list = list(map(int, input().split()))
operation_list = list(map(int, input().split())) # +, -, *, / 의 개수
max_res, min_res = -int(1e9), int(1e9)

def recursive(depth, num):
    global max_res, min_res

    if depth == n - 1:
        max_res = max(num, max_res)
        min_res = min(num, min_res)
        return
    
    for operation in range(4):
        if operation_list[operation]:
            operation_list[operation] -= 1

            if operation == 0:
                recursive(depth + 1, num + n_list[depth + 1])
            elif operation == 1:
                recursive(depth + 1, num - n_list[depth + 1])
            elif operation == 2:
                recursive(depth + 1, num * n_list[depth + 1])
            else:
                recursive(depth + 1, int(num / n_list[depth + 1]))

            operation_list[operation] += 1        

recursive(0, n_list[0])
print(max_res, min_res, sep='\n')
