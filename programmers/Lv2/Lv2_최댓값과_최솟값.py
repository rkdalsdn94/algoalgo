def solution(s):
    answer = sorted([ int(i) for i in s.split() ])
    return str(answer[0]) + ' ' + str(answer[-1])

print(solution('1 2 3 4')) # '1 4'
print(solution('-1 -2 -3 -4')) # '-4 -1'
print(solution('-1 -1')) # '-1 -1'