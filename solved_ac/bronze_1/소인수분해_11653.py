# 백준 - 브론즈1 - 소인수분해 - 11653 - 수학, 정수론, 소수 판정 문제
'''
수학, 정수론, 소수 판정 문제

solved.ac 사이트에서 문제의 분류를 위와같이 해놨지만 단순 구현 문제인거 같다.
소인수분해하는 코드를 구현 후 제출하면 통과이다.
'''

n = int(input())

# 테스트
# n = 72 # 2  \  2  \  2  \  3  \  3
# n = 3 # 3
# n = 6 # 2  \  3
# n = 2 # 2
# n = 9991 # 97  \  103

if n == 1:
    print('')

for i in range(2, n + 1):
    if n % i == 0:
        while n % i == 0:
            print(i)
            n = n // i
