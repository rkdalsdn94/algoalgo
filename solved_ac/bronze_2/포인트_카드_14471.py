'''
    처음에 브론즈 2 여서 별 생각을 안했는데.. 문제를 이해하는데 생각보다 시간이 걸렸다
    문제를 이해하면 구현은 쉬웠다.

in
    4 5
    1 7
    6 2
    3 5
    4 4
    0 8
out
    4
in
    5 4
    5 5
    8 2
    3 7
    8 2
out
    0
'''

def solution(n, m):
    res = 0
    temp = []

    for _ in range(m):
        a, _ = map(int, input().split())
        if a >= n: res += 1
        else: temp.append((n-a))
        
    temp.sort()
    if res >= m - 1: return 0
    else: return sum(temp[:m-res-1])

n, m = map(int, input().split())

print(solution(n, m))

