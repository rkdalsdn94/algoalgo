# 백준 - 실버3 - 두 개의 배열 - 17124 - 이진 탐색, 정렬 문제
"""
이진 탐색, 정렬 문제

[핵시 아이디어]
    배열 B를 정렬한 후, 각 A[i]에 대해 이진 탐색을 사용하여 B에서 A[i]와 가장 가까운 값을 효율적으로 찾는다.
    가장 가까운 값이 여러 개일 경우 더 작은 값을 선택한다.

[풀이 과정]
    1. 배열 B를 오름차순으로 정렬한다.
    2. 각 A[i]에 대해 이진 탐색을 수행하여 B에서 A[i]와 가장 가까운 값을 찾는다.
    3. 가장 가까운 값이 여러 개일 경우 더 작은 값을 선택한다.
    4. 선택된 값들의 합을 계산하여 출력한다.

in
    3
    4 3
    20 5 14 9
    16 8 12
    3 4
    16 8 12
    20 5 14 9
    3 3
    1 2 3
    2 3 4
out
    44
    37
    7
"""

def find_closest(B, target):
    left, right = 0, len(B) - 1

    # 이진 탐색으로 target의 위치 찾기
    while left <= right:
        mid = (left + right) // 2
        if B[mid] == target:
            return target
        elif B[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # target과 가장 가까운 값 찾기
    candidates = []
    if right >= 0:
        candidates.append(B[right])
    if left < len(B):
        candidates.append(B[left])

    # 거리가 가장 작고, 같다면 값이 더 작은 것 선택
    return min(candidates, key=lambda x: (abs(target - x), x))

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    B.sort()  # 이진 탐색을 위한 정렬

    res = 0
    for a in A:
        res += find_closest(B, a)

    print(res)
