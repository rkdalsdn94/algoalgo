from math import gcd
def solution(n, m):
    return [gcd(n,m),n * m // gcd(n, m)]
print(solution(3, 12)) # [3, 12]
print(solution(2, 5)) # [1, 10]