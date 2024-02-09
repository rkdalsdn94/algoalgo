# 백준 - 브론즈2 - 줄 세우기 - 1681 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

아래와 같이 완전 탐색으로 문제를 풀었는데 약 196ms의(PyPy3) 시간이 걸렸다.
다른 사람의 풀이는 시간이 훨씬 짧길래 봤더니, n의 범위를 % 연산자를 통해 줄이고, % 연산을 통해 얻은 값들을 list에 담은 다음에 값을 구했다.
해당 코드는 제일 아래 적어놨다.

풀이 과정
 - res의 길이가 n과 같지 않다면 while 문을 실행한다.
 - 현재 반복중인 숫자에서 l 글자가 없다면 res에 append한다.
 - res의 길이가 n과 같아진다면 마지막 인덱스 값을 출력하면 된다.
'''

n, l = map(int, input().split())

# 테스트
# n, l = 10, 1 # 22

l = str(l)
res = []
i = 0

while len(res) != n:
    i += 1
    if l not in str(i):
        res.append(i)

print(res[-1])

# 다른 사람(gracely9901)의 풀이 (시간 64ms)
'''
import sys
from collections import deque

N, L = list(map(int,sys.stdin.readline().rstrip().split()))
R = deque([])
while N:
    R.appendleft(N%9)
    N = N // 9
R = list(R)
if L != 0:
    num = [i for i in range(10)]
    num.remove(L)
    for i in R:
        print(num[i], end='')
    print('')
else:
    while True:
        ans = []
        for idx, i in enumerate(R):
            if i == 0:
                ans[idx-1] -=1
                ans.append(9)
            else:
                ans.append(i)
        if ans[0] == 0:
            ans.remove(0)
        R = ans
        if 0 not in ans:
            break
    for i in R:
        print(i, end='')
    print('')
'''
