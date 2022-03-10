'''
시뮬레이션, bfs
처음에 ck 변수를 전역으로 둬서 틀렸습니다가 나왔었다.
어디가 틀린지 고민하다 ck의 위치를 bfs함수 안으로 옮기니까 해결 되었다.

전체적인 풀이 과정은
문제의 조건이 앞자리가 0이 아니고, i < j 일 때 자리를 교환 가능하다고 한다
i < j는 combination으로 모든 교환 가능한 인덱스 값을 찾고, 하나 씩 교환 해보면서
max값을 갱신한다. 반복문 내에 '0'을 만났을 때에는 무시할 수 있는 조건을 추가하면 된다.

그래서 최종 반환값이 존재할때는 그 반환값을 출력하고, 아닐땐 -1로 출력한다.
'''

from collections import deque
from copy import deepcopy
from itertools import combinations

# n, k = map(int, input().split())

# 테스트
# n, k = 16375, 1 # 76315
# n, k = 132, 3 # 312
# n, k = 432, 1 # 423
# n, k = 90, 4 # -1
# n, k = 5, 2 # -1
n, k = 436659, 2 # 966354

combi = list(combinations(range(len(str(n))), 2))
q = deque([(n)])
res = 0

def bfs():
    ck = set()
    max_num = 0

    for _ in range(len(q)):
        a = list(str(q.popleft()))
    
        for i, j in combi:
            temp = deepcopy(a)
            temp[i], temp[j] = temp[j], temp[i]

            if temp[0] == '0':
                continue

            max_num = max(max_num, int(''.join(temp)))

            if max_num not in ck:
                ck.add(max_num)
                q.append(max_num)

    return max_num

while k:
    res = bfs()
    k -= 1

if res: print(res)
else: print(-1)
