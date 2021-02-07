def solution(n):
    answer = sum([int(i) for i in str(n)])
    return answer
print(solution(123)) # 6
print(solution(987)) # 24