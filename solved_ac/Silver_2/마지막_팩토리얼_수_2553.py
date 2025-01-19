# 백준 - 실버2 - 마지막 팩토리얼 수 - 2553 - 수학, 정수론 문제
'''
수학, 정수론 문제

핵심 아이디어
    - 팩토리얼을 계산한 뒤 뒤에서부터 0이 아닌 수를 찾는다.

풀이 과정
    1. N을 입력받는다.
    2. 팩토리얼을 계산한다.
    3. 뒤에서부터 0이 아닌 수를 찾아 출력한다.
'''

n = int(input())

# 테스트
# n = 5 # 2

num = 1
for i in range(1, n + 1):
    num *= i

num = str(num)
res = ''
for i in range(len(num) - 1, -1, -1):
    if num[i] != '0':
        res = num[i]
        break

print(res)
