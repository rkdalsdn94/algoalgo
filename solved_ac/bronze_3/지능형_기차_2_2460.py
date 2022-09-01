# 백준 - 브론즈 3 - 지능형 기차 2 - 2460
'''
단순 구현, 수학, 사칙연산 문제 문제

temp에 내리는 사람을 뺀 후, 타는 사람을 더하면서 최댓값을 갱신시키면 된다.
'''

train_station = [ list(map(int, input().split())) for _ in range(10) ]

# 테스트
# train_station = [[0, 32], [3, 13], [28,  25], [17, 5], [21, 20],
#                  [11, 0], [12, 12], [4, 2], [0, 8], [21, 0]]  # 42

res = 0
temp = 0

for i, j in train_station:
    temp -= i
    temp += j    
    res = max(temp, res)

print(res)
