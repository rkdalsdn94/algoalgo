# 백준 - 골드4 - 숨바꼭질 4 - 13913 - 그래프, bfs 문제
'''
그래프, bfs 문제

전에 풀었던 백준 - 숨바꼭질 2 (12851) 문제에서 경로만 추가하면 된다.
풀이 방식이 잘 생각이 나지 않아 다른 사람들의 코드 중 풀이만 참고했는데,
move 배열을 따로 선언한 뒤 해당 배열에 이동경로를 기록하는 부분에서 힌트를 얻었다.
따라서, move 배열을 만든 뒤, q에서 꺼내는 값(a)을 범위를 벗어나지 않고 이동한(nx) 위치에 값을 기록해놓고, 역순으로 돌아오면 된다.

https://pythontutor.com/visualize.html#mode=edit 여기 사이트에서 ck, move 와 nx 비교할 때 50 으로 바꾼 뒤
한 Next 버튼을 클릭하면서 확인해보면 쉽게 이해할 수 있다.
'''

from collections import deque

n, k = map(int, input().split())

# 테스트
# n, k = 5, 17 # 4  \  5 10 9 18 17
# n, k = 5, 17 # 4  \  5 4 8 16 17

ck = [-1] * 100_001
move = [0] * 100_001
q = deque([n])
ck[n] = 0
res = []

while q:
    a = q.popleft()

    if a == k:
        break

    for nx in [a * 2, a + 1, a - 1]:
        if 0 <= nx < 100_001 and (ck[nx] == ck[a] + 1 or ck[nx] == -1):
            ck[nx] = ck[a] + 1
            q.append(nx)
            move[nx] = a # 전의 이동했던 위치를 기록

temp = k
for _ in range(ck[k] + 1): # 이동 위치를 따라서 res 배열에 추가
    res.append(temp)
    temp = move[temp]

print(ck[k])
print(*res[::-1])
