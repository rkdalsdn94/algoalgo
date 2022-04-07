'''
in
    3
    0 10
    33 1005
    1 4
out
    2
    199
    0

문제상의 시간제한, input의 범위 등을 고려했을 때 2중 반복문을 돌려도 시간초과가 날거 같지 않았다.
코드 로직은 너무 단순해서 따로 적지 않고,
다른 사람들이 푼 코드를 봤을 때 시간을 더 효율적으로 하려면

2번째 반복문 내에서 while 문을 하면서
if n % 10 == 0 인지 검사하고 res += 1
if n // 10 <= 0 일때 while 문을 끝내면 더 빠르게 답을 구할수 있다.
'''

t = int(input())

for _ in range(t):
    res = 0
    n, m = map(int, input().split())

    for i in range(n, m + 1):
        res += str(i).count('0')

    print(res)
