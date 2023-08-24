# 백준 - 브론즈1 - 소가 길을 건너간 이유 1 - 14467 - 구현 문제
'''
구현 문제

cows를 초기화할 때 0으로 하면 안된다. 입력으로 들어올 때 길의 왼쪽은 0으로 들어오기 때문에 값이 달라질 수 있다.
따라서, cows를 -1로 초기화 해야 된다.

소의 현재 위치를 저장해두고, 입력받은 n_list의 값이 전의 값과 다르다면 res를 1씩 증가시키면 된다.
단, 처음 입력은 제외시키기 위해 -1을 따로 분기 처리했다.
'''

n = int(input())
n_list = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n = 8
# n_list = [[3, 1], [3, 0], [6, 0], [2, 1], [4, 1], [3, 0], [4, 0], [3, 1]] # 3

res = 0
cows = [-1] * 11

for i, j in n_list:
    if cows[i] == -1:
        cows[i] = j
    elif cows[i] != j:
        cows[i] = j
        res += 1

print(res)
