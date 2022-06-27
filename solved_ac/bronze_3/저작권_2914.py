'''
단순 수학, 구현 문제

단순한 수학, 구현 문제이다.
    x / a = 올림한 값 i
ㄴ> x = (i - 1) * a + 1 --> i에서 1빼는 다시 더하는 이유는 올림한 값이므로 뺀 후에 다시 더해주면 된다.

단순하게 반복문으로 풀어보면 아래와 같다. --> 입력값이 크지 않아서 가능하다..
import math
a, b = map(int,input().split())
for x in range(100001):
    if math.ceil(x / a) == i:
        print(x)
        break
'''

a, i = map(int, input().split())

# 테스트
# a, i = 38, 24 # 875
# a, i = 1, 100 # 100
# a, i = 10, 10 # 91

print((i - 1) * a + 1)
