# 백준 - 실버5 - CD - 4158 - 자료 구조(set), 이분 탐색, 투 포인터 문제
'''
자료 구조(set), 이분 탐색, 투 포인터 문제

아래 코드는 set과 비트 연산자(&) 를 활용해서 풀었는데,
다른 사람 풀이를 보면 이분 탐색과 투 포인터를 활용해서 푼 코드들이 있어 주석으로 추가해놨다.

in
    3 3
    1
    2
    3
    1
    2
    4
    0 0
out
    2
'''
import sys; input = sys.stdin.readline

while 1:
    n, m = map(int, input().split())
    
    if n == 0 and m == 0:
        break
    
    n_set = { int(input()) for _ in range(n) }
    m_set = { int(input()) for _ in range(m) }

    res = n_set & m_set
    print(len(res))

'''
이분 탐색과 투 포인터를 활용한 코드

while True:
    n,m = map(int, input().split())
    if n == 0 and m == 0:
        break

    cd1 = [int(input()) for _ in range(n)]
    cd2 = [int(input()) for _ in range(m)]

    left = 0
    right = 0
    cnt = 0

    while left < n and right < m:
        if cd1[left] == cd2[right]:
            cnt +=1
            left +=1
            right +=1
        elif cd1[left] > cd2[right]:
            right +=1
        else:
            left +=1

    print(cnt)
'''
