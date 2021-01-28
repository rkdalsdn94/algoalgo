def solution(n):
    answer = n + 1
    while bin(n).count('1') != bin(answer).count('1'):
        answer += 1
    return answer


print(solution(78))  # 83
print(solution(15))  # 23
