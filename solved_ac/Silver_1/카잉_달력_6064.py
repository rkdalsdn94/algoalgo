'''
수학 문제

while 반복문 조건은 카잉 달력을 계산 했을 때 x는 (m * n)을 넘지 않는다.
x나 y중 하나 고정으로 한 후 m이나 n을 계속 더하면서
더해지는 값이 m * n보다 크면 -1 출력
더해지는 값이 n으로 나눠지면 고정한 값 출력으로 풀 수 있다.

in
    3
    10 12 3 9
    10 12 7 2
    13 11 5 6
out
    33
    -1
    83
'''

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    flag = True

    while x <= m * n:
        if (x - y) % n == 0:
            print(x)
            flag = False
            break
        x += m

    if flag:
        print(-1)
