# 프로그래머스 - Lv4 - 징검다리 - 이진 탐색
'''
이진 탐색 문제

rocks의 배열에서 distance를 append해야 된다.

풀이 과정
 1. 이진 탐색을 위해 rocks 리스트에 distance를 추가하고 정렬한다.
 2. start, end를 1, distance로 설정한다.
 3. start가 end보다 작거나 같은 동안 반복
   3.1. mid를 (start + end) // 2로 설정
   3.2. prev를 0으로 초기화하고, remove_cnt를 0으로 초기화한다.
   3.3. rocks를 돌면서 temp를 i - prev로 설정하고, temp가 mid보다 작은 경우 remove_cnt를 1 증가시킨다.
   3.4. remove_cnt가 n보다 큰 경우 end를 mid - 1로 설정하고, 그렇지 않은 경우 res를 mid로 설정하고, start를 mid + 1로 설정한다.
 4. res를 반환한다.
'''

def solution(distance, rocks, n):
    res = int(1e9)
    start, end = 1, distance
    rocks.append(distance)
    rocks.sort() # 정렬되어 있어야 이진 탐색 가능

    while start <= end:
        mid = (start + end) // 2
        prev = 0
        remove_cnt = 0

        for i in rocks:
            temp = i - prev

            if temp < mid:
                remove_cnt += 1

                if remove_cnt > n:
                    break
            else:
                prev = i

        if remove_cnt <= n:
            res = mid
            start = mid + 1
        else:
            end = mid - 1

    return res

print(solution(25, [2, 14, 11, 21, 17], 2)) # 4
