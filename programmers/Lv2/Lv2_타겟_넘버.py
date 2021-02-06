from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([0,0])
    
    while q:
        a, b = q.popleft()
        
        if b == len(numbers):
            if a == target:
                answer += 1
        else:
            q.append([a+numbers[b], b+1])
            q.append([a-numbers[b], b+1])      
    
    return answer
print(solution([1,1,1,1,1], 3)) # 5