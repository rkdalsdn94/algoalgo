# 백준 - 실버3 - N과 M 4 - 15652 - 백 트래킹 문제
'''
백 트래킹 문제

기존의 n과 m 문제에서 start 부분이 필요한 백 트래킹 문제이다.

depth가 m과 같아질 때까지(종료 조건) 백 트래킹을 실행한 뒤 문제에서 나오는 비내림차순을 구현하기 위해 start 부분이 필요하다.
문제를 다 풀고 다른 사람 풀이를 참고하는데, 비내림차순을 만들 수 있는 내장 함수가 있어서 제알 아래 적어놨다. (중복을 허용한 조합)
    - 참고 : https://docs.python.org/ko/3/library/itertools.html#itertools.combinations_with_replacement
'''

n, m = map(int, input().split())

# 테스트
# n, m = 3, 1 # 1  \  2  \  3
# n, m = 4, 2
'''
out
    1 1
    1 2
    1 3
    1 4
    2 2
    2 3
    2 4
    3 3
    3 4
    4 4
'''
# n, m = 3, 3
'''
out
    1 1 1
    1 1 2
    1 1 3
    1 2 2
    1 2 3
    1 3 3
    2 2 2
    2 2 3
    2 3 3
    3 3 3
'''

res = []

def back_tracking(depth, start, arr):
    if depth == m:
        res.append(arr)
        return

    for i in range(start, n + 1):
        back_tracking(depth + 1, i, arr + [i])

back_tracking(0, 1, [])
for i in res:
    print(*i)

'''
python 내장 함수인 combinations_with_replacement 을 이용한 풀이 - 중복을 허용한 조합

from itertools import combinations_with_replacement as combiWithReplace

n, m = map(int, input().split())
arr = [str(i) for i in range(1, n + 1)]

for i in combiWithReplace(arr, m):
    print(*i)
'''

