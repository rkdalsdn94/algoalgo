# 백준 - 골드5 - 4연산 - 14395 - 그래프, bfs 문제
'''
그래프, bfs 문제

'*', '+', '/' 과정을 q에 append 하고 ck하는 부분을 set()으로 만들면 된다.
위 과정이 0보다 크고 10 ** 9 + 1 보다 작고, set에 들어가서 검사한 값이 아니라면 while 문을 통해 반복한다.
while문이 끝나도록 프로그램이 종료되지 않으면 -1을 출력하면 된다.

생각해봐아 할 부분으론 빼기('-')가 있다.
s = s - s 를 하게 되면 값이 0이 되서 더이상 진행할 수가 없다. 즉, '-' 의 경우는 하지 않아도 된다. (이 부분 때문에 ZeroDivisionError 에러..)
또한, maximum의 범위를 10 ** 9 + 1로 해야 된다. (1 ~ 3 % 내외로 틀린다면 범위 설정을 제대로 해야 된다.)
'''

from collections import deque

s, t = map(int, input().split())

# s, t = 7, 392 # +*+
# s, t = 7, 256 # /+***
# s, t = 4, 256 # **
# s, t = 7, 7 # 0
# s, t = 7, 9 # -1
# s, t = 10, 1 # /

q = deque([(s, '')])
maximum = 10 ** 9 + 1
res = -1
ck = set([s])

if s == t:
    print(0)
    exit(0)

while q:
    a, res = q.popleft()

    if a == t:
        print(res)
        exit(0)

    nx = a * a
    if 0 <= nx < maximum and nx not in ck:
        q.append([nx, res + '*'])
        ck.add(nx)

    nx = a + a
    if 0 <= nx < maximum and nx not in ck:
        q.append([nx, res + '+'])
        ck.add(nx)

    nx = a // a
    if nx not in ck:
        q.append([nx, res + '/'])
        ck.add(nx)

print(-1)
