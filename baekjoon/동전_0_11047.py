# pypy3 로 제출해야함 안그럼 시간초과 남..
# n, k = 10, 4200 # 6
# n, k = 10, 4790 # 12
# coin_list = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]
cnt = 0
coin_list.sort(reverse=True)

for i in coin_list:
    while k >= i:
        k -= i
        cnt += 1
print(cnt)
