# 백준 - 알바생 강호 - 실버4 - 그리디, 정렬 문제
'''
단순 정렬, 그리디 문제
'''

n = int(input())
n_list = sorted([ int(input()) for _ in range(n) ], reverse=True)

# 테스트
# n = 4
# n_list = sorted([3,3,3,3], reverse=True) # 6
# n = 3
# n_list = sorted([3,2,3], reverse=True) # 5
# n = 5
# n_list = sorted([7,8,6,9,10], reverse=True) # 30
# n = 5
# n_list = sorted([1,1,1,1,2], reverse=True) # 2
# n = 3
# n_list = sorted([1,2,3], reverse=True) # 4

res = 0

for i in range(n):
    temp = n_list[i] - i 

    if temp > 0:
        res += temp

print(res)