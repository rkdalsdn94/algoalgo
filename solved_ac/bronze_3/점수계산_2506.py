# 백준 - 브론즈3 - 점수계산 - 2506 - 단순 구현
'''
단순 구현 문제

반복문으로 n_list의 현재 값이랑 이전 값이 0이 아니면 n_list의 현재 값을 + 1했다.
그리고 n_list를 다 더한 값을 출력하면 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# n = 10
# n_list = [1,0,1,1,1,0,0,1,1,0] # 10

for i in range(1, n):
    if n_list[i - 1] != 0 and n_list[i] != 0:
        n_list[i] = n_list[i - 1] + 1

print(sum(n_list))