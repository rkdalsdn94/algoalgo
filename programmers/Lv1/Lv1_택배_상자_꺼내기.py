# 프로그래머스 - Lv1 - 택배 상자 꺼내기 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

[핵심 아이디어]
    1. 2차원 배열을 사용하여 지그재그로 쌓인 상자들의 위치를 효율적으로 표현한다.
    2. 행 번호를 이용하여 각 위치의 상자 번호를 수식으로 직접 계산한다 (row * w + i).
    3. 홀수 행의 경우 리스트를 뒤집어([::-1]) 오른쪽에서 왼쪽으로 배치한다.
    4. 목표 상자를 찾은 후에는 해당 열에서 위쪽으로 있는 상자들만 확인하면 된다.

[풀이 과정]
    1. 필요한 총 행의 개수를 계산한다 (max_row = n // w + 1).
    2. 각 행의 상자 배치:
       - 각 위치의 상자 번호를 row * w + i 수식으로 계산한다.
       - n보다 큰 번호는 0으로 처리하여 빈 공간으로 표시한다.
       - 홀수 행은 리스트를 뒤집어 반대 방향으로 배치한다.
    3. 목표 상자 탐색:
       - 2중 반복문으로 목표 상자의 위치(r, c)를 찾는다.
       - 목표 상자를 찾으면 해당 위치에서부터 위로 올라가며 확인한다.
       - 빈 공간(0)을 만나거나 마지막 행까지 도달하면 계산을 종료한다.
    4. 결과 반환:
       - 목표 상자를 포함하여 위쪽에 있는 모든 상자의 개수를 반환한다.
       - 빈 공간을 만나면 그 시점까지의 상자 개수를 반환한다.
'''

def solution(n, w, num):
    max_row = n // w + 1

    boxes = []
    for row in range(max_row):
        current_row = [row * w + i if row * w + i <= n else 0 for i in range(1, w + 1)]
        boxes.append(current_row[::-1] if row % 2 == 1 else current_row)

    for r in range(max_row):
        for c in range(w):
            if boxes[r][c] != num:
                continue

            res = 1  # 목표 상자부터 시작
            for i in range(r + 1, max_row):
                if boxes[i][c] == 0:
                    return res
                res += 1
            return res

    return 0

print(solution(22, 6, 8) == 3)
print(solution(13, 3, 6) == 4)
