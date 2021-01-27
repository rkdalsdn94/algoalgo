def solution(n):
    answer = ''
    temp = '수박'
    for i in range(n):
        answer += temp[i % 2]
    return answer


print(solution(3))
print(solution(4))
