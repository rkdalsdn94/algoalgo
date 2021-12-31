'''
    1 <= n <= 1,000,000,000   ==> n이 최대 10억이다
'''

def solution(n):
    res = [0,0,0,0,0,0,0,0,0,0]
    temp = 1

    while n != 0:
        while n % 10 != 9:
            for i in str(n):
                res[int(i)] += temp
            n -= 1
        if n < 10:
            for i in range(n + 1):
                res[i] += temp
            res[0] -= temp
            break
        else:
            for i in range(10):
                res[i] += (n // 10 + 1) * temp
        res[0] -= temp
        temp *= 10
        n //= 10

    return res

n = int(input())
answer = solution(n)

for i in answer:
    print(i, end=' ')
