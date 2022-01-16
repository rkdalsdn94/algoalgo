n = int(input()) # n이 3, 4, 5, 6, 7, 8, 9, 14 이렇게 들어오면 --> 1/1, 1/2, 2/1, 3/1, 2/2, 1/3, 1/4, 2/3, 3/2, 2/4 이렇게 출력되어야 한다
cnt = 0

while n > cnt:
    n -= cnt
    cnt += 1

if cnt % 2 == 0:
    numerator, denominator = n, cnt - n + 1
else:
    numerator, denominator = cnt - n + 1, n

print(f'{numerator}/{denominator}')
