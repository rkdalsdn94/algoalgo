# 백준 - 실버3 - 선분 위의 점 - 11663 - 정렬, 이진 탐색 문제
'''
정렬, 이진 탐색 문제

풀이 과정
    1. n, m을 입력받는다.
    2. n_list를 입력받고 정렬한다.
    3. m_list를 입력받는다.
    4. m_list의 a, b를 이진 탐색을 통해 찾는다.
    5. a, b를 이진 탐색을 통해 찾으면 그 차이를 출력한다.
    6. a, b를 찾지 못하면 a, b가 들어갈 위치를 찾아서 차이를 출력한다.
        6.1. a, b가 들어갈 위치를 찾을 때 b가 0이면 left를 반환하고, b가 1이면 right를 반환한다.
        6.2. left, right를 찾아서 차이를 출력한다.
'''

n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))
m_list = [list(map(int, input().split())) for _ in range(m)]

# 테스트
# n, m = 5, 5
# n_list = sorted([1, 3, 10, 20, 30])
# m_list = [[1, 10], [20, 60], [3, 30], [2, 15], [4, 8]] # 3  \  2  \  4  \  2  \  0

def binary_search(a, b):
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2

        if a < n_list[mid]:
            right = mid - 1
        elif a > n_list[mid]:
            left = mid + 1
        else:
            return mid

    if b == 0:
        return left
    else:
        return right

for i, j in m_list:
    l, r = binary_search(i, 0), binary_search(j, 1)
    print(r - l + 1)
