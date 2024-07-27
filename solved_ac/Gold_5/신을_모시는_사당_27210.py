# 백준 - 골드5 - 신을 모시는 사당 - 27210 - dp, 누적 합 문제
'''
dp, 누적 합 문제

풀이 과정
    1. 입력 값을 입력 받는다.
    2. res에 0을 저장한다.
    3. prefix_sum을 0으로 초기화한다.
    4. for문을 돌면서 prefix_sum을 계산한다.
    5. max_sum과 min_sum을 계산한다.
    6. res에 max_sum과 min_sum의 차이를 저장한다.
    7. res를 출력한다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 5
# n_list = [1, 1, 2, 1, 2] # 2
# n = 1
# n_list= [1] # 1
# n = 2
# n_list = [1, 2] # 1
# n = 6
# n_list = [2, 2, 1, 1, 2, 2] # 2
# n = 8
# n_list = [2, 2, 2, 1, 1, 2, 2, 2] # 4

res = 0
prefix_sum = [0] * (n + 1)

for i in range(1, n + 1):
    if n_list[i - 1] == 1:
        prefix_sum[i] = prefix_sum[i - 1] + 1
    else:
        prefix_sum[i] = prefix_sum[i - 1] - 1
    
max_sum = max(prefix_sum)
min_sum = min(prefix_sum)
res = abs(max_sum - min_sum)
print(res)
