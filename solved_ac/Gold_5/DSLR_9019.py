'''
BFS, 구현 문제

n의 네 자릿수를 d1, d2, d3, d4라고 하자(즉 n = ((d1 × 10 + d2) × 10 + d3) × 10 + d4라고 하자)

D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.

위에 D S L R을 각 각 조건으로 만들어서(bfs 함수 안)
처음 입력받았을 때 spilt한 값(d)이랑 같으면 retrun 하면 된다.
pypy3로 제출해야 통과할 수 있다. (python3는 시간 초과 나온다)

코드가 길어져서 각 코드마다 주석을 다는게 읽기 더 편할거 같다.
'''

from collections import deque

def bfs(a):
    q = deque([(a, '')])
    ck = [0] * 10000
    ck[a] = 1

    while q:
        a, d = q.popleft()
        if a == b: # 탈출 조건
            return d

        if 2 * a <= 9999 and ck[2 * a] == 0: # 이 조건이 맞으면 D 추가
            ck[2 * a] = 1
            q.append((2 * a, d + 'D'))

        if 2 * a > 9999 and ck[(2 * a) % 10000] == 0: # 이 조건이 맞으면 D 추가
            ck[(2 * a) % 10000] = 1
            q.append([(2 * a) % 10000, d + 'D'])

        if a - 1 >= 0 and ck[a - 1] == 0: # 이 조건이 맞으면 S 추가
            ck[a - 1] = 1
            q.append((a - 1, d + 'S'))
        
        if a - 1 < 0 and ck[9999] == 0: # 이 조건이 맞으면 S 추가
            ck[9999] = 1
            q.append((9999, d + 'S'))

        temp = int((a % 1000) * 10 + a / 1000) # 이 조건이 맞으면 L 추가
        if ck[temp] == 0:
            ck[temp] = 1
            q.append((temp, d + 'L'))

        temp = int((a % 10) * 1000 + a / 10) # 이 조건이 맞으면 R 추가
        if ck[temp] == 0:
            ck[temp] = 1
            q.append((temp, d + 'R'))

t = int(input())
for _ in range(t):
    global b
    a, b = map(int, input().split())

    print(bfs(a))
