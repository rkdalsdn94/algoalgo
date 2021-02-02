def solution(n):
    answer, temp = 0, 1
    
    for _ in range(n):
        answer, temp = temp, answer+temp
    
    return answer % 1234567

print(solution(3)) # 2
print(solution(5)) # 5