def solution(num):
    answer = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
            answer += 1
        elif num % 2 == 1:
            num *= 3
            num += 1
            answer += 1
        if answer >= 500:
            return -1
    return answer
print(solution(6)) # 8
print(solution(16)) # 4
print(solution(626331)) # -1