# 프로그래머스 - Lv2 - N진수 게임 - 구현, 진법 변환, 문자열 문제
"""
구현, 진법 변환, 문자열 문제

[핵심 아이디어]
    1. 0부터 시작하여 충분히 많은 숫자를 해당 진법으로 변환하여 큰 문자열을 만든다.
    2. 만들어진 문자열에서 튜브(p)의 순서에 해당하는 문자들만 t개 추출한다.
    3. 10~15는 A~F로 변환되어야 함을 고려한다.

[풀이 과정]
    1. 0부터 시작하여 N진법으로 변환된 문자열을 충분히 긴 하나의 문자열로 연결한다.
       - 각 숫자의 N진법 변환은 재귀 함수를 사용하여 구현한다.
    2. 전체 문자열에서 튜브(p)의 순서에 해당하는 문자들을 t개 추출한다.
       - 첫 번째 순서는 인덱스 p-1에서 시작하며, m명이 참여하므로 m씩 증가시킨다.
    3. 추출된 문자들을 이어 붙여 최종 결과를 반환한다.
"""

def solution(n, t, m, p):
    # N진법으로 숫자 변환하는 함수
    def convert_to_base_n(num, base):
        if num == 0:
            return '0'
        digits = "0123456789ABCDEF"
        res = ""

        while num > 0:
            res = digits[num % base] + res
            num //= base
        return res

    # 전체 게임 진행 문자열 생성
    game_str = '0'  # 0부터 시작
    num = 1

    # t*m 길이 이상의 문자열이 필요함 (최대 t*m 개의 자리가 필요)
    # 여유롭게 t*m*2 까지 생성
    while len(game_str) < t * m * 2:
        game_str += convert_to_base_n(num, n)
        num += 1

    # 튜브의 순서(p)에 해당하는 문자만 추출
    answer = ''
    for i in range(t):
        # p-1은 0-인덱스 기준으로 튜브의 첫 순서, m은 한 사이클의 길이
        idx = (p - 1) + (i * m)
        answer += game_str[idx]

    return answer

print(solution(2, 4, 2, 1) == "0111")
print(solution(16, 16, 2, 1) == "02468ACE11111111")
print(solution(16, 16, 2, 2) == "13579BDF01234567")
