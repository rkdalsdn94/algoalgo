# 백준 - 실버3 - 정수 a를 k로 만들기 - 25418 - 그래프, bfs 문제
'''
그래프, bfs 문제

k의 값을 나머지 연선과, 나누기 연산을 통해서 푸는 방식이 더 속도가 빠른데, 이 방법은 잘 몰라서 bfs로 풀었다.
풀이는 다음과 같다.
 - k + 1 의 크기로 ck 배열을 만든 뒤(만들 때 0으로 초기화) * 2의 연산을 먼저 bfs로 진행한다. (숫자를 크게 만드는 방법이 속도가 더 빠름)
 - bfs를 돌기 위해 a와 현재 방문 횟수를 체크하기 위해 0을 같이 q(deque)에 담는다.
 - q에 있는 값들을 각각 curr, cnt의 이름으로 꺼내서 curr 값을 * 2, + 1을 진행한다.
    - 이때 k + 1의 범위를 벗어나지 않고, 방문하지 않았으면 방문 표시와 함께 q에 해당 값을 담아준다.
 - 이 과정을 curr의 값이 k와 같을 때까지 반복하고, 같아졌을 때 cnt의 값을 res에 담고 출력하면 된다.
'''

from collections import deque

a, k = map(int, input().split())

# 테스트
# a, k = 5, 10  # 1
# a, k = 7, 77 # 7
# a, k = 1111, 997651 # 850

q = deque([[a, 0]])
ck = [0] * (k + 1)
ck[a] = 1
res = 0

while q:
    curr, cnt = q.popleft()

    if curr == k:
        res = cnt
        break

    for nx in [curr * 2, curr + 1]:
        if 0 <= nx < k + 1 and ck[nx] != 1:
            ck[nx] = 1
            q.append([nx, cnt + 1])

print(res)
