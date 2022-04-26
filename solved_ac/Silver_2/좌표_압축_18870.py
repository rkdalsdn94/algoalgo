'''
정렬, 자료구조(dict을 활용해야 된다.) 문제

처음에 시간 초과가 나와서 어디 부분이 문제 일까 싶어서 생각해보니까
res를 list말고, dict를 사용하고 원래의 n_list의 값을 키로 잡고 값을 정렬한 순서로 잡으면
훨씬 빠를거 같아서 그렇게 수정하니까 성공했다.
'''

from copy import deepcopy

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n, n_list = 5, [2, 4, -10, 4, -9] # 2 3 0 3 1
# n, n_list = 6, [1000, 999, 1000, 999, 1000, 999] # 1 0 1 0 1 0

res = []
copy_list = { j: i for i, j in enumerate(sorted(set(deepcopy(n_list)))) }

for i in n_list:
    res.append(copy_list[i])

print(*res)
