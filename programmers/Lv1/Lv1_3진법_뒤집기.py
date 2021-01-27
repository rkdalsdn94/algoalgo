def solution(n):
    if n < 3:
        return n
    answer = ''
    while n // 3 >= 1:
        temp = n % 3
        n = n // 3
        answer = str(temp) + answer
        if n < 3:
            answer = str(n) + answer

    return int(answer[::-1], 3)


print(solution(45))
print(solution(125))
