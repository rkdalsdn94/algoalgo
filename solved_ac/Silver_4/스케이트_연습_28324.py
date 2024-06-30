# 백준 - 실버4 - 스케이트 연습 - 28324 - 그리디 문제
'''
그리디 문제
'''

n = int(input())
V = []
temp = input().split()

for i in range(n - 1, -1, -1):
    V.append(int(temp[i]))

res = 1
cur_speed = 1

for i in range(1, n):

    if V[i] > cur_speed:
        cur_speed += 1
    else:
        cur_speed = V[i]

    res += cur_speed

print(res)
