def solution(s):
    answer = 0
    res = []

    if len(s) <= 2:
        return len(s)

    for i in range(1, len(s)//2 + 1):
        str_temp = ""
        answer = 1
        temp = s[:i]
        for j in range(i, len(s), i):
            if s[j:i+j] == temp:
                answer += 1
            else:
                if answer == 1:
                    answer = ""
                str_temp += str(answer) + temp
                temp = s[j:i+j]
                answer = 1
        if answer == 1:
            answer = ""
        str_temp += str(answer) + temp
        res.append(len(str_temp))
    return min(res)


print(solution('aabbaccc'))  # 7
print(solution('ababcdcdababcdcd'))  # 9
print(solution('abcabcdede'))  # 8
print(solution('abcabcabcabcdededededede'))  # 14
print(solution('xababcdcdababcdcd'))  # 17
