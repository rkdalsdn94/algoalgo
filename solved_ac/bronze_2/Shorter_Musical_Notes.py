# 백준 - 브론즈2 - Shorter Musical Notes - 6014 - 구현 문제
"""
구현 문제

[핵심 아이디어]
    누적 합 배열과 이진 탐색을 활용하여 각 쿼리에 대해 빠르게 음표 인덱스를 찾음
    - 누적 합 배열: 각 음표가 끝나는 시간을 저장
    - 이진 탐색: 주어진 시간에 해당하는 음표 인덱스를 빠르게 찾음

[풀이 과정]
    1. 각 음표의 길이를 입력받아 누적 합 배열을 생성
    2. 각 쿼리 시간에 대해 이진 탐색을 사용하여 해당 시간이 속하는 음표의 인덱스를 찾음
    3. 찾은 인덱스를 출력

in
    3 5
    2
    1
    3
    2
    3
    4
    0
    1
out
    2
    3
    3
    1
    1
"""

import bisect

N, Q = map(int, input().split())

cum_time = [0]
for _ in range(N):
    beats = int(input())
    cum_time.append(cum_time[-1] + beats)

for _ in range(Q):
    query_time = int(input())
    # bisect_right는 query_time보다 큰 첫 번째 원소의 인덱스를 반환
    note_index = bisect.bisect_right(cum_time, query_time)
    print(note_index)
