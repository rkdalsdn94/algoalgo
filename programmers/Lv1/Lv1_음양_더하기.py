def solution(absolutes, signs):
    answer = []
    for i, j in zip(absolutes, signs):
        answer.append(i) if j else answer.append(-i)

    return sum(answer)

print(solution([4,7,12], [True,False,True])) # 9
print(solution([1,2,3], [False,False,True])) # 0