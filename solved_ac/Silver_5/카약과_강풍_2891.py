# 백준 - 실버5 - 카약과 강풍 - 2891 - 구현, 그리디 문제
'''
구현, 그리디 문제

'''

n, s, r = map(int, input().split())
s_list = list(map(int, input().split()))
r_list = list(map(int, input().split()))

# 테스트
# n, s, r = 5, 2, 1
# s_list = [2, 4]
# r_list = [3] # 1
# n, s, r = 5, 2, 3
# s_list = [2, 4]
# r_list = [1,3,5] # 0
# n, s, r = 10, 1, 1
# s_list = [1, 3]
# r_list = [] # 2
# n, s, r = 10, 5, 2
# s_list = [1, 2,3,6,7]
# r_list = [7,8] # 4
# n, s, r = 5, 3, 3
# s_list = [2,3,4]
# r_list = [1,2,3] # 1

res = s

for i in r_list:
    if i in s_list:
        r_list.remove(i)
        s_list.remove(i)
        res -= 1

for i in s_list:
    for j in r_list:
        if j - 1 in r_list:
            r_list.remove(j)
            res -= 1
        elif j + 1 in r_list:
            r_list.remove(j)
            res -= 1
        elif j + 1 < i:
            break

print(res)
