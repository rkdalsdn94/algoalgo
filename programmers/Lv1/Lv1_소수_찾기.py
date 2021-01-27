import math


def ck(x):
    z = int(math.sqrt(x))
    for i in range(2, z + 1):
        if x % i == 0:
            return False
    return True


def solution(n):
    answer = 0

    for i in range(2, n+1):
        if ck(i):
            answer += 1
    return answer


print(solution(10))  # 4
print(solution(5))   # 3
