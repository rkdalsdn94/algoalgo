'''
처음 접근을 '그리디' || '점화식을 세운 다음에 풀어야 하나?'라는 쪽으로 접근을 해서
테스트케이스들이 어느 정도 있길래 그걸 손으로 풀어보면서 생각해 보는데,
'완전 탐색 아니면 안 되겠다'라는 생각이 들었다. (예제 5번을 손으로 풀다 보면 완전 탐색 말고 답이 안 나온다)
그 생각을 한 후에 ck를 어떻게 만들까에 대한 고민을 하다가 '순열 그대로 검사하자' 라고 접근 한 뒤에 해결했다.
ㄴ> (ck를 0, 1 말고 다양하게 사용할 수 있도록 연습한 문제였다.)
'''

from collections import deque
from copy import deepcopy

n, k = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, k = 3, 3
# n_list = [3, 2, 1] # 1
# n, k = 3, 3
# n_list = [1, 2, 3] # 0
# n, k = 5, 2
# n_list = [5, 4, 3, 2, 1] # 10
# n, k = 5, 4
# n_list = [3, 2, 4, 1, 5] # -1
# n, k = 8, 4
# n_list = [7, 2, 1, 6, 8, 4, 3, 5] # 7
# n, k = 4, 2
# n_list = [1, 4, 3, 2] # 3   --> 위에 예제가 너무 커서 만들었다

ck = set()
q = deque([(n_list, 0)])
res = -1

while q:
    n_list, cnt = q.popleft()

    if n_list == sorted(n_list):
        res = cnt
        break

    for i in range(n - k + 1):
        temp = deepcopy(n_list)
        temp[i:i+k] = n_list[i:i+k][::-1]  # 여기 부분이 이해가 잘 안되면 list(n_list[i:i+k])[::-1] --> 이렇게 생각하면 된다

        if tuple(temp) not in ck:
            ck.add(tuple(temp))
            q.append((temp, cnt + 1))

print(res)

