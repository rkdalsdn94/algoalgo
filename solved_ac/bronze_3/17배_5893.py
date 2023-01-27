####################################################
# 백준 - 브론즈3 - 17배 - 5893 - 단순 구현, 수학 문제
'''
단순 구현, 수학 문제

문제 분류에 수학도 있지만, 단순 구현만 잘 하면 풀 수 있는 문제이다.
앞에 '0b' 를 더해 문자열로 입력받고, 2진수로 만들어 준 후에 17을 곱한 다음 2진수로 출력하면 된다. 

- 다른 사람풀이 보니까 0b를 더하지 않아도 int(n, 2) -> 해도 괜찮다...
'''

n = '0b' + input()

# 테스트
# n = '0b' + '10110111' # 110000100111

res = int(n, 2) * 17

print(bin(res)[2:])
