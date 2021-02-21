def solution(d, budget):
    d.sort()
    while sum(d) > budget:
        d.pop()
    return len(d)
print(solution([1,3,2,5,4], 9)) # 3
print(solution([2,2,3,3], 10)) # 4