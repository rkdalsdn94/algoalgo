'''
구현, 시뮬레이션, 그리디 문제

문제 알고리즘 분류가 더 있는거 같은데 현재 코드에선 위에 적어논 3가지로 문제를 푼거 같다.
dasom은 항상 첫번째라서 따로 input을 받고 나머지를 리스트 컴프리헨션으로 입력 받고, 역순으로 정렬한다.
역순으로 정렬된 n_list의 0번째 인덱스 값이 while문으로 dasom보다 크거나 같으면
계속 수를 비교하면서 res를 1씩 증가하면서 최종 res를 출력했다.
'''

# n = int(input())
# dasom, n_list = int(input()), sorted([ int(input()) for _ in range(n - 1) ], reverse=True)
# print(dasom, n_list)

# 테스트
n = 3
dasom, n_list = 5, sorted([7,7], reverse=True) # 2
n = 4
dasom, n_list = 10, sorted([10,10,10], reverse=True) # 1
n = 1
dasom, n_list = 1, sorted([], reverse=True) # 0
n = 5
dasom, n_list = 5, sorted([10,7,3,8], reverse=True) # 4

res = 0

if n == 1:
    print(res)
    exit()

while n_list[0] >= dasom:
    dasom += 1
    n_list[0] -= 1
    res += 1
    n_list.sort(reverse=True)

print(res)
