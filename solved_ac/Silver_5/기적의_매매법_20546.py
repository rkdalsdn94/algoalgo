# 백준 - 실버5 - 기적의 매매법 - 20546 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

BNP와 TIMING의 자본금과 주식 수를 구하고, 비교하여 출력하면 되는 문제이다.
BNP의 경우, 주식 가격이 자본금보다 작거나 같을 때까지 주식을 사고, 마지막에 자본금을 갱신해야 된다.
TIMING의 경우, 3일 연속 주식 가격이 떨어지면 매수하고, 3일 연속 주식 가격이 오르면 매도해야 된다.

문제를 다 푼뒤 bnp와 timing을 더해주지 않아서 틀렸었다. bnp와 timing을 꼭 더해주어야 된다.
첫 번째 예제에서 timing_num의 자산은 195원이 되어야 된다. (마찬가지로 bnp도 더해주어야 한다.)

풀이 과정
 1. 입력을 받는다. (money : 초기 자본금, n_list : 14일 동안의 주식 가격)
 2. BNP와 TIMING의 자본금과 주식 수를 구한다.
 3. BNP와 TIMING의 자본금과 주식 수를 비교하여 출력한다.

주의할 점
 1. BNP와 TIMING의 자본금과 주식 수를 구할 때, 주식 가격이 자본금보다 작거나 같을 때까지 주식을 사고, 자본금을 갱신해야 된다.
 2. TIMING의 경우, 3일 연속 주식 가격이 떨어지면 매수하고, 3일 연속 주식 가격이 오르면 매도해야 된다.
 3. TIMING의 경우, 3일 연속 주식 가격이 떨어지면 매수하고, 3일 연속 주식 가격이 오르면 매도해야 된다.
 4. BNP와 TIMING의 자본금과 주식 수를 비교하여 출력한다.
'''

money = int(input())
n_list = list(map(int, input().split()))

# 테스트
# money = 100
# n_list = [10, 20, 23, 34, 55, 30, 22, 19, 12, 45, 23, 44, 34, 38] # BNP
# money = 15
# n_list = [20, 20, 33, 98, 15, 6, 4, 1, 1, 1, 2, 3, 6, 14] # TIMING

bnp, timing = money, money
bnp_num, timing_num = 0, 0
temp = 0

# BNP 매매
for i in n_list:
    if i <= bnp:
        bnp_num += bnp // i
        bnp %= i
bnp_num = bnp_num * n_list[-1] + bnp

# TIMING 매매
for i in range(3, len(n_list)):
    # print(n_list[i - 3], n_list[i - 2], n_list[i - 1], n_list[i])
    if n_list[i - 3] > n_list[i - 2] > n_list[i - 1] > n_list[i]: # 가격이 3일 연속 떨어지는 경우 (매수)
        temp += timing // n_list[i]
        timing = timing % n_list[i]

    if n_list[i - 3] < n_list[i - 2] < n_list[i - 1] < n_list[i] and temp > 0: # 가격이 3일 연속 오르는 경우 (매도)
        timing_num += temp * n_list[i]
        temp = 0

if b_temp != 0:
    timing_num += b_temp * n_list[-1]

if timing != 0:
    timing_num += timing

if bnp_num == timing_num:
    print('SAMESAME')
elif bnp_num > timing_num:
    print('BNP')
else:
    print('TIMING')
