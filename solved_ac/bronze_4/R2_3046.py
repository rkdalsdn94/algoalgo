'''
단순 구현, 수학 문제

(r1 + r2) / 2 = s
r1 + r2 = s * 2
r2 = (s * 2) - r1 로 풀었다.
'''

r1, s = map(int, input().split())
res = s * 2 - r1
print(res)
