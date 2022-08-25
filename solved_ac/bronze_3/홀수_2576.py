'''
단순 구현 문제

홀수인지 계산하고 풀면 된다.
'''

n_list = [ int(input()) for _ in range(7) ]

# 테스트
# n_list = [12, 77, 38, 41, 53, 92, 85] # 256, 41
# n_list = [2, 4, 20, 32, 6, 10, 8] # -1

res = 0
minimum_num = 101

for i in n_list:
    if i % 2 != 0:
        res += i
        minimum_num = min(minimum_num, i)

if res != 0:
    print(res)
    print(minimum_num)
else:
    print(-1)