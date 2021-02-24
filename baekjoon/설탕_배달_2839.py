# n = 18 # 4
# n = 4 # -1
# n = 6 # 2
# n = 9 # 3
# n = 11 # 3
n = int(input())
res = 0

while 1:
    if n % 5 == 0:
        res += n//5
        print(res)
        break
    n -= 3
    res += 1
    if n < 0 :
        print(-1)
        break
