def solution(bl, w, tw):
    answer = 0
    temp = []
    add = 0
    for i in tw:
        while 1:
            if not temp:
                temp.append(i)
                add += i
                answer += 1
                break
            elif len(temp) == bl:
                add -= temp.pop(0)
            else:
                if add + i > w:
                    answer += 1
                    temp.append(0)
                else:
                    temp.append(i)
                    add += i
                    answer += 1
                    break

    return answer + bl


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
