import math


def solution(n):
    if int(math.sqrt(n)) == math.sqrt(n):
        return int(math.sqrt(n) + 1) ** 2
    else:
        return -1


print(solution(121))
print(solution(3))
