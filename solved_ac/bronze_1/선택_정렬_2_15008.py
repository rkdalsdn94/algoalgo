# 백준 - 브론즈1 - 선택 정렬 2 - 23882 - 구현, 정렬 문제
"""
구현, 정렬 문제
 - PyPy3로 제출해야 됨

[핵심 아이디어]
    1. 선택 정렬을 구현하되, 교환이 발생할 때마다 카운트
    2. K번째 교환이 발생한 직후의 배열 상태를 출력
    3. 총 교환 횟수가 K보다 작으면 -1 출력

[풀이 과정]
    1. 배열의 마지막 인덱스부터 시작하여 역순으로 진행
    2. 현재 범위(0부터 i까지)에서 최댓값의 인덱스를 찾음
    3. 최댓값이 마지막 위치(i)가 아니라면 교환 수행 및 교환 횟수 증가
    4. K번째 교환 발생 시 현재 배열 상태 출력 후 종료
    5. 모든 정렬이 끝났는데 K번째 교환이 발생하지 않았다면 -1 출력
"""

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 테스트
# n, k = 5, 2
# arr = [3, 1, 2, 5, 4] # 2 1 3 4 5
# n, k = 5, 4
# arr = [3, 1, 2, 5, 4] # -1

swap_count = 0

for i in range(n-1, 0, -1):
    # 최댓값 찾기
    max_idx = 0
    for j in range(1, i+1):
        if arr[j] > arr[max_idx]:
            max_idx = j

    # 교환이 필요한 경우
    if max_idx != i:
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        swap_count += 1

        # K번째 교환인지 확인
        if swap_count == k:
            print(*arr)
            break
else:
    print(-1)
