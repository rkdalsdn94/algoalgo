'''
처음에 다른 문제들 처럼 해당 수까지 소수를 찾는 방법으로 cnt를 증가시켰는데,
시간초과가 나왔다. 그래서 문제에 나온 범위까지 모든 소수를 구해놓고,
입력받는 수가 문제 범위 안에 있으면 res를 증가하는 방식으로 수정 후 통과했다.
'''

n = int(input())

def isPrime(x):
    if x == 1:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

all_prime_number = list(range(2, (123456 * 2) + 1))
temp = [ i for i in all_prime_number if isPrime(i) ]

while n != 0:
    res = 0

    for i in temp:
        if n < i <= n * 2:
            res += 1

    print(res)
    n = int(input())

