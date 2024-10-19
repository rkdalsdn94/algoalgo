# 백준 - 실버3 - 활자 - 1951 - 수학, 구현 문제
'''
수학, 구현 문제

풀이 과정
    1. n을 입력받는다.
    2. res 리스트와 temp를 각각 [0] * 10, 1로 초기화한다.
    3. n이 0이 될 때까지 반복문을 돌린다.
        3.1. n을 10으로 나눈 나머지를 res에 더한다.
        3.2. n을 10으로 나눈 몫을 n에 저장한다.
    4. res를 출력한다.
'''

n = int(input())

# 테스트
# n = 10 # 11
# n = 18 # 27

res = [0] * 10
temp = 1

while n:
    while n % 10 != 9:
        for i in str(n):
            res[int(i)] += temp
        n -= 1

    if n < 10:
        for i in range(n + 1):
            res[i] += temp
        res[0] -= temp
        break

    for i in range(10):
        res[i] += (n // 10 + 1) * temp
    res[0] -= temp
    temp *= 10
    n //= 10

print(sum(res) % 1234567)
