# 백준 - 실버4 - 피하자 - 25379 - 그리디 문제
'''
그리디 문제

짝수와 홀수를 양쪽으로 계산하면 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 1
# n_list = [1]  # 0
# n = 4
# n_list = [4, 5, 1, 0] # 2
# n = 4
# n_list = [1, 2, 3, 1] # 1

res1, res2 = 0,0
temp = 0
for i in n_list:
    if i % 2 == 1:
        temp += 1
    else:
        res1 += temp

n_list.reverse()
temp = 0
for i in n_list:
    if i % 2 == 1:
        temp += 1
    else:
        res2 += temp
print(min(res1, res2))
