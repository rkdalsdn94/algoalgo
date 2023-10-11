# 백준 - 실버5 - 귀찮음 - 16208 - 수학, 그리디, 정렬 문제
'''
수학, 그리디, 정렬 문제

solved.ac 사이트 기준으론 문제 분류가 정렬이 포함되어 있지만, 정렬을 안해도 된다.

풀이 과정
    1. n_list 전체의 합을 구한다.
    2. 전체 합에서 n_list의 인덱스 값을 하나씩 빼고, 해당 값을 n_list와 곱한다.
        (x+y)인 막대를 자를 때 x * y 의 비용이 들어가기 때문에
'''

n = int(input())
n_list = list(map(int, input().split()))

# n = 4
# n_list = [3, 5, 4, 2] # 71
# n = 10
# n_list = [12, 43, 22, 51, 2, 55, 8, 21, 98, 50] # 55164

total = sum(n_list)
res = 0
for i in range(n - 1):
    total -= n_list[i]
    res += total * n_list[i]

print(res)
