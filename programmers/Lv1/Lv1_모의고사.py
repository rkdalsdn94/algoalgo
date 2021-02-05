def solution(answers):
    answer = []
    
    a = [1, 2, 3, 4, 5] * int(len(answers) // 5 + 1)
    b = [2, 1, 2, 3, 2, 4, 2, 5] * int(len(answers) // 5 + 1)
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * int(len(answers) // 5 + 1)
    
    a_cnt = 0
    b_cnt = 0
    c_cnt = 0
    
    for i in range(len(answers)):
        if answers[i] == a[i] :
            a_cnt += 1
        if answers[i] == b[i] :
            b_cnt += 1
        if answers[i] == c[i] :
            c_cnt += 1
    temp = [a_cnt, b_cnt, c_cnt]
    
    for x, y in enumerate(temp):
        if y == max(temp):
            answer.append(x+1)
    
    return answer
print(solution([1,2,3,4,5])) # [1]
print(solution([1,3,2,4,2])) # [1,2,3]