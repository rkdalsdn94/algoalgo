'''
단순 구현 문제

n이 최대 100이니까 temp 리스트를 101개로 초기화 한 후에
초기화한 temp에서 0이 아니면 res + 1 아니면 0이면 temp[i] += 1 하면 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 3
# n_list = [1,2,3] # 0

temp = [0] * 101
res = 0

for i in n_list:
    if temp[i] != 0:
        res += 1
    else:
        temp[i] += 1

print(res)
