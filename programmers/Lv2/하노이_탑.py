# 프로그래머스 - Lv2 - 하노이 탑 - 재귀 문제
"""
재귀 문제

[핵심 아이디어]
    1. n개의 원판을 옮기는 문제를 더 작은 문제로 분할하여 해결
    2. n개의 원판을 옮기는 과정은 다음 3단계로 구성:
       a. n-1개의 원판을 출발 기둥에서 중간 기둥으로 이동
       b. 남은 1개(가장 큰 원판)를 출발 기둥에서 목표 기둥으로 이동
       c. n-1개의 원판을 중간 기둥에서 목표 기둥으로 이동
    3. 재귀 호출을 통해 위 과정을 n=1일 때까지 반복

[풀이 과정]
    1. n=1인 경우(기저 조건): 단순히 출발 기둥에서 목표 기둥으로 원판 이동
    2. n>1인 경우:
       a. n-1개의 원판을 출발 기둥(start)에서 중간 기둥(mid)으로 이동
          (이때 목표 기둥(end)을 중간 지점으로 활용)
       b. 가장 큰 원판 1개를 출발 기둥(start)에서 목표 기둥(end)으로 이동
       c. n-1개의 원판을 중간 기둥(mid)에서 목표 기둥(end)으로 이동
          (이때 출발 기둥(start)을 중간 지점으로 활용)
    3. 모든 이동 과정을 answer 리스트에 [시작기둥, 도착기둥] 형태로 기록
"""

def solution(n):
    answer = []

    def recursive(n, start, mid, end):
        if n == 1:
            answer.append([start, end])
            return

        recursive(n - 1, start, end, mid)
        answer.append([start, end])
        recursive(n - 1, mid, start, end)

    recursive(n, 1, 2, 3)
    return answer

print(solution(2) == [[1, 2], [1, 3], [2, 3]])
