'''
항상 풀던대로 
n 을 입력받고 그 후에 바로 n_list를 만들어서 풀다가(아래코드 처럼)
[
    n = int(input())
    n_list = [ list(map(int, input().split())) ]
]
위처럼 하니까 메모리 초과가 나온다 그래서
n만큼 돌면서 n_list를 받으니까 문제가 해결되었다.
요구 사항을 보니까 n_list의 범위가 엄청 크다.. 메모리 초과가 날 수 있는 상황이였다

in
    4
    10 1 2 3 1 2 3 1 2 3 1
    5 1 1 1 2 2
    6 10 10 2 10 10 2
    6 1 1 1 2 2 2
out
    SYJKGW
    1
    10
    SYJKGW
'''

from collections import Counter

n = int(input())

for i in range(n):
    n_list = list(map(int, input().split()))
    temp = n_list.pop(0)
    cnt_ck = dict(Counter(n_list).most_common(1))

    for j, k in cnt_ck.items():
        if k > temp // 2: print(j)
        else: print('SYJKGW')
