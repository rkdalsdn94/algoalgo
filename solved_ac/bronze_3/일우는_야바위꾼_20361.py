# 백준 - 브론즈3 - 일우는 야바위꾼 - 20361 - 단순 구현, 시뮬레이션 문제
'''
단순 구현, 시뮬레이션 문제

정답으로 출력할 res 배열을 n + 1 크기로 만들고 x 위치를 1로 만들고
k_list를 통해 인덱스만 바꾸고 최종적으로 1의 인덱스 위치를 출력하면 되는 간단한 문제이다.
'''

n, x, k = map(int, input().split())
k_list = [list(map(int, input().split())) for _ in range(k)]

# n, x, k = 3, 2, 4
# k_list = [[1,3], [3,2], [3,1], [2,3]] # 1

res = [0] * (n + 1)
res[x] = 1

for i, j in k_list:
    res[i], res[j] = res[j], res[i]

print(res.index(1))
