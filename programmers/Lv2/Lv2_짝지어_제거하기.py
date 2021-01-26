def solution(s):
    answer = []

    for i in s:
        if answer:
            if answer[-1] == i:
                answer.pop()
            else:
                answer.append(i)
        else:
            answer.append(i)
    return 0 if answer else 1


print(solution('baabaa'))  # 1
print(solution('cdcd'))  # 0
