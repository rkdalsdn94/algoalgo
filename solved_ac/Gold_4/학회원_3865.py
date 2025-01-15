# 백준 - 골드4 - 학회원 - 3865 - 그래프, 문자열, bfs, dfs, 자료 구조(집합), 파싱 문제
'''
그래프, 문자열, bfs, dfs, 자료 구조(집합), 파싱 문제

핵심 아이디어
  1. 학회와 회원 관계를 그래프 형태로 표현하되, 해시맵을 사용하여 각 학회의 회원 목록을 관리한다.
  2. BFS를 사용하여 주어진 시작 학회부터 모든 연결된 학회를 탐색하면서 실제 사람 회원을 찾는다.
  3. 중복 계산을 방지하기 위해 set 자료구조를 활용하여 고유한 회원만 카운트한다.
  4. 문자열 파싱을 통해 입력된 정보를 학회와 회원으로 정확히 분리한다.

풀이 과정
- 1. 입력 처리
    - 각 테스트 케이스의 첫 줄에서 학회 수 n을 입력받는다.
    - n개의 줄에 대해 각 줄을 콜론(:)을 기준으로 분리하여 학회 이름과 회원 목록을 구분한다.
    - 회원 목록은 마침표(.)를 제거하고 콤마(,)로 분리하여 리스트로 저장한다.
    - society_members 해시맵에 각 학회별 회원 목록을 저장한다.
- 2. 회원 탐색
    - BFS를 사용하여 첫 번째 학회부터 시작하여 연결된 모든 학회를 탐색한다.
    - visited 집합을 사용하여 이미 방문한 학회를 체크하고 순환을 방지한다.
    - 각 회원을 확인하여 다른 학회인 경우 큐에 추가하고, 실제 사람인 경우 결과 집합에 추가한다.
- 3. 결과 출력
    - 최종적으로 result 집합의 크기를 출력하여 고유한 회원 수를 계산한다.
    - 이 과정을 입력이 0이 될 때까지 반복한다.
'''

from collections import defaultdict, deque

def get_all_members(society, society_members):
    result = set()
    visited = set()
    queue = deque([society])

    while queue:
        current = queue.popleft()
        if current in visited:
            continue

        visited.add(current)

        # 현재 학회의 모든 멤버를 처리
        for member in society_members[current]:
            if member in society_members:  # 멤버가 다른 학회인 경우
                if member not in visited:
                    queue.append(member)
            else:  # 멤버가 실제 사람인 경우
                result.add(member)

    return result

while True:
    n = int(input())
    if n == 0:
        break

    society_members = {}
    first_society = None

    for _ in range(n):
        line = input().strip()
        society, members = line.split(':')
        members = members[:-1].split(',')  # 마지막 마침표 제거

        if first_society is None:
            first_society = society

        society_members[society] = members

    result = get_all_members(first_society, society_members)
    print(len(result))
