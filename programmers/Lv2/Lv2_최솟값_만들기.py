def solution(A,B):
    answer = 0
    for i, j in zip(sorted(A), sorted(B, reverse=True)):
        answer += i * j
    return answer
print(solution([1,4,2],[5,4,4])) # 29
print(solution([1,2],[3,4])) # 10