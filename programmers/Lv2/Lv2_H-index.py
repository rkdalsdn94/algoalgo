def solution(citations):
    citations = sorted(citations, reverse=True)
    for i in range(len(citations)):
        if i + 1 > citations[i]:
            return i
    return len(citations)


print(solution([3, 0, 6, 1, 5]))  # 3
