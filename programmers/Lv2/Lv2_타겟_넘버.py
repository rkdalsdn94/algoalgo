# from collections import deque

# def solution(numbers, target):
#     answer = 0
#     q = deque()
#     q.append([0,0])
    
#     while q:
#         a, b = q.popleft()
        
#         if b == len(numbers):
#             if a == target:
#                 answer += 1
#         else:
#             q.append([a+numbers[b], b+1])
#             q.append([a-numbers[b], b+1])      
    
#     return answer
# print(solution([1,1,1,1,1], 3)) # 5

# 위에 처럼 풀고 다른 사람 풀이에 이거 봤는데 진짜 예술이다...
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target) 
print(solution([1,1,1,1,1], 3)) # 5