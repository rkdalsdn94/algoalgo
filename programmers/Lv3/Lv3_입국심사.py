def solution(n, times):
    answer = 0
    times.sort()
    start, end = 1, times[-1] * n

    while start <= end:
        mid = (start + end) // 2 # 최악의 경우와 최선의 경우의 중간 값
        ck = 0 # mid라는 시간안에 몇 명이 통과할 수 있는지 체크하려는 변수

        # mid라는 시간안에 몇 명이 통과할 수 있는지 검사
        for i in times:
            ck += mid // i
            if ck >= n:
                break

        # 해당 시간안에 통과할 수 있는 경우 최솟값을 찾기 위해 검사
        if ck >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer

print(solution(6, [7, 10])) # 28