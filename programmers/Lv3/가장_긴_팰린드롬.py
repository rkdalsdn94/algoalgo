# 프로그래머스 - Lv3 - 가장 긴 팰린드롬 - 문자열, 팰린드롬 문제
"""
문자열, 팰린드롬 문제

[핵심 아이디어]
    각 위치를 중심으로 좌우로 확장하며 팰린드롬을 찾는 중앙 확장법 사용.
    팰린드롬은 홀수 길이(중심 1개)와 짝수 길이(중심 2개) 두 가지 형태가 있으므로
    각 위치에서 두 경우를 모두 확인하여 최대 길이를 찾는다.

[풀이 과정]
    1. 문자열의 각 인덱스를 순회하며 중심점으로 설정
    2. 홀수 길이 팰린드롬: (i, i)를 중심으로 확장
    3. 짝수 길이 팰린드롬: (i, i+1)을 중심으로 확장
    4. 각 확장 함수는 중심에서 양쪽으로 퍼져나가며 대칭 확인
    5. 최대 팰린드롬 길이를 지속적으로 갱신하여 반환
"""

def solution(s):
    def expand_around_center(left, right):
        """
        주어진 중심(left, right)에서 양쪽으로 확장하며
        팰린드롬의 길이를 반환
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # while 종료 시 left와 right는 팰린드롬 범위를 벗어난 상태
        # 실제 팰린드롬 길이는 (right - 1) - (left + 1) + 1 = right - left - 1
        return right - left - 1

    max_length = 0

    # 각 위치를 중심으로 팰린드롬 탐색
    for i in range(len(s)):
        # 홀수 길이 팰린드롬 (중심이 한 문자)
        # 예: "aba" - 'b'를 중심으로
        odd_length = expand_around_center(i, i)

        # 짝수 길이 팰린드롬 (중심이 두 문자 사이)
        # 예: "abba" - 'bb' 사이를 중심으로
        even_length = expand_around_center(i, i + 1)

        # 현재 위치에서 찾은 가장 긴 팰린드롬 길이
        current_max = max(odd_length, even_length)
        max_length = max(max_length, current_max)

    return max_length

print(solution('abcdcba') == 7)
print(solution('abacde') == 3)
