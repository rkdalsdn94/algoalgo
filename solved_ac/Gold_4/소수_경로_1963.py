# 백준 - 골드4 - 소수 경로 - 1963 - 수학, 그래프, bfs, 에라토스테네스의 체 문제
'''
수학, 그래프, bfs, 에라토스테네스의 체 문제

소수를 구해놓고, bfs를 활용해서 4글자의 각 자리수를 0 ~ 9 까지 변경하면서 답을 구해가면 된다.

풀이 과정
 - 10000 까지의 범위를 가진 소수 리스트(prime_list)를 미리 만들어 놓는다. (에라토스테네스의 체를 통해)
 - q(deque)에 시작 위치인 a와 몇 번 실행했는지 숫자를 세기 위한 0(cnt)을 넣는다.
 - 방문 여부를 체크하기 위해 ck 리스트를 10_000의 크기로 만들어 주고, 시작 위치는 1로 초기화한다.
 - bfs에 q를 넣고 실행하는데, q의 값을 꺼내서 검사한다.
     - 값을 꺼낼 때 시작 위치(a)의 값이 도착 값(b)와 같으면 숫자를 세기 위해 사용했던 cnt를 return 한다.
     - 값이 다르다면, 문제에서 항상 '네 자리 소수'임을 이야기 했으므로,
       range가 4인 반복문과, 숫자는 0~9까지 이므로 range가 10인 반복문을 실행한다.
     - a의 값을 한 글자 씩 변경하고, 변경한 글자가 1000을 넘고, 방문하지 않은 곳이고, 소수이면 cnt를 1 증가시키고 q에 담는다.
     - 이 과정을 q가 빌 때까지 반복하는데, 다 반복해도 b와 같은 값이 안 된다면, -1을 return한다.
     - bfs를 실행한 값을 res에 담고, res가 -1 이면 'Impossible'을 출력하고, 나머지는 res의 값을 출력하면 된다.

in
    3
    1033 8179
    1373 8017
    1033 1033
out
    6
    7
    0
'''

from collections import deque

prime_list = [1] * 10001
for i in range(2, 100):
    if prime_list[i]:
        for j in range(i * 2, 10000, i):
            prime_list[j] = 0

def bfs(q):
    while q:
        now, cnt = q.popleft()

        if now == b:
            return cnt

        for i in range(4):
            for j in range(10):
                temp = list(str(now))
                temp[i] = str(j)
                temp = int(''.join(temp))

                if 1000 <= temp and ck[temp] == 0 and prime_list[temp] == 1:
                    ck[temp] = 1
                    q.append([temp, cnt + 1])
    return -1

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    q = deque([(a, 0)])
    ck = [0] * 10000
    ck[a] = 1
    res = bfs(q)
    print('Impossible' if res == -1 else res)
