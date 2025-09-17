# 프로그래머스 - Lv2 - N-Queen - 백 트래킹 문제
"""
백 트래킹 문제

[핵심 아이디어]
    각 행에 퀸을 하나씩 배치하면서 이전에 배치된 퀸들과의 충돌 여부를 확인.
    열 충돌, 대각선 충돌을 체크하여 유효한 배치만 탐색하고 백트래킹으로 모든 경우의 수를 효율적으로 탐색.

[풀이 과정]
    1. 각 행에 대해 0번 열부터 n-1번 열까지 퀸 배치 시도
    2. 현재 위치에서 이전 행들에 배치된 퀸들과 충돌하는지 검사
       - 같은 열 충돌: 같은 col 값
       - 좌상-우하 대각선: row - col 값이 같음
       - 우상-좌하 대각선: row + col 값이 같음
    3. 충돌하지 않으면 다음 행으로 진행하여 재귀 호출
    4. n번째 행까지 성공적으로 배치하면 경우의 수 증가
"""

def solution(n):
    def is_safe(queens, row, col):
        # 현재 위치 (row, col)에 퀸을 배치할 수 있는지 확인
        for i in range(row):
            # 같은 열에 퀸이 있는지 확인
            if queens[i] == col:
                return False
            # 대각선에 퀸이 있는지 확인
            # 좌상-우하 대각선: |row차이| == |col차이|
            if abs(queens[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(queens, row):
        # 모든 행에 퀸을 배치했으면 하나의 해를 찾음
        if row == n:
            return 1

        count = 0
        # 현재 행의 각 열에 퀸 배치 시도
        for col in range(n):
            if is_safe(queens, row, col):
                queens[row] = col  # 퀸 배치
                count += backtrack(queens, row + 1)  # 다음 행으로 진행
                # 백트래킹: queens[row] 값은 자동으로 덮어씌워짐

        return count

    # queens[i] = j는 i행 j열에 퀸이 배치됨을 의미
    queens = [-1] * n
    return backtrack(queens, 0)

print(solution(4) == 2)
