# 백준 - 골드5 - 세 친구 - 17089 - 그래프, 완전 탐색 문제
'''
[문제 분석]
N명의 사람 중에서 세 명(A, B, C)을 선택하는데, 이들이 모두 서로 친구여야 하며
각자의 친구 수의 합(선택된 친구들 제외)이 최소가 되어야 한다.

[핵심 아이디어]
    1. 그래프에서 삼각형 찾기: 세 정점이 서로 연결된 삼각형을 찾는 문제로 해석
    2. 최적화 전략:
      - 인접 행렬을 사용하여 O(1) 시간에 친구 관계 확인
      - 각 정점의 차수(degree)가 작은 경우를 우선적으로 고려
      - 중복 검사를 방지하여 불필요한 연산 제거
    3. 친구 수 계산:
      - 각 정점의 전체 친구 수에서 선택된 두 친구를 제외
      - 세 정점의 수정된 친구 수 합이 최소가 되도록 함

[풀이 과정]
    1. 데이터 구조 준비
      - 인접 행렬: 빠른 친구 관계 확인
      - 친구 리스트: 각 사람의 친구 목록 저장
    2. 삼각형 탐색
      - 첫 번째 정점(a) 선택
      - a의 친구들 중 두 번째 정점(b) 선택
      - a의 친구들 중 세 번째 정점(c) 선택, b와 c가 친구인지 확인
    3. 친구 수 계산 및 최소값 갱신
      - 각 정점마다 전체 친구 수에서 선택된 두 친구 제외
      - 세 정점의 수정된 친구 수 합의 최소값 갱신
    4. 결과 반환
      - 조건을 만족하는 삼각형이 없으면 -1 반환
      - 있다면 최소 친구 수 합 반환

in
    5 6
    1 2
    1 3
    2 3
    2 4
    3 4
    4 5
out
    2

in
    7 4
    2 1
    3 6
    5 1
    1 7
out
    -1
'''

def solution(N, M, edges):
    # 인접 행렬로 변경하여 친구 관계 확인 속도 개선
    friends = [[False] * (N+1) for _ in range(N+1)]
    # 각 사람의 친구 목록을 저장
    friend_lists = [[] for _ in range(N+1)]

    # 친구 관계 데이터 구조 초기화
    for a, b in edges:
        friends[a][b] = friends[b][a] = True
        friend_lists[a].append(b)
        friend_lists[b].append(a)

    min_sum = float('inf')

    # 삼각형 찾기
    for a in range(1, N+1):
        if not friend_lists[a]:  # 친구가 없는 경우 스킵
            continue
        for b in friend_lists[a]:
            if b <= a:  # 중복 검사 방지
                continue
            for c in friend_lists[a]:
                if c <= b:  # 중복 검사 방지
                    continue
                if not friends[b][c]:  # b와 c가 친구가 아니면 스킵
                    continue

                # 친구 수 계산 (선택된 세 사람 제외)
                a_count = len(friend_lists[a]) - 2  # b와 c 제외
                b_count = len(friend_lists[b]) - 2  # a와 c 제외
                c_count = len(friend_lists[c]) - 2  # a와 b 제외

                min_sum = min(min_sum, a_count + b_count + c_count)

    return min_sum if min_sum != float('inf') else -1

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

print(solution(N, M, edges))
