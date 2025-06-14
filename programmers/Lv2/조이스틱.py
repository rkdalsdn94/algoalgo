# 프로그래머스 - Lv2 - 조이스틱 - 그리디 문제
"""
그리디 문제

[핵심 아이디어]
    1. 각 문자마다 'A'에서 목표 문자까지의 최소 조작 횟수를 계산 (위로 이동 vs 아래로 이동)
    2. 커서 이동 최적화: 연속된 'A' 구간을 건너뛰는 최적 경로 탐색
    3. 오른쪽으로만 이동, 왼쪽 우선 이동, 오른쪽 후 되돌아가기 등 모든 경우를 비교

[풀이 과정]
    1. 각 문자에 대해 'A'에서 해당 문자까지 위/아래 이동 중 최소 횟수 계산
    2. 커서 이동 최적화를 위해 연속된 'A' 구간 탐지
    3. 다양한 이동 패턴(순차 이동, 되돌아가기 등)을 비교하여 최소 이동 횟수 계산
    4. 알파벳 변경 횟수와 커서 이동 횟수를 합산하여 최종 답 도출
"""

def solution(name):
    answer = 0
    n = len(name)

    # 1. 각 문자마다 A에서 목표 문자까지의 최소 조작 횟수 계산
    for char in name:
        # 위로 이동하는 경우와 아래로 이동하는 경우 중 최소값
        up_move = ord(char) - ord('A')  # A에서 위로 이동
        down_move = ord('Z') - ord(char) + 1  # A에서 아래로 이동 (A->Z->Y->...->char)
        answer += min(up_move, down_move)

    # 2. 커서 이동 최적화
    min_move = n - 1  # 오른쪽으로만 이동하는 기본 경우

    for i in range(n):
        # 현재 위치 i에서 연속된 A의 끝 지점 찾기
        next_pos = i + 1
        while next_pos < n and name[next_pos] == 'A':
            next_pos += 1

        # 오른쪽으로 i만큼 이동 후 처음으로 돌아가서 왼쪽으로 이동하는 경우
        # i (오른쪽 이동) + i (돌아오기) + (n - next_pos) (왼쪽 이동)
        min_move = min(min_move, 2 * i + n - next_pos)

        # 왼쪽으로 먼저 이동한 후 오른쪽으로 이동하는 경우
        # (n - next_pos) (왼쪽 이동) + (n - next_pos) (돌아오기) + i (오른쪽 이동)
        min_move = min(min_move, 2 * (n - next_pos) + i)

    answer += min_move
    return answer

print(solution('JEROEN')) # 56
print(solution('JAN')) # 23
