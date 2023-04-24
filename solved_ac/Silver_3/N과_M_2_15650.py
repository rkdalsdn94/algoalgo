# 백준 - 실버3 - N과 M (2) - 15650 - 백 트래킹 문제
'''
백 트래킹 문제

파이썬에서 itertools의 combinations를 이용해서도 풀 수 있지만, 백 트래킹을 공부하고 싶어서 백 트래킹 방식으로 풀었다.
파일 제일 아래 combinations를 활용한 풀이도 적어놓았다.
풀이 과정은 recursive라는 재귀 함수를 통해서 res의 길이가 m과 같을 때 res를 출력 하면 된다.
res의 길이가 m과 다를시 res에 값을 추가한 뒤, recursive 함수를 반복하면 된다.
'''

n, m = map(int, input().split())

# 테스트
# n, m = 3, 1 # 1  \  2  \  3
# n, m = 4, 2 # 1 2  \  1 3  \  1 4  \  2 3  \  2 4  \  3 4
# n, m = 4, 4 # 1 2 3 4

res = []

def recursive(x):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    
    for i in range(x, n + 1): # (1, 2)를 사용했을 경우 (2, 1)도 사용하지 못 하게 하기 위해서 x부터 시작해야 된다.
        res.append(i)
        recursive(i + 1)
        res.pop()

recursive(1)

'''
combination 내장 함수 활용

permutations는 중복된 값을 허용해서 'N과 M (1)' 문제에선 활용할 수 있는데, 이 문제(N과 M 2)에서는 사용할 수 없다.
---즉, (1, 2)를 사용했을 경우 (2, 1)을 사용하면 안 된다. ---
'''

from itertools import combinations

n, m = map(int, input().split())
temp = [ i for i in range(1, n + 1) ]

for i in combinations(temp, m):
    print(*i)
