# 백준 - 실버4 - 프로그래밍 대회 전용 부지 - 9414 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

테스트케이스 만큼 반복하면서 0이 아닐 때까지 n_list에 값을 담는다.
내림차순으로 정렬한 뒤 2 * (n[0] ** 1), 2 * (n[1] ** 2), ..., 2 * (n[i] ** (i + 1)) 의 값을 res에 담는다.
res의 값이 5 * (10 ** 6) 보다 작으면 res를 출력하고, 크면 'Too expensive'를 출력하면 된다.

in
    3
    7
    2
    10
    0
    20
    29
    31
    0
    42
    41
    40
    37
    20
    0
out
    134
    17744
    Too expensive
'''

t = int(input())
for _ in range(t):
    n_list = []
    res = 0

    while 1:
        n = int(input())

        if n == 0:
            break

        n_list.append(n)

    n_list.sort(reverse=True)
    for i in range(len(n_list)):
        res += 2 * (n_list[i] ** (i + 1))

    if res <= 5 * (10 ** 6):
        print(res)
    else:
        print('Too expensive')
