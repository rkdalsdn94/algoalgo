# pypy3 로 제출해야 함

n, res = 8, 0
# n, res = int(input()), 0

# 세로, 왼쪽 위, 오른쪽 아래 체크
ck1, ck2, ck3 = [0]*40 ,[0]*40, [0]*40

def dfs(x):
    global res
    if x == n:
        res += 1
        return
    for i in range(n):
        if ck1[i] or ck2[i+x] or ck3[x-i+n-1]:
            continue
        ck1[i] = ck2[i+x] = ck3[x-i+n-1] = 1
        dfs(x+1)
        ck1[i] = ck2[i+x] = ck3[x-i+n-1] = 0

dfs(0)
print(res) # 92
