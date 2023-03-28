# 백준 - 브론즈2 - 공 바꾸기 - 10813 - 단순 구현, 시뮬레이션 문제
'''
단순 구현, 시뮬레이션 문제

단순한 구현 문제이다. swap_position에 있는 값들을 res list에서 인덱스 위치를 서로 바꾸면 된다.
'''

n, m = map(int, input().split())
swap_position = [ list(map(int, input().split())) for _ in range(m) ]

# 테스트
# n, m = 5, 4
# swap_position = [ [1,2], [3,4], [1,4], [2,2] ] # 3 1 4 2 5

res = [ i for i in range(1, n + 1) ]

for i, j in swap_position:
    res[i - 1], res[j - 1] = res[j - 1], res[i - 1]

print(*res)
