# 백준 - 브론즈2 - 영식이와 친구들 - 1592 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

index를 구하는 문제이다. 나머지는 생각나는데로 바로 구현하면 된다.
index를 구하는 방법으로는 n_list[idx]를 2로 나눴을 때 나머지가 0인지 아닌지를 확인하고,
나머지 연산자를 이용해서 idx를 구하면 된다.
'''

n, m, l = map(int, input().split())

# 테스트
# n, m, l = 5, 3, 2 # 10
# n, m, l = 4, 1, 3 # 0
# n, m, l = 10, 3, 5 # 4
# n, m, l = 15, 4, 9 # 15

ck = [0] * n
idx, res = 0, 0
n_list = [0] * n

while n_list[idx] < m - 1:
    n_list[idx] += 1
    res += 1
    idx = (idx - l) % n if n_list[idx] % 2 == 0 else (idx + l) % n

print(res)
