def solution(people, limit):
    people.sort(reverse=True)
    answer = len(people)
    start, end = 0, len(people) - 1

    while start < end:
        if people[start] + people[end] <= limit:
            answer -= 1
            end -= 1
        start += 1
    return answer


print(solution([70, 50, 80, 50], 100))  # 3
print(solution([70, 80, 50], 100))      # 3
print(solution([70, 40, 40, 40, 40, 40, 40, 40], 140))   # 4
