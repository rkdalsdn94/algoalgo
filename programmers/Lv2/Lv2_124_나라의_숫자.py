def solution(n):
    answer = ''
    temp = [1, 2, 4]

    while n > 0:
        n -= 1
        answer += str(temp[n % len(temp)])
        n //= len(temp)

    return answer[::-1]


print(solution(5))
print(solution(10))
print(solution(6))
