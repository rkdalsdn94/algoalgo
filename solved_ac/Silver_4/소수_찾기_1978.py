'''
단순 소수 찾기 문제이다.
전에 풀었던 방식대로 풀었다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 4
# n_list = [1, 3, 5, 7] # 3

res = 0

def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

for i in n_list:
    if is_prime(i):
        res += 1

print(res)
