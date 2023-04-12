# 백준 - 브론즈2 - 바구니 뒤집기 - 10811 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

리스트 슬라이싱을 이용해서 문제를 풀었다.
'''

n, m = map(int, input().split())
n_list = [ i for i in range(1, n + 1) ]
m_list = [ list(map(int, input().split())) for _ in range(m) ]

# 테스트
# n, m = 5, 4
# n_list = [1,2,3,4,5]
# m_list = [[1, 2], [3, 4], [1, 4], [2, 2]] # 3 4 1 2 5

for i, j in m_list:
    n_list = n_list[:i - 1] + n_list[i - 1:j][::-1] + n_list[j:]

print(*n_list)
