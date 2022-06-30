'''
구현 문제

단순하게 구현 하는 문제인데 너무 생각없이 풀다가 [0] * m(자리) 만큼 해야 되는데
p로 곱했어서 인덱스 에러가 나왔다.

in
    3
    4 1
    1
    1
    1
    1
    4 4
    1
    2
    3
    4
    4 4
    1
    4
    1
    4
out
    3
    0
    2
'''

k = int(input())

for _ in range(k):
    p, m = map(int, input().split())
    p_list = [0] + [0] * m
    res = 0

    for _ in range(p):
        a = int(input())

        if p_list[a] == 0:
            p_list[a] += 1
        else:
            res += 1

    print(res)