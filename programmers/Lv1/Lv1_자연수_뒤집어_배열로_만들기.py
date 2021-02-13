def solution(n):
    answer = list(map(int, str(n)[::-1]))
    return answer
print(solution(12345)) # [5,4,3,2,1]