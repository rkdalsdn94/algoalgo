a, b = input().split()
# 테스트
# a, b = 'adaabc', 'aababbc' # 2
# a, b = 'hello', 'xello' # 1
# a, b = 'koder', 'topcoder' # 1
# a, b = 'abc', 'topabcoder' # 0
# a, b = 'giorgi', 'igroig' # 6
res = []

for i in range(len(b) - len(a) + 1):
    cnt = 0

    for j in range(len(a)):
        if a[j] != b[i + j]:
            cnt += 1

    res.append(cnt)

print(min(res))