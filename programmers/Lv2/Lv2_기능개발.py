def solution(progresses, speeds):
    answer = []
    # res = []

    for x, y in zip(progresses, speeds):

        if len(answer) == 0 or answer[-1][0] < abs((x-100)//y):
            answer.append([abs((x-100)//y), 1])
        else:
            answer[-1][1] += 1

    # for i in answer:
    #     res.append(i[1])

    return [res[1] for res in answer]


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
