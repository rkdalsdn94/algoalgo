# 백준 - 브론즈2 - 진법 변환 - 2745 - 구현, 수학, 문자열 문제
'''
구현, 수학, 문자열 문제

진법 변환을 하는 문제이다.

풀이 과정
    1. n, b를 입력받는다.
    2. n을 b진법으로 변환하여 출력한다.
        2.1. n을 뒤집어서 순회하면서 b의 i승을 곱하여 res에 더한다.
        2.2. 문자인 경우 ord를 사용하여 숫자로 변환한다.
        2.3. 숫자인 경우 int를 사용하여 숫자로 변환한다.
        2.4. res를 출력한다.
'''

def base_conversion(n, b):
    res = 0
    for i, num in enumerate(n[::-1]):
        if num.isdigit():
            res += int(num) * (b ** i)
        else:
            res += (ord(num) - ord('A') + 10) * (b ** i)
    return res

n, b = input().split()

# 테스트
# n, b = 'ZZZZZ 36'.split()

b = int(b)
print(base_conversion(n, b))
