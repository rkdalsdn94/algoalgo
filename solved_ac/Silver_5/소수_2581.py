'''
소수 구하는 문제가 익숙하고, 문제 난이도도 높지 않아서 그런지 문제를 푸는데 어렵지 않았다.
여기서 소수 구하는 함수도 이 전에 소수 구하는 문제에서 사용했던 함수랑 비슷하게 나온거 같다.
소수가 있을 경우에는 소수들의 합과, 제일 작은 수를 출력하고
없을 경우엔 -1을 출력하면 되는 문제이다.
'''

# m = int(input())
# n = int(input())

# 테스트
m, n = 60, 100 # 620 \n 61
m, n = 64, 65 # -1


res = []

def isPrime(x):
    if x == 1:
        return False

    for i in range(2, int(x ** 0.5 + 1)):
        if x % i == 0:
            return False
    return True

for i in range(m, n + 1):
    if isPrime(i):
        res.append(i)

if res:
    print(sum(res))
    print(res[0])
else:
    print(-1)