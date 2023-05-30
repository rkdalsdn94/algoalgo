# 백준 - 브론즈1 - 벼락치기 - 23739 - 단순 구현, 수학 문제
'''
단순 구현, 수학 문제

절반 시간을 넘게되면 다음 챕터로 넘어갈 수 있다. 이 부분만 생각하고 문제를 풀면 if 조건문으로 쉽게 풀 수 있는 문제다.
'''

n = int(input())
arr = [ int(input()) for _ in range(n) ]

# 테스트
# n = 5
# arr = [10, 20, 30, 40, 50] # 5

limit_time = 30
half_time = 0
res = 0 

for i in range(n):
    if limit_time <= 0:
        limit_time = 30

    half_time = arr[i] / 2
    if limit_time - arr[i] >= 0:
        limit_time = limit_time - arr[i]
        res += 1
    elif limit_time - arr[i] <= 0 and limit_time >= half_time:
        limit_time = 0
        res += 1
    elif limit_time - arr[i] <= 0 and limit_time < half_time:
        limit_time = 0
        continue

print(res)
