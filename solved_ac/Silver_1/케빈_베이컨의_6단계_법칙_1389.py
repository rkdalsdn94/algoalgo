'''
bfs 문제 (플로이드-와샬로도 풀 수 있는데, 아직 bfs가 더 편한거 같다...)

입력값을 딕셔너리(m_list)로 서로 연결해준다.
 -- (1, n + 1)하는 이유는 인덱스를 1부터 사용하고 싶어서 그렇게 했다. -> a, b 를 -1 씩 안해도 돼서 더 편하다
그리고 1부터 n까지 bfs로 모두 돌면서 처음 시작하는 부분을 ck로 담고 m_list에 키로 있는 값들을 모두 꺼내보면서 체크한다.
그리고 temp에 이 전의 값 + 1 씩 하면서 bfs가 끝났을 시점에 모두 더한다(sum(temp))
마지막으로 제일 작은 인덱스의 + 1 을 한 후에 출력 해준다.(인덱스는 0부터 시작이라 제출할 때는 +1을 해야 된다.)
'''

from collections import deque

n, m = map(int, input().split())
m_list = { i: [] for i in range(1, n + 1) }

for _ in range(m):
    a, b = map(int, input().split())
    m_list[a].append(b)
    m_list[b].append(a)
# print(m_list, n, m)

# 테스트
# n, m = 5, 5
# m_list = {1: [3, 4], 2: [3], 3: [1, 4, 2], 4: [1, 5, 3], 5: [4]}

res = []

def bfs(i):
    temp = [0] * (n + 1)
    ck = [i]
    q = deque([i])

    while q:
        a = q.popleft()
        
        for j in m_list[a]:
            if j not in ck:
                temp[j] = temp[a] + 1
                ck.append(j)
                q.append(j)

    return sum(temp)

for i in range(1, n + 1):
    res.append(bfs(i))

print(res.index(min(res)) + 1)
