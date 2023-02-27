# 백준 - 실버4 - 수 찾기 - 1920 - 자료 구조, 정렬, 이진 탐색 문제
'''
자료 구조(set), 정렬, 이진 탐색 문제

input
    5
    4 1 5 2 3
    5
    1 3 7 9 5
out
    1
    1
    0
    0
    1
'''

'''
이진 탐색 풀이
'''
n, n_list = int(input()), sorted(list(map(int, input().split())))
m, m_list = int(input()), list(map(int, input().split()))

for i in m_list:
    res = False
    start, end = 0, len(n_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if n_list[mid] == i:
            res = True
            break
        elif n_list[mid] > i:
            end = mid - 1
        else:
            start = mid + 1

    if res:
        print(1)
    else:
        print(0)

'''
예전에 풀었던 방식 (set 자료 구조 풀이)
# 처음에 n_list를 list 로 받았다가 시간 초과 남
# 중복 제거 위해서 set자료형 사용
'''
n = int(input())
n_list = set(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)
