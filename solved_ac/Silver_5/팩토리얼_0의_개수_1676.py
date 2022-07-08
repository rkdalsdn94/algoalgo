'''
수학 문제

n의 팩토리얼을 구한 후 문자로 캐스팅 한 뒤에 역순으로 반복문을 돌린다
역순으로 된 반복문에서 0이 아니게 되는 상황이 오면 반복문을 멈추고,
0이면 res를 더해가는 방식으로 풀었다.
'''

from math import factorial as fac

n = int(input())

# 테스트
# n = 10 # 2
# n = 3 # 0

res = 0

for i in str(fac(n))[::-1]:
    if i != '0':
        break
    res += 1

print(res)
