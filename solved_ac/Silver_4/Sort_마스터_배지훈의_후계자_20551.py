# 백준 - 실버4 - Sort 마스터 배지훈의 후계자 - 20551 - 자료 구조(dict), 정렬, 이진 탐색 문제
'''
자료 구조(dict), 정렬, 이진 탐색 문제

dict를 활용한 코드의 속도가 더 빠르고, 읽기도 쉽다. 이러한 문제가 있을 때 dict을 잘 활용하면 좋을거 같다.
근데, 공부하려는 마음으로 이진 탐색으로도 풀어봤는데, 생각보다 꽤 까다로웠다.
n_list 안에서 중복된 값이 있을 경우도 생각해야 돼서 n_list[mid]가 target이랑 같다고 하더라도, end와 mid가 같을 때만 break한다.
'''

import sys; input = sys.stdin.readline

n, m = map(int, input().split())
n_list = sorted([ int(input()) for _ in range(n) ])
m_list = [int(input()) for _ in range(m)]

# 테스트
# n, m = 5, 5
# n_list = sorted([9, 0, -1, 3, 2])
# m_list = [-1, 10, 5, 9, 0] # 0  \  -1  \  -1  \  4  \  1
# n, m = 8, 4
# n_list = sorted([3, 3, 4, 9, 2, 5, 3, 4])
# m_list = [3, 10, 4, 2] # 1  \  -1  \  4  \  0

def binary_search(n_list, target):
    start, end = 0, n - 1

    while start <= end:
        mid = (start + end) // 2

        if n_list[mid] < target:
            start = mid + 1
        elif n_list[mid] > target:
            end = mid - 1
        elif n_list[mid] == target: # n_list안에서 중복된 값이 있을 경우 - 예제 2에서 3을 찾을 때를 디버깅하면 왜 필요한지 알 수 있다
            if end == mid:
                break
            end = mid

    if n_list[mid] == target:
        return mid
    return -1

for i in m_list:
    print(binary_search(n_list, i))


# dict 활용 코드
'''
import sys; input = sys.stdin.readline
n, m = map(int, input().split())
n_list = sorted([ int(input()) for _ in range(n) ])
m_list = [ int(input()) for _ in range(m) ]

# 테스트
# n, m = 5, 5
# n_list = sorted([9, 0, -1, 3, 2])
# m_list = [-1, 10, 5, 9, 0] # 0  \  -1  \  -1  \  4  \  1
# n, m = 8, 4
# n_list = sorted([3, 3, 4, 9, 2, 5, 3, 4])
# m_list = [3, 10, 4, 2] # 1  \  -1  \  4  \  0

temp_dict = dict()

for i in range(n):
    if n_list[i] not in temp_dict:
        temp_dict[n_list[i]] = i

for i in m_list:
    if i in temp_dict:
        print(temp_dict[i])
    else:
        print(-1)
'''