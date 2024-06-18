# 백준 - 브론즈2 - Mad Scientist - 4580 - 구현 문제
'''
구현 문제

어떻게 풀어야 되는지 영어로 되어 있어 더 이해가 잘 안되는 문제였다.
입력으로 들어오는 처음 값이 k이고, 그 이후의 값들로 답을 구하는 걸 알고나면 금방 풀 수 있다.

풀이 과정
    1. 입력을 받고, k와 p_list를 만든다.
    2. k가 0이면 종료한다.
    3. res를 만들고, p_list를 돌면서 res에 값을 추가한다.
    4. res를 출력한다.

in
    6 2 7 7 8 12 13
    1 4
    3 4 4 5
    3 0 4 5
    5 2 2 4 7 7
    0
out
    1 1 2 2 2 2 2 4 5 5 5 5 6
    1 1 1 1
    1 1 1 1 3
    2 2 2 2 3
    1 1 3 3 4 4 4
'''

while True:
    k, *p_list = map(int, input().split())

    if k == 0:
        break

    res = [1] * p_list[0]

    for i in range(2, k + 1):
        x = p_list[i - 1] - p_list[i - 2]
        res += [i] * x

    print(*res)
