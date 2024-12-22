# 백준 - 실버1 - Error Correction - 6586 - 에드 훅 문제
'''
에드 훅 문제

풀이 과정
    1. 입력값을 받는다.
    2. 입력값이 0인 경우 종료한다.
    3. 행과 열의 합이 홀수인 경우를 찾는다.
        3.1. 행의 합을 구한다
        3.2. 열의 합을 구하기 위해 zip을 사용해 전치행렬*로 변환한다 (전치행렬* : 원래 행렬의 행과 열을 뒤바꾼 행렬)
        3.3. 홀수인 행/열의 개수와 해당 위치를 동시에 저장한다
    4. 판단 조건:
        4.1. 홀수인 행과 열이 모두 없으면 이미 parity property를 만족하므로 "OK"
        4.2. 홀수인 행과 열이 각각 1개씩이면 그 위치의 비트를 변경하면 되므로 "Change bit"
        4.3. 그 외의 경우는 한 번의 비트 변경으로 해결할 수 없으므로 "Corrupt"
시간복잡도: O(n²) - 행렬 순회
공간복잡도: O(n²) - 입력 행렬과 전치행렬 저장

in
    4
    1 0 1 0
    0 0 0 0
    1 1 1 1
    0 1 0 1
    4
    1 0 1 0
    0 0 1 0
    1 1 1 1
    0 1 0 1
    4
    1 0 1 0
    0 1 1 0
    1 1 1 1
    0 1 0 1
    0
out
    OK
    Change bit (2,3)
    Corrupt
'''

while 1:
    n = int(input())

    if n == 0:
        break
    n_list = [list(map(int, input().split())) for _ in range(n)]
    change_row_col = list(map(list, zip(*n_list))) # 열을 행으로 변환 (세로 줄을 가로 줄로 변환), 전치행렬

    row, col = 0, 0
    row_idx, col_idx = 0, 0
    for i in range(n):
        if sum(n_list[i]) % 2 == 1:
            row += 1
            row_idx = i + 1
        if sum(change_row_col[i]) % 2 == 1:
            col += 1
            col_idx = i + 1

    if row == 0 and col == 0:
        print('OK')
    elif row == 1 and col == 1:
        print(f'Change bit ({row_idx},{col_idx})')
    else:
        print('Corrupt')
