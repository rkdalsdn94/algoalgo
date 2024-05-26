# 프로그래머스 - Lv3 - 입국심사 - 이진 탐색 문제
'''
이진 탐색 문제

해당 문제를 다시 풀었다. 전에 풀었던 방식과 좀 다르게 최근에 푼 이진 탐색 방식처럼 풀었다.

풀이 과정
1. start, end를 1, times 중 가장 큰 값 * n으로 설정
2. start가 end보다 작은 동안 반복
    2.1. mid를 (start + end) // 2로 설정
    2.2. cnt를 0으로 초기화하고, times를 돌면서 mid // i를 cnt에 더한다.
    2.3. cnt가 n보다 크거나 같은 경우 end를 mid로 설정하고, 그렇지 않은 경우 start를 mid + 1로 설정한다.
3. start를 반환한다.
'''

def solution(n, times):
    start, end = 1, max(times) * n

    while start < end:
        mid = (start + end) // 2
        cnt = sum([mid // i for i in times])

        if cnt >= n:
            end = mid
        else:
            start = mid + 1

    return start

print(solution(6, [7, 10])) # 28

# 예전 코드
'''
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
'''
