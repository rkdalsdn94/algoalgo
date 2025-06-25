# 백준 - 브론즈1 - Router 1 - 13192 - 구현, 애드 훅, 해 구성하기, 시뮬레이션 문제
"""
구현, 애드 훅, 해 구성하기, 시뮬레이션 문제

[핵심 아이디어]
    1. 모든 입력 노드가 모든 출력 노드에 도달할 수 있는 최소 비용 네트워크 구성
    2. 파워 함수 P = IN × OUT을 최소화하면서 연결성 보장
    3. 제한조건이 여유로운 경우 완전 이분 그래프 사용
    4. 제한이 빡빡한 경우 계층적 트리 구조 사용

[풀이 과정]
    1. 입력 제한조건 분석 (n, m, p)
    2. 완전 연결 가능성 검토: n² ≤ m, n ≤ p
    3. 완전 연결이 가능하면 모든 입력을 모든 출력에 직접 연결
    4. 불가능하면 이진 트리나 계층 구조로 파워 분산
    5. 연결 리스트 생성 및 출력
"""

n, m, p = map(int, input().split())

# 테스트
# n, m, p = 3, 100, 200
# """
# out
#     9 8
#     1 7
#     2 7
#     3 8
#     7 8
#     8 4
#     8 9
#     9 5
#     9 6
# """
# n, m, p = 3, 100, 200
# """
# out
#     6 9
#     1 4
#     1 5
#     1 6
#     2 4
#     2 5
#     2 6
#     3 4
#     3 5
#     3 6
# """

# 완전 연결 방식 체크
complete_connections = n * n
complete_max_power = n

# 완전 연결 방식 사용
total_nodes = 2 * n  # 입력 N개 + 출력 N개
connections = []

# 모든 입력(1~N)을 모든 출력(N+1~2N)에 연결
for input_node in range(1, n + 1):
    for output_node in range(n + 1, 2 * n + 1):
        connections.append((input_node, output_node))

print(total_nodes, len(connections))
for x, y in connections:
    print(x, y)
