# 백준 - 브론즈1 - 암호 키 - 1816 - 수학, 완전 탐색, 정수론, 에라토스테네스의 체
'''
수학, 완전 탐색, 정수론, 에라토스테네스의 체

에라토스테네스의 체를 이용해 소수 리스트를 구한 뒤, 중간에 소수로 나누어 떨어지면 'NO' 아니면 'YES'를 출력하면 되는 문제이다.
'''

def eratosthenes(n):
    li = [0, 0] + [1] * n
    for i in range(2, n + 1):
        if li[i]:
            for j in range(2 * i, n + 1, i):
                li[j] = 0
    return li

prime_list = eratosthenes(1000000)

t = int(input())
for _ in range(t):
    n = int(input())
    flag = 1
    for i in range(2, min(1000001, int(n ** 0.5) + 1)):
        if prime_list[i] and not n % i:
            flag = 0
            break
    print('YES' if flag else 'NO')
