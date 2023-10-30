# 백준 - 브론즈3 - 약수 구하기 - 2501 - 단순 구현, 완전 탐색 문제
'''
단순 구현, 완전 탐색 문제

입력으로 들어오는 n의 약수들을 divisor_list에 append 한 뒤,
k 번째가 되면 break를 하고 divisor_list의 마지막 값을 출력하면 된다.
반복문이 다 끝났을 때 temp의 값이 k보다 크거나 같지 않다면 0을 출력하면 된다.

엄청 단순한 문제인데, js를 연습하고 싶어서 이 문제를 풀었다.
'''

n, k = map(int, input().split())

# 테스트
# n, k = 6, 3 # 3
# n, k = 25, 4 # 0
# n, k = 2735, 1 # 1

divisor_list = []
temp = 0

for i in range(1, n + 1):
    if n % i == 0:
        divisor_list.append(i)
        temp += 1
    if temp == k:
        break
if temp >= k:
    print(divisor_list[-1])
else:
    print(0)
