'''
단순 구현, 사칙연산 문제

단순하게 구현하고 뺄셈 한 다음에 출력하면 된다.
'''

l, p = map(int, input().split())
describer = list(map(int, input().split()))

# 테스트
# l, p = 1, 10
# describer = [10, 10, 10, 10, 10] # 0 0 0 0 0
# l, p = 5, 20
# describer = [99, 101, 1000, 0, 97] # -1 1 900 -100 -3

res = []
temp = l * p

for i in describer:
    res.append(i - temp)

print(*res)