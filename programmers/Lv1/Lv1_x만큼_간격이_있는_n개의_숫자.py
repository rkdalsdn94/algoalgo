def solution(x, n):
    answer, temp = [x], x
    while len(answer) != n:
        temp += x
        answer.append(temp)
    return answer


print(solution(2, 5))  # [2, 4, 6, 8, 10]
print(solution(4, 3))  # [4, 8, 12]
print(solution(-4, 2))  # [-4, -8]
