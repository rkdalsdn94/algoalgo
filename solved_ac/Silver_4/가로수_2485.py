# 백준 - 실버4 - 가로수 - 2485 - 수학, 정수론, 유클리드 호제법
'''
수학, 정수론, 유클리드 호제법

입력받은 가로수들(n_list)의 차를 유클리드 호제법으로 최대 공약수를 구한 뒤 심을 가로수의 개수를 구하면 된다.
가로수의 개수를 구하는 법은 (가로수의 간격 // 최대공약수 - 1)이다.
유클리드 호제법을 직접 구현하는 대신 gcd 함수를 사용했다.
'''

from math import gcd

n = int(input())
n_list = [int(input()) for _ in range(n)]

# 테스트
# n = 4
# n_list = [1, 3, 7, 13] # 3
# n = 4
# n_list = [2, 6, 12, 18] # 5

n_list_subtract = []
greatest_common_divisor = 0
res = 0

for i in range(n - 1):
    n_list_subtract.append(abs(n_list[i + 1] - n_list[i]))

for i in range(len(n_list_subtract)):
    greatest_common_divisor = gcd(greatest_common_divisor, n_list_subtract[i])

for i in n_list_subtract:
    res += i // greatest_common_divisor - 1

print(res)
