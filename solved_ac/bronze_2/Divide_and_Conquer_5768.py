# 백준 - 브론즈2 - Divide and Conquer - 5768 - 정수론, 사칙연산 문제
"""
정수론, 사칙연산 문제

[핵심 아이디어]
    1. M부터 N까지의 모든 숫자에 대해 약수의 개수를 계산한다
    2. 약수의 개수가 가장 많은 숫자를 찾되, 약수 개수가 같다면 더 큰 숫자를 선택한다
    3. 약수의 개수는 간단하게 나누어 떨어지는지 확인하여 계산한다

[풀이 과정]
    1. 각 테스트 케이스마다 M부터 N까지 모든 수를 확인한다
    2. 각 숫자의 약수 개수를 계산한다
    3. 약수 개수가 최대인 숫자 중 가장 큰 숫자를 출력한다
"""

# 약수의 개수를 계산하는 함수
def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

while True:
    M, N = map(int, input().split())

    if M == 0 and N == 0:
        break

    max_divisors = 0  # 최대 약수 개수
    max_number = M    # 최대 약수를 가진 숫자

    # M부터 N까지 모든 숫자 확인
    for num in range(M, N + 1):
        # 현재 숫자의 약수 개수 계산
        divisors = count_divisors(num)

        # 약수 개수가 더 많거나, 같지만 숫자가 더 큰 경우 업데이트
        if divisors > max_divisors or (divisors == max_divisors and num > max_number):
            max_divisors = divisors
            max_number = num

    print(max_number, max_divisors)
