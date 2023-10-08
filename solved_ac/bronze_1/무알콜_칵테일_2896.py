# 백준 - 브론즈1 - 무알콜 칵테일 - 2896 - 수학, 사칙연산 문제
'''
수학, 사칙연산 문제

단순한 사칙 연산 문제이다.
입력으로 들어오는 a, b, c를 각각 i, j, k 로 나눈 뒤 제일 작은 값을 구한다.
제일 작은 값을 temp에 담아두고, i * temp, j * temp, k * temp 한 뒤 각각 a, b, c 의 값에서 뺀 값을 출력하면 된다.
'''

a, b, c = map(int, input().split())
i, j, k = map(int, input().split())

# 테스트
# a, b, c = 9, 9, 9
# i, j, k = 3, 2, 1 # 0 3 6
# a, b, c = 10, 10, 10
# i, j, k = 3, 3, 3 # 0 0 0
# a, b, c = 10, 15, 18
# i, j, k = 3, 4, 1 # 0 1.666667 14.666667

temp = min(a / i, b / j, c / k)
print(a - i * temp, b - j * temp, c - k * temp)
