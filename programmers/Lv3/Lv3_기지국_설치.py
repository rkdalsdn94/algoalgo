# 프로그래머스 - Lv3 - 기지국 설치 - 그리디, 이분 탐색 문제
'''
그리디, 이분 탐색 문제

풀이 과정
 1. 기지국이 설치되어 있지 않은 구간을 찾아야 합니다.
 2. 기지국이 설치되어 있지 않은 구간을 찾으면, 2 * w + 1만큼 커버가 가능합니다.
 3. 따라서, start가 stations[end] - w보다 작으면, 커버가 안되는 것이므로 answer에 1을 더하고, start를 2 * w + 1만큼 이동합니다.
 4. start가 stations[end] - w보다 크면, 커버가 되는 것이므로, start를 stations[end] + w + 1로 이동합니다.
 5. start가 stations[end] + w보다 크면, end를 1 증가시킵니다.
 6. start가 n보다 작을 때까지 반복합니다.
 7. start가 n보다 크면, answer를 반환합니다.
'''

def solution(n, stations, w):
    answer = 0
    stations = sorted([s - 1 for s in stations])

    start, end = 0, 0

    while start < n and end < len(stations):
        if start < stations[end] - w:
            answer += 1
            start += 2 * w + 1

        if stations[end] - w <= start <= stations[end] + w:
            start = stations[end] + w + 1

        if start > stations[end] + w:
            end += 1

    while start < n:
        answer += 1
        start += 2 * w + 1

    return answer

print(solution(11, [4, 11], 1)) # 3
print(solution(16, [9], 2)) # 3
