# n = int(input())
# m = int(input())
# g = [ [] * n for _ in range(n + 1)]
# for _ in range(m):
#     a,b = map(int, input().split())
#     g[a].append(b)
#     g[b].append(a)
# 테스트
n = 7
m = 6
g = [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
    
cnt = 0
ck = [0] * (n + 1)
def dfs(s):
    global cnt
    ck[s] = 1
    for i in g[s]:
        if ck[i] == 0:
            dfs(i)
            cnt += 1
 
dfs(1)
print(cnt)
