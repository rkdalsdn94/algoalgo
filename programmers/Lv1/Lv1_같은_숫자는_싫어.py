def solution(arr):
    temp = arr[0]
    answer = []
    answer.append(temp)
    for i in arr:
        if temp != i:
            answer.append(i)
        temp = i
    return answer

# print(solution([1,1,3,3,0,1,1]))
# print(solution([4,4,4,3,3]))
