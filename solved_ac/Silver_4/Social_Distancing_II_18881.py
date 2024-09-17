# 백준 - 실버4 - Social Distancing II - 18881 - 정렬, 스위핑 문제
'''
정렬, 스위핑 문제

소들의 위치와 감염 상태를 고려해 최소한의 초기 감염 소의 수를 찾아야 한다. 다음의 단계를 생각해보자.
    1. 입력 처리 및 정렬: 소들의 위치와 감염 상태를 입력받고 위치를 기준으로 정렬합니다.
    2. 최대 감염 반경 distance 계산: 감염 소와 건강한 소 사이의 최소 거리를 찾아 감염 반경의 최대값을 구합니다.
    3. Union-Find 초기화 및 그룹화:
        - 감염된 소들을 개별 집합으로 초기화합니다.
        - 감염된 소들 간의 거리가 distance보다 작으면 같은 집합으로 합칩니다.
    4. 최소 초기 감염 소의 수 계산:
        - 각 감염된 소의 대표 부모를 찾아 그룹의 수를 셉니다.
        - 그룹의 수는 최소 초기 감염 소의 수와 같습니다.
Union-Find를 사용한 이유는 다음과 같다.
 - 효율적인 연결성 판단: 여러 요소들의 연결 여부를 효율적으로 판단하기 위해 Union-Find 자료 구조를 사용합니다.
 - 확장성: 만약 문제의 조건이 더 복잡해지거나, 소들의 연결 관계가 더 복잡해질 경우에도 Union-Find를 사용하면 쉽게 관리할 수 있습니다.
 - 시간 복잡도 감소: 경로 압축을 통해 Union-Find의 연산은 거의 상수 시간에 수행되므로, 전체 알고리즘의 효율성을 높입니다.

풀이 과정
    1. n을 입력받는다.
    2. 소들을 입력받아 정렬한다.
    3. distance를 무한대로 초기화한다.
    4. 감염 소와 건강한 소 사이의 최소 거리를 찾는다.
    5. 감염 소들 간의 연결된 컴포넌트를 구성한다.
    6. 연결된 컴포넌트의 수를 센다.
    7. 연결된 컴포넌트의 수를 출력한다.
'''

n = int(input())
cows = sorted([list(map(int, input().split())) for _ in range(n)])

# 테스트
# n = 6
# cows = sorted([
#     [7, 1], [1, 1], [15, 1], [3, 1], [10, 0], [6, 1]
# ]) # 3

distance = float('inf')

# 감염 소와 건강한 소 사이 최소 거리 찾기
for i in range(n - 1):
    x1, s1 = cows[i]
    x2, s2 = cows[i + 1]

    if s1 != s2:
        distance = min(distance, abs(x2 - x1))

# 감염 소들 간의 연결된 컴포넌트 구성
parent = {}
def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u]) # 경로 압축(Path Compression)
    return parent[u]

def union(u, v):
    pu, pv = find(u), find(v)
    if pu != pv:
        parent[pu] = pv

sick_cows = [i for i, (x, s) in enumerate(cows) if s == 1]
for idx in sick_cows:
    parent[idx] = idx

for i in range(len(sick_cows) - 1):
    idx1, idx2 = sick_cows[i], sick_cows[i + 1]
    x1, _ = cows[idx1]
    x2, _ = cows[idx2]

    if abs(x2 - x1) < distance:
        union(idx1, idx2)

# 연결된 컴포넌트의 수 세기
res = set()
for i in sick_cows:
    res.add(find(i))

print(len(res))
