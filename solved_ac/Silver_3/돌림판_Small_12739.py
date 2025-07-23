# 백준 - 실버3 - 돌림판 (Small) - 12739 - 구현, 시뮬레이션 문제
"""
구현, 시뮬레이션 문제

[핵심 아이디어]
    1. 원형 구조에서 인덱스 처리를 위해 모듈로 연산 활용
    2. K번 반복하면서 모든 위치를 동시에 변환 (이전 상태 기준)
    3. 3개 색의 조합을 분석하여 다음의 변환 규칙 적용
       - 모두 같거나 모두 다르면 파랑(B)
       - 2개 같고 1개 다를 때 특정 조건에 따라 빨강(R) 또는 초록(G)

[풀이 과정]
    1. 입력받은 돌림판 정보를 리스트로 저장
    2. K번 반복하면서 다음의 과정을 진행
       - 각 위치에서 왼쪽, 중간, 오른쪽 색상 확인
       - 변환 규칙에 따라 새로운 색상 결정
       - 모든 위치의 새로운 색상을 동시에 적용
    3. 최종 상태에서 각 색상의 개수 계산 및 출력
"""

def get_new_color(left, center, right):
    """변환 규칙에 따라 새로운 색상을 반환하는 함수"""
    colors = [left, center, right]

    # 모두 같거나 모두 다른 경우 → 파랑
    if len(set(colors)) == 1 or len(set(colors)) == 3:
        return 'B'

    # 2개 같고 1개 다른 경우
    # X색이 2개, Y색이 1개인 상황 찾기
    color_count = {}
    for color in colors:
        color_count[color] = color_count.get(color, 0) + 1

    # X색 (2개)와 Y색 (1개) 찾기
    X, Y = None, None
    for color, count in color_count.items():
        if count == 2:
            X = color
        elif count == 1:
            Y = color

    # 특정 조건 만족시 빨강, 아니면 초록
    # (X=R, Y=G) 또는 (X=G, Y=B) 또는 (X=B, Y=R)
    if (X == 'R' and Y == 'G') or (X == 'G' and Y == 'B') or (X == 'B' and Y == 'R'):
        return 'R'
    else:
        return 'G'

N, K = map(int, input().split())
spinner = list(input().strip())

# 테스트
# N, K = 3, 5
# spinner = list('RGB') # 0 0 3
# N, K = 6, 3
# spinner = list('RRGGBB') # 3 3 0

for _ in range(K):
    new_spinner = [''] * N

    for i in range(N):
        # 원형 구조에서 왼쪽, 중간, 오른쪽 인덱스 계산
        left = spinner[(i - 1) % N]
        center = spinner[i]
        right = spinner[(i + 1) % N]

        # 새로운 색상 결정
        new_spinner[i] = get_new_color(left, center, right)

    # 새로운 상태로 업데이트
    spinner = new_spinner

# 각 색상의 개수 계산
red_count = spinner.count('R')
green_count = spinner.count('G')
blue_count = spinner.count('B')

print(red_count, green_count, blue_count)
