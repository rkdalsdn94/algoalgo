# 백준 - 브론즈3 - 주사위 게임 - 10103 - 단순 구현 문제
'''
단순 구현 문제

입력받은 두 수가 다를때 더 높은 수의 숫자를 낮게 낸 사람의 점수에서 배면 된다.
'''

n = int(input())
n_list = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n = 4
# n_list = [[5,6], [6,6], [4,3], [5,2]]

C, S = 100, 100

for i, j in n_list:
    if i > j:
        S -= i
    elif i < j:
        C -= j

print(C, S, sep='\n')
