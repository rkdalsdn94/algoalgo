# 백준 - 실버1 - 골드바흐의 추측 - 6588 - 수학, 소수 판정, 에라토스테네스의 체 문제
'''
수학, 소수 판정, 에라토스테네스의 체 문제

PyPy3로 제출해야 시간 초과가 안난다.

미리 n의 최대 범위까지 각 수의 배수를 에라토스테네스의 체 방식으로 구해놓은 다음
n을 일력 받았을 때 3부터 시작해서 i번 째의 값과, n - i의 값이 true이면 두 값을 출력하면 된다.
반복문이 다 끝나도록 true가 없으면 "Goldbach's conjecture is wrong."를 출력하면 되는데, 사실 출력될 일은 없다.

in
    8
    20
    42
    0
out
    8 = 3 + 5
    20 = 3 + 17
    42 = 5 + 37
'''

import sys; input = sys.stdin.readline

sieve_of_eratosthenes = [1] * 1000001
for i in range(2, 1001):
    if sieve_of_eratosthenes[i]:
        for j in range(i + i, 1000001, i):
            sieve_of_eratosthenes[j] = 0

while 1:
    n = int(input())
    flag = True

    if n == 0:
        break

    for i in range(3, len(sieve_of_eratosthenes)):
        if sieve_of_eratosthenes[i] and sieve_of_eratosthenes[n - i]:
            print(f'{n} = {i} + {n - i}')
            flag = False
            break
    
    if flag:
        print("Goldbach's conjecture is wrong.")
