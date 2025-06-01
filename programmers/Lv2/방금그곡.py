# 프로그래머스 - Lv2 - 방금그곡 - 문자열, 구현, 시뮬레이션 문제
"""
문자열, 구현, 시뮬레이션 문제

테스트 34번만 실패한다면?
    - 문제 설명이 잘못 되어 있음
    - B#에 대해서도 replace 처리를 해야 함 (왜 안되지를 한참 고민하다 질문하기 탭을 참고 함)

[핵심 아이디어]
    1. #이 포함된 음표(C#, D#, F#, G#, A#)를 단일 문자로 변환하여 문자열 처리를 단순화
    2. 재생 시간에 따라 악보를 반복하거나 자르는 시뮬레이션 수행
    3. 부분 문자열 검색으로 기억한 멜로디가 포함되는지 확인
    4. 재생 시간이 긴 음악을 우선하고, 같으면 먼저 입력된 음악 선택

[풀이 과정]
    1. #이 포함된 음표들을 소문자로 변환하는 전처리 함수 구현
    2. 각 음악 정보에 대해:
       a. 시작 시간과 종료 시간으로부터 재생 시간 계산
       b. 악보와 기억한 멜로디를 전처리하여 변환
       c. 재생 시간만큼 악보를 반복하거나 잘라서 실제 재생된 멜로디 생성
       d. 기억한 멜로디가 실제 재생된 멜로디에 포함되는지 확인
    3. 조건을 만족하는 음악 중 재생 시간이 가장 긴 음악 반환
    4. 조건을 만족하는 음악이 없으면 "(None)" 반환
"""

import math

def replace_step(m: str):
    """#이 포함된 음표를 소문자로 변환하는 함수"""
    return (m.replace('C#', 'c').replace('D#', 'd')
            .replace('F#', 'f').replace('G#', 'g')
            .replace('A#', 'a').replace('B#', 'b')) # B#에 대해서도 추가해야 됨

def solution(m, musicinfos):
    answer = None
    max_play_time = 0
    m = replace_step(m)  # 기억한 멜로디 전처리

    for musicinfo in musicinfos:
        start_time, end_time, name, melody = musicinfo.split(',')

        # 재생 시간 계산 (분 단위)
        start_minutes = int(start_time[:2]) * 60 + int(start_time[3:])
        end_minutes = int(end_time[:2]) * 60 + int(end_time[3:])
        play_time = end_minutes - start_minutes

        # 악보 전처리
        melody = replace_step(melody)

        # 재생 시간만큼 멜로디 생성
        melody_repeated_count = math.ceil(play_time / len(melody))
        melody_played = (melody * melody_repeated_count)[:play_time]

        # 기억한 멜로디가 포함되고 재생 시간이 더 긴 경우 갱신
        if m in melody_played and play_time > max_play_time:
            answer = name
            max_play_time = play_time

    return '(None)' if answer is None else answer

# 테스트
print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))  # "HELLO"
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))  # "FOO"
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))  # "WORLD"
