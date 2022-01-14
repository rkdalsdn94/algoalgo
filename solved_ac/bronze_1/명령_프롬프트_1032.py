n = int(input())
n_list = []

for _ in range(n):
    n_list.append(input())

# 테스트
# n = 3
# n_list = ['config.sys', 'config.inf', 'configures']
# n = 1
# n_list = ['onlyonefile']

res = list(n_list[0])

for i in range(1, len(n_list)):
    for j in range(len(n_list[i])):
        if res[j] != n_list[i][j] and res[j] != '?':
            res[j] = '?'

print(''.join(res))