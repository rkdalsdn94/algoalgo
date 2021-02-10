from collections import deque
def solution(n, computers):
    answer = 0
    ck = [0] * n
    
    while 0 in ck:
        q = deque([ck.index(0)])
        while q:
            a = q.popleft()
            ck[a] = 1
            for i in range(len(computers[a])):
                if ck[i] == 0 and computers[a][i] == 1:
                    q.append(i)
        answer += 1
        
    return answer
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1
print(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])) # 3