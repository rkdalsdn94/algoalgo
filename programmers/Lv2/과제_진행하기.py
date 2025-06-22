# 프로그래머스 - Lv2 - 과제 진행하기 - 스택, 구현 문제
"""
스택, 구현 문제

[핵심 아이디어]
    1. 과제를 시작 시간 순으로 정렬하여 순차 처리
    2. 각 과제가 다음 과제 시작 전에 완료 가능한지 판단
    3. 완료 가능하면 완료 후 남은 시간으로 스택의 중단된 과제들 처리
    4. 완료 불가능하면 남은 시간을 계산하여 스택에 저장

[풀이 과정]
    1. 모든 과제의 시작 시간을 분 단위로 변환하고 시작 시간 순으로 정렬
    2. 각 과제에 대해 다음 과제와 비교
       a. 현재 과제 완료 시간 ≤ 다음 과제 시작 시간인 경우
          - 현재 과제를 완료하고 결과에 추가
          - 남은 시간(다음 과제 시작까지)으로 스택의 과제들을 LIFO 순서로 처리
       b. 현재 과제 완료 시간 > 다음 과제 시작 시간인 경우
          - 현재 과제를 중단하고 남은 시간을 계산하여 스택에 저장
    3. 마지막 과제는 항상 스택에 추가
    4. 스택에 남은 모든 과제들을 LIFO 순서로 완료
"""

def solution(plans):
    answer = []

    # 시간을 분 단위로 변환하는 함수
    def time_to_minutes(time_str):
        h, m = map(int, time_str.split(':'))
        return h * 60 + m

    # 과제 정보를 분 단위로 변환하고 정렬
    tasks = []
    for name, start, playtime in plans:
        start_time = time_to_minutes(start)
        duration = int(playtime)
        tasks.append([name, start_time, duration])  # 리스트로 생성 (수정 가능하도록)

    tasks.sort(key=lambda x: x[1])  # 시작 시간 순으로 정렬

    stack = []  # 중단된 과제들을 저장할 스택

    for i in range(len(tasks)):
        # 마지막 과제인 경우 스택에 추가하고 종료
        if i == len(tasks) - 1:
            stack.append(tasks[i])
            break

        # 현재 과제와 다음 과제 정보
        current_name, current_start, current_duration = tasks[i]
        next_name, next_start, next_duration = tasks[i + 1]

        # 현재 과제 완료 시간
        current_end_time = current_start + current_duration

        if current_end_time <= next_start:  # 현재 과제가 다음 과제 시작 전에 완료 가능
            # 현재 과제 완료
            answer.append(current_name)

            # 다음 과제 시작까지의 여유 시간 계산
            available_time = next_start - current_end_time

            # 여유 시간 동안 스택의 중단된 과제들을 순차적으로 처리
            while available_time > 0 and stack:
                prev_name, prev_start, prev_remaining = stack.pop()  # 가장 최근에 중단된 과제

                if available_time >= prev_remaining:  # 스택 과제를 완료할 수 있는 경우
                    answer.append(prev_name)
                    available_time -= prev_remaining
                else:  # 스택 과제를 부분적으로만 진행 가능한 경우
                    # 남은 시간으로 다시 스택에 저장
                    stack.append([prev_name, prev_start, prev_remaining - available_time])
                    available_time = 0

        else:  # 현재 과제가 다음 과제 시작 전에 완료 불가능
            # 현재 과제의 남은 시간 계산하여 스택에 저장
            actually_worked_time = next_start - current_start  # 실제 진행된 시간
            remaining_time = current_duration - actually_worked_time  # 남은 시간
            tasks[i][2] = remaining_time  # 남은 시간으로 업데이트
            stack.append(tasks[i])

    # 스택에 남은 모든 과제들을 완료 (LIFO 순서)
    while stack:
        name, start_time, remaining_time = stack.pop()
        answer.append(name)

    return answer

plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
res = ["korean", "english", "math"]
print(solution(plans) == res)

plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
res = ["science", "history", "computer", "music"]
print(solution(plans) == res)

plans = [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]
res = ["bbb", "ccc", "aaa"]
print(solution(plans) == res)
