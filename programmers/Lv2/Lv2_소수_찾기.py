from itertools import permutations
import math


def solution(numbers):
    answer = []

    for i in range(1, len(numbers) + 1):
        num = list(set(map(''.join, permutations(numbers, i))))
        # print(num)
        for j in num:
            # print(j)
            if int(j) > 1:
                if ck(int(j)):
                    answer.append(int(j))

    # print(answer)

    return len(set(answer))


def ck(x):
    z = int(math.sqrt(x))
    for i in range(2, z + 1):
        if x % i == 0:
            return False
    return True


print(solution('17'))  # 3
print(solution('011'))  # 2
print(solution('123'))  # 5
