def solution(numbers):
    answer = []

    for i in numbers:
        if i % 2 == 0:
            temp = list('0' + bin(i)[2:])
            temp[-1] = '1'
        else:
            temp = list('0' + bin(i)[2:])
            idx = ''.join(temp).rfind('0')
            temp[idx] = '1'
            temp[idx+1] = '0'

        answer.append(int(''.join(temp), 2))

    return answer


print(solution([2,7])) # [3, 11]