# 프로그래머스 - LV2 - 쿼드압축 후 개수 세기 - 재귀, 분할 정복 문제
'''
재귀, 분할 정복 문제

어제 백준에서 푼 '실버 1 - 쿼드트리(1992)' 문제랑 똑같이 풀었다.
단, 백준에서는 답으로 출력할 변수를 global로 설정 후 retune 값을 사용하지 않고 출력했었는데,
프로그래머스에선 그렇게 하면 전체 작업이 완료한 시점으로 바껴서 안 된다.
그래서 재귀 함수의 리턴값을 정한 후 문제를 풀었다.

board를 완전 탐색으로 돌면서 temp와 다른 값이 나왔을 때 분할해서 재귀 함수를 답을 도출해갔다.
'''

def recursive(x, y, n, arr, one, zero):
    temp = arr[x][y]
    new_n = n // 2

    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != temp:
                one, zero = recursive(x, y, new_n, arr, one, zero)
                one, zero = recursive(x, y + new_n, new_n, arr, one, zero)
                one, zero = recursive(x + new_n, y, new_n, arr, one, zero)
                one, zero = recursive(x + new_n, y + new_n, new_n, arr, one, zero)
                return one, zero

    if temp == 1: one += 1
    elif temp == 0: zero += 1
    return one, zero

def solution(arr):
    one, zero = recursive(0, 0, len(arr), arr, 0, 0)
    return [zero, one]

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])) # [4, 9]
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],
                [0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],
                [0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],
                [0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])) # [10, 15]
