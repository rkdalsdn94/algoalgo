# 프로그래머스 - Lv2 - 호텔 대실 - 그리디, 정렬, 자료구조(힙) 문제
"""
그리디, 정렬, 자료구조(힙) 문제

[핵심 아이디어]
    1. 모든 예약 시간을 분 단위로 변환하여 다루기 쉽게 함
    2. 퇴실 시간에 청소 시간(10분)을 추가
    3. 시작 시간을 기준으로 예약을 정렬
    4. 사용 가능한 객실을 관리하기 위해 우선순위 큐(힙) 사용
    5. 각 예약에 대해, 가장 빨리 사용 가능한 객실을 배정하거나 새 객실 추가

[풀이 과정]
    1. 모든 예약의 시작 시간과 종료 시간을 분 단위로 변환
    2. 시작 시간을 기준으로 예약을 정렬
    3. 각 예약에 대해:
       a. 우선순위 큐에서 가장 빨리 사용 가능한 객실 확인
       b. 해당 객실의 사용 가능 시간이 현재 예약 시작 시간보다 이전이면 재사용
       c. 그렇지 않으면 새 객실 추가
       d. 객실의 사용 가능 시간을 현재 예약의 종료 시간 + 청소 시간으로 업데이트
    4. 최종적으로 사용된 객실 수 반환
"""

import heapq

def solution(book_time):
    # 시간을 분 단위로 변환하는 함수
    def time_to_minutes(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes

    # 예약 시간을 분 단위로 변환하고 [시작 시간, 종료 시간+청소 시간] 형태로 저장
    bookings = []
    for start, end in book_time:
        start_minutes = time_to_minutes(start)
        end_minutes = time_to_minutes(end) + 10  # 청소 시간 10분 추가
        bookings.append([start_minutes, end_minutes])

    # 시작 시간을 기준으로 정렬
    bookings.sort(key=lambda x: x[0])

    # 우선순위 큐를 사용해 객실 관리 (각 객실의 사용 가능 시간을 저장)
    rooms = []
    for start, end in bookings:
        # 사용 가능한 객실이 있고, 그 객실의 사용 가능 시간이 현재 예약 시작 시간보다 이전이면
        if rooms and rooms[0] <= start:
            # 해당 객실을 재사용
            heapq.heappop(rooms)

        # 새 객실을 추가하거나 기존 객실의 사용 가능 시간을 업데이트
        heapq.heappush(rooms, end)

    # 사용된 객실의 수 반환
    return len(rooms)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))  # 3
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))  # 1
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))  # 3
