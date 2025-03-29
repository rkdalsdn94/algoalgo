# 프로그래머스 - Lv2 - 파일명 정렬 - 문자열, 정렬, 구현
"""
문자열, 정렬, 구현

[핵심 아이디어]
    1. 파일명을 HEAD, NUMBER, TAIL로 분리한다.
    2. HEAD는 대소문자 구분 없이 사전순 정렬 (소문자로 변환하여 비교)
    3. NUMBER는 숫자로 변환하여 정렬 (앞의 0은 무시)
    4. HEAD와 NUMBER가 같을 경우 원래 순서 유지 (안정 정렬)

[풀이 과정]
    1. 각 파일명을 HEAD, NUMBER, TAIL로 분리
       - HEAD: 숫자가 나오기 전까지의 모든 문자
       - NUMBER: HEAD 이후 처음 나오는 연속된 숫자 (최대 5자리)
       - TAIL: NUMBER 이후의 모든 문자
    2. 분리된 파일명 정보를 저장
    3. HEAD(소문자 변환)와 NUMBER(정수 변환) 순으로 정렬
    4. 정렬된 파일명 반환
"""

def solution(files):
    answer = []

    for file in files:
        head, number, tail = '', '', ''

        # HEAD 추출 (숫자가 나올 때까지)
        i = 0
        while i < len(file) and not file[i].isdigit():
            head += file[i]
            i += 1

        # NUMBER 추출 (연속된 숫자, 최대 5자리)
        number_count = 0
        while i < len(file) and file[i].isdigit() and number_count < 5:
            number += file[i]
            i += 1
            number_count += 1

        # TAIL 추출 (나머지 부분)
        tail = file[i:] if i < len(file) else ""
        answer.append([head, number, tail])

    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(i) for i in answer]

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
res = ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print(solution(files) == res)
files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
res = ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
print(solution(files) == res)
