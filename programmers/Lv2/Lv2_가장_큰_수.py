def solution(numbers):
    answer = [str(i) for i in numbers]
    answer.sort(key=lambda x: x*3, reverse=True)
    # print(answer)

    return str(int(''.join(answer)))


print(solution([6, 10, 2]) == '6210')
print(solution([3, 30, 34, 5, 9]) == '9534330')
