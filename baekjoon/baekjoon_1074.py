# 백준 1074 - Z

# n, r, c = map(int, input().split())
# res = 0


# def recursive(n, x, y):
#     global res
#     if n == 2:
#         if x == r and y == c:
#             print(res)
#             return
#         res += 1
#         if x == r and y + 1 == c:
#             print(res)
#             return
#         res += 1
#         if x + 1 == r and y == c:
#             print(res)
#             return
#         res += 1
#         if x + 1 == r and y + 1 == c:
#             print(res)
#             return
#         res += 1
#         return
#     recursive(n // 2, x, y)
#     recursive(n // 2, x, y + n // 2)
#     recursive(n // 2, x + n // 2, y)
#     recursive(n // 2, x + n // 2, y + n / 2)


# recursive(2 ** n, 0, 0)


n, r, c = map(int, input().split())
res = 0
while n > 0:
    temp = (2 ** n) // 2
    if n > 1:
        if temp > r and temp <= c:
            res += temp ** 2
            c -= temp
        elif temp <= r and temp > c:
            res += (temp ** 2) * 2
            r -= temp
        elif temp <= r and temp <= c:
            res += (temp ** 2) * 3
            r -= temp
            c -= temp
    elif n == 1:
        if r == 0 and c == 1:
            res += 1
        elif r == 1 and c == 0:
            res += 2
        elif r == 1 and c == 1:
            res += 3
    n -= 1
print(res)
