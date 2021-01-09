n, m = list(map(int, input().split()))
xl = [input() for _ in range(n)]
# n, m = 4, 4
# xl = ['....', '....', '....', '....']

col_temp, low_temp = 0, 0

low = [0] * n
col = [0] * m

for i in range(n):
    for j in range(m):
        if xl[i][j] == 'X':
            low[i] = 1
            col[j] = 1

for i in range(len(low)):
    if low[i] == 0:
        low_temp += 1
for i in range(len(col)):
    if col[i] == 0:
        col_temp += 1

print(max(col_temp, low_temp))
