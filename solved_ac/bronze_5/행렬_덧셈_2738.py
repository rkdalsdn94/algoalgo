'''
단순 구현 문제

n으로 res 배열을 만들어 준 후에,
m만큼 반복하면서 temp리스트로 B의 행렬을 입력 받고
res를 더해주면서 풀었다.

in
    3 3
    1 1 1
    2 2 2
    0 1 0
    3 3 3
    4 4 4
    5 5 100
out
    4 4 4
    6 6 6
    5 6 100
'''
n, m = map(int, input().split())
res = [ list(map(int, input().split())) for _ in range(n) ]

for i in range(n):
    temp = list(map(int, input().split()))
    
    for j in range(m):
        res[i][j] += temp[j]

for i in range(n):
    print(*res[i])
