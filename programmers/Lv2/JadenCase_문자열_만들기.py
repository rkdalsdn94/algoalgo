def solution(s):
    temp = s.lower().split(' ')
    answer = ''

    for i in temp:
        answer += i.capitalize() + ' '

    return answer[:-1]


print(solution('3people unFollowed me'))
print(solution('for the last week'))
