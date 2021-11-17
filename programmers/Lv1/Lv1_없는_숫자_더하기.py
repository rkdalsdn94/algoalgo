def solution(numbers):
    answer = [0,1,2,3,4,5,6,7,8,9]
    
    for i in numbers:
        if i in answer:
            # print(i)
            answer.remove(i)
            
    return sum(answer)

print(solution([1,2,3,4,6,7,8,0])) #    14
print(solution([5,8,4,0,6,7,9]))   #    6