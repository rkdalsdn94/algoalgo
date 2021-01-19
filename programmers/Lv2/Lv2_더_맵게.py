import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()

    while scoville[0] <= K:
        try:
            heapq.heappush(scoville, heapq.heappop(
                scoville) + heapq.heappop(scoville) * 2)
        except:
            return -1
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
