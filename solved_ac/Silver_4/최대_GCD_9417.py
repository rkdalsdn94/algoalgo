# 백준 - 실버4 - 최대 GCD - 9417 - 수학, 완전 탐색, 정수론, 유클리드 호제법 문제
'''
수학, 완전 탐색, 정수론, 유클리드 호제법 문제

파이선 math 안에 있는 gcd 함수를 이용해서 풀었다.
입력으로 들어온 값들 중 두 수씩 gcd 함수를 돌리면 되는 간단한 문제이다.
두 수씩 gcd를 돌린 값들 중 제일 큰 값을 출력하면 된다.

풀이 과정
 - 입력을 잘 받고, 두 수의 쌍 중 최대 공약수가 가장 큰 값을 출력하면 된다.

in
    3
    10 20 30 40
    7 5 12
    125 15 25
out
    20
    1
    25
'''

from math import gcd

n = int(input())
for _ in range(n):
    m_list = list(map(int, input().split()))
    res = []

    for i in range(len(m_list) - 1):
        for j in range(i + 1, len(m_list)):
            res.append(gcd(m_list[i], m_list[j]))

    print(max(res))
