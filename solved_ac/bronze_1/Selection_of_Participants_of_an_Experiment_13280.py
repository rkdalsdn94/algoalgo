# 백준 - 브론즈1 - Selection of Participants of an Experiment - 13280 - 완전 탐색, 정렬 문제
'''
완전 탐색, 정렬 문제

단순 구현 문제이다.
정렬하고, 완전 탐색 방식으로 전체 값을 비교하여 최솟값을 찾으면 된다.

풀이 과정
    1. 입력 값을 입력 받는다.
    2. 입력 값을 정렬한다.
    3. res에 lst의 첫번째 값과 두번째 값을 뺀 값을 저장한다.
    4. for문을 돌면서 temp에 lst의 i번째 값과 i+1번째 값을 뺀 값을 저장한다.
    5. res와 temp를 비교하여 작은 값을 res에 저장한다.
    6. res를 출력한다.

in
    5
    10 10 10 10 10
    5
    1 5 8 9 11
    7
    11 34 83 47 59 29 70
    0
out
    0
    1
    5
'''

while 1:
    n = int(input())
    if n == 0:
        break

    n_list = sorted(list(map(int, input().split())))
    res = abs(n_list[0] - n_list[1])
    for i in range(1, n - 1):
        temp = abs(n_list[i] - n_list[i + 1])
        res = min(res, temp)

    print(res)
