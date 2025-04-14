# 프로그래머스 - Lv1 - 공원 - 구현, 완전 탐색 문제
"""
구현, 완전 탐색 문제

[핵심 아이디어]
    1. 돗자리 크기가 큰 것부터 작은 순으로 정렬하여 가능한 가장 큰 돗자리부터 확인한다.
    2. 공원의 각 위치(i, j)에서 시작하여 정사각형 돗자리를 놓을 수 있는지 확인한다.
    3. 해당 위치에 돗자리를 놓기 위해서는 그 영역 내 모든 칸이 '-1'(빈 공간)이어야 한다.
    4. 가장 처음 찾은 가능한 돗자리의 크기가 정답이 된다.

[풀이 과정]
    1. 돗자리 크기를 내림차순으로 정렬한다.
    2. 각 돗자리 크기(k)에 대해:
       a. 공원의 모든 위치(i, j)를 순회하며 해당 위치에 k 크기의 돗자리를 놓을 수 있는지 확인한다.
       b. 확인을 위해 ck() 함수를 호출하여 (i, j)부터 시작하는 k×k 영역이 모두 '-1'인지 검사한다.
       c. 가능한 위치를 찾으면 즉시 해당 돗자리 크기를 반환한다.
    3. 모든 크기와 위치를 확인해도 돗자리를 놓을 수 없다면 -1을 반환한다.
"""

def solution(mats, park):
    answer = -1
    mats = sorted(mats, reverse=True)  # 돗자리 크기를 내림차순으로 정렬
    n, m = len(park), len(park[0])     # 공원의 크기

    def ck(x, y, num):
        # (x, y)에서 시작하는 num×num 크기의 돗자리를 놓을 수 있는지 확인하는 함수
        if x + num > n or y + num > m:  # 공원 범위를 벗어나는 경우
            return False

        for i in range(x, x + num):
            for j in range(y, y + num):
                if park[i][j] != '-1':  # 빈 공간('-1')이 아닌 경우
                    return False        # 돗자리를 놓을 수 없음

        return True  # 모든 칸이 빈 공간이면 돗자리를 놓을 수 있음

    for k in mats:  # 큰 돗자리부터 차례로 확인
        for i in range(n):
            for j in range(m):
                if park[i][j] == '-1' and ck(i, j, k):  # 빈 공간이고 돗자리를 놓을 수 있으면
                    return k  # 해당 돗자리 크기 반환

    return answer  # 돗자리를 놓을 수 없는 경우 -1 반환

mats = [5, 3, 2]
park = [["A", "A", "-1", "B", "B", "B", "B", "-1"],
        ["A", "A", "-1", "B", "B", "B", "B", "-1"],
        ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
        ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
        ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
        ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]
print(solution(mats, park))  # 3
