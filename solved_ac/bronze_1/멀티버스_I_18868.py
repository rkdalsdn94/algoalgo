# 백준 - 브론즈1 - 멀티버스 I - 18868 - 완전 탐색 문제
'''
완전 탐색 문제

행성의 크기가 같은지 검사하면 되는 문제이다. (인덱스의 값을 검사하는 것이 아니라 크기 순으로 검사해야 된다.)
n과 m을 반대로 했다.

풀이 과정
 1. 입력을 받는다. (n : 우주의 개수, m : 행성의 개수)
 2. n_list에 행성의 차원 수를 받는다.
 3. n_list를 정렬한 후, 각 행성의 차원 수를 정렬한 인덱스 순서 리스트를 만든다.
 4. 만약 두 행성의 차원 수가 같다면 res를 1 더한다.
 5. res를 출력한다.
'''

n, m = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]

# n, m = 2, 3
# n_list = [[1, 3, 2], [12, 50, 31]] # 1
# n, m = 2, 3
# n_list = [[1, 3, 2], [12, 50, 10]] # 0
# n, m = 5, 3
# n_list = [[20, 10, 30], [10, 20, 60], [80, 25, 79], [30, 50, 80], [80, 25, 81]] # 2

res = 0

for i in range(n):
    arr_sort = sorted(n_list[i])
    idx = []

    for j in n_list[i]: # 크기 순으로 인덱스 순서 리스트 만들기
        idx.append(arr_sort.index(j) + 1)
    n_list[i] = idx

for i in range(n - 1):
    for j in range(i + 1, n):
        if n_list[i] == n_list[j]: # 우주끼리 리스트 순서가 같으면 res를 1 더하면 된다.
            res += 1

print(res)
