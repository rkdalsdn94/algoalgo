# 백준 - 브론즈2 - 소수 단어 - 2153 - 수학, 문자열 문제
'''
수학, 문자열 문제

단순히 문자열을 아스키 코드로 변환 후 소수인지 아닌지 확인하는 문제이다.

풀이 과정
 - 입력으로 들어온 문자열을 ord() 함수를 사용하여 아스키 코드로 변환 후 소문자인지 대문자인지 확인하여 값을 더한다.
    - 대문자일 경우 38을 빼고, 소문자일 경우 96을 빼면 된다.
    - 소문자는 1 ~ 26, 대문자는 27 ~ 52의 값을 가진다.
 - 소수인지 확인하는 함수(prime_check)를 만들어서 소수인지 아닌지 확인 후 출력한다.
 - 출력할 때 소수인지 아닌지에 따라 다른 문구를 출력한다.
'''

word = input()

# 테스트
# word = 'UFRN' # It is a prime word.
# word = 'contest'  # It is not a prime word.

def prime_check(n):
    if n < 1:
        return False
    if n == 1:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = sum([ord(i) - 38 if i.isupper() else ord(i) - 96 for i in word])

print('It is a prime word.' if prime_check(num) else 'It is not a prime word.')
