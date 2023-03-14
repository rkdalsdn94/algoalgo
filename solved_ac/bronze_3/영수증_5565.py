# 백준 - 브론즈3 - 영수증 - 5565 - 단순 구현, 사칙연산 문제
'''
단순 구현, 사칙연산 문제

처음 들어온 n - 나머지 입력 값들의 합을 출력하면 된다.
'''

n = int(input())
book_list = sum([ int(input()) for _ in range(9) ])

# 테스트
# n = 9850
# book_list = sum([ 1050, 800, 420, 380, 600, 820, 2400, 1800, 980 ])

print(n - book_list)
