def solution(priorities, location):
    answer = 0
    q = [[idx, i] for i, idx in enumerate(priorities)]
    # print(q)
    while True:
        if q[0][0] == max(q)[0]:
            answer += 1

            if q[0][1] == location:
                return answer
            else:
                q.pop(0)
        else:
            q.append(q.pop(0))


# print(solution([2,1,3,2], 2))
# print(solution([1,1,9,1,1,1], 0))
