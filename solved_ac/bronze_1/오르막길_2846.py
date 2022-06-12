'''
구현 문제

단순 구현 문제다 근데 뭔가 생각보다 바로바로 구현이 이루어지진 않았다.
계속 구현 문제를 도전해봐야겠다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 5
# n_list = [1,2,1,4,6] # 5
# n = 8
# n_list = [12,20,1,3,4,4,11,1] # 8
# n = 6
# n_list = [10, 8, 8, 6, 4, 3] # 0

res, temp, num = [], n_list[0], 0

for i in range(1, n):
    if n_list[i] - temp > 0:
        num += n_list[i] - temp
        temp = n_list[i]
    else:
        res.append(num)
        temp = n_list[i]
        num = 0
else:
    res.append(num)

print(max(res))
