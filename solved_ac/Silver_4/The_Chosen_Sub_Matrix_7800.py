# 백준 - 실버4 - The Chosen Sub Matrix - 7800 - 구현, 완전 탐색, 자료 구조(해시), 정렬 문제
"""
구현, 완전 탐색, 자료 구조(해시), 정렬 문제

input을 EOF까지 받는 문제이다. 따라서 while True: try: except EOFError: break 형태로 입력을 받아야 한다.

[핵심 아이디어]
    1. N x N 행렬에서 모든 가능한 M x M 부분 행렬을 추출한다.
    2. 각 부분 행렬의 서로 다른 원소의 개수를 계산한다.
    3. 우선순위 기준에 따라 최적의 부분 행렬을 선택한다:
       - 1순위: 서로 다른 원소의 개수가 가장 적은 것
       - 2순위: 원소들을 내림차순 정렬했을 때 사전순으로 가장 큰 것
       - 3순위: 행 인덱스가 가장 작은 것
       - 4순위: 열 인덱스가 가장 작은 것

[풀이 과정]
    1. EOF까지 여러 테스트 케이스를 입력받는다.
    2. 각 테스트 케이스마다 모든 가능한 M x M 부분 행렬을 순회한다.
    3. 각 부분 행렬의 서로 다른 원소를 set으로 구하고 개수를 계산한다.
    4. 서로 다른 원소들을 내림차순으로 정렬한다.
    5. 정렬 키를 만들어 우선순위에 따라 정렬한다.
    6. 가장 우선순위가 높은 부분 행렬의 위치를 출력한다.
"""

def find_best_submatrix(n, m, matrix):
    candidates = []

    # 모든 가능한 M x M 부분 행렬을 순회
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            # 부분 행렬 추출
            submatrix = [row[j:j + m] for row in matrix[i:i + m]]

            # 서로 다른 원소 찾기
            unique_elements = set()
            for row in submatrix:
                for element in row:
                    unique_elements.add(element)

            # 서로 다른 원소의 개수
            distinct_count = len(unique_elements)

            # 서로 다른 원소들을 내림차순으로 정렬
            sorted_elements = sorted(unique_elements, reverse=True)

            # 정렬 키 생성
            sort_key = (distinct_count, [-x for x in sorted_elements], i, j)
            candidates.append((sort_key, i + 1, j + 1)) # 1-based 인덱스로 저장

    # 우선순위에 따라 정렬
    candidates.sort()

    # 가장 우선순위가 높은 부분 행렬의 위치 반환
    return candidates[0][1], candidates[0][2]

# 테스트
# n1, m1 = 4, 3
# n1_list = [[3, 9, 9, 9], [3, 9, 9, 2], [3, 9, 9, 2], [2, 5, 5, 2]]  # 1 1
# n2, m2 = 10, 2
# n2_list = [
#     [1, 5, 7, 8, 2, 3, 3, 3, 1, 7],
#     [2, 2, 3, 6, 3, 7, 3, 2, 3, 1],
#     [5, 9, 3, 5, 7, 0, 4, 6, 9, 1],
#     [1, 0, 3, 4, 2, 6, 4, 3, 9, 0],
#     [7, 4, 9, 9, 5, 4, 6, 2, 1, 5],
#     [5, 6, 9, 9, 6, 6, 3, 8, 0, 8],
#     [4, 3, 3, 5, 2, 1, 7, 6, 4, 1],
#     [6, 5, 9, 5, 0, 3, 1, 8, 8, 6],
#     [2, 2, 2, 8, 0, 1, 3, 5, 9, 0],
#     [3, 6, 4, 2, 3, 3, 0, 2, 0, 0]
# ] # 5 3
# result1 = find_best_submatrix(n1, m1, n1_list)
# print(f"{result1[0]} {result1[1]}")
# result2 = find_best_submatrix(n2, m2, n2_list)
# print(f"{result2[0]} {result2[1]}")

while True:
    try:
        n, m = map(int, input().split())
        matrix = [list(map(int, input().split())) for _ in range(n)]

        result = find_best_submatrix(n, m, matrix)
        print(f"{result[0]} {result[1]}")

    except EOFError:
        break
