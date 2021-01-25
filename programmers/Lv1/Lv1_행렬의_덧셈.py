def solution(arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        temp = []
        for x, y in zip(i, j):
            temp.append(x+y)
        answer.append(temp)

    return answer


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))  # [[4,6],[7,9]]
print(solution([[1], [2]], [[3], [4]]))  # [[4],[6]]
