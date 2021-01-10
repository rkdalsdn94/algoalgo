n, c = map(int, input().split())
nl = sorted([int(input()) for _ in range(n)])
# n, c = 5, 3
# nl = sorted([1, 2, 8, 4, 9])

start, end = 1, nl[-1] - nl[0]
res = 0
while start <= end:
    mid = (start + end) // 2
    temp = nl[0]
    cnt = 1

    for i in range(1, len(nl)):
        if nl[i] >= mid + temp:
            temp = nl[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)
