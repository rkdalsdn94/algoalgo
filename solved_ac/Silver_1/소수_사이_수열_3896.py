# 백준 - 실버1 - 소수 사이 수열 - 3896 - 에라토스테네스의 체, 완전 탐색 문제
'''
에라토스테네스의 체, 완전 탐색 문제

에라토스테네스의 체를 이용해 입력의 최대 범위인 100000번째 소수(1299709)까지의 소수들을 구한 뒤 다음 두 과정을 진행한다.
 - 시작하려는 k가 소수면 0을 출력한다.
 - k 부터 1씩 빼면서 소수가 나올 때까지 1씩 더한다.
 - k 부터 1씩 더하면서 소수가 나올 때까지 1씩 더한다.
위 과정을 진행한 뒤 최종적으로 1을 더해 출력하면 된다.

in
    5
    10
    11
    27
    2
    492170
out
    4
    0
    6
    0
    114
'''

prime_list = [1] * (1299709 + 1)
prime_list[0], prime_list[1] = 0, 0

for i in range(1, 1299709 + 1):  # 에라토스테네의 체를 이용한 소수 구하기
    if not prime_list[i]:
        continue
    for j in range(i * i, 1299709 + 1, i):
        prime_list[j] = 0

t = int(input())
for _ in range(t):
    k = int(input())

    if prime_list[k]:
        print(0)
        continue
    left, right = k, k
    res = 1

    while 1:
        left -= 1
        if prime_list[left]:
            break
        res += 1

    while 1:
        right += 1
        if prime_list[right]:
            break
        res += 1
    print(res + 1)

