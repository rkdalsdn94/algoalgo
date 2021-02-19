def solution(N, stages):    
    answer = {}
    users = len(stages)
    
    for i in range(1, N+1):
        if users == 0:
            answer[i] = 0
        else:
            answer[i] = stages.count(i) / users
        users -= stages.count(i)
    answer = sorted(answer.items(), key=lambda x: x[1], reverse=True)
    return [answer[i][0] for i in range(len(answer))]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3,4,2,1,5]
print(solution(4, [4,4,4,4,4])) # [4,1,2,3]