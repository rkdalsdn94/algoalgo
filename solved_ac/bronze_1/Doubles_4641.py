'''
단순 구현, 완전 탐색 문제

주어진 입력 리스트에서 0번째 인덱스를 제외한 수를 하나씩 뽑은 후 temp변수에 2배 한 후에
해당 temp가 입력 리스트 안에 있으면 res + 1 그 다음 res를 출력하면 된다.

in
    1 4 3 2 9 7 18 22 0
    2 4 8 10 0
    7 5 11 13 1 3 0
    -1
out
    3
    2
    0
'''

while 1:
    n_list = sorted(list(map(int, input().split())))
    res = 0

    if len(n_list) == 1:
        break

    for i in n_list[1:]:
        temp = i * 2

        if temp in n_list:
            res += 1
    print(res)
