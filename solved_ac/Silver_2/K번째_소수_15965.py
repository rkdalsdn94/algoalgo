# 백준 - 실버2 - K번째 소수 - 15965 - 수학, 소수 판정, 에라토스테네스의 체 문제
'''
수학, 소수 판정, 에라토스테네스의 체 문제

에라토스테네스의 체로 소스 리스트를 구한다. (최댓값은 10 ** 7로 잡으면 된다. 이유는 50만번 째 소수는 7368788 임)
for 문으로 0이 아닌 값들만 prime_list에 담은 후 k - 1 번재 인덱스를 출력하면 된다.

in
    1
out
    2

in
    3
out
    5
'''

K = int(input())
INF = 10 ** 7
li = [1] * INF

for i in range(2, int(INF ** 0.5) + 1):
    if li[i]:
        for j in range(i + i, INF, i):
            li[j] = 0

prime_list = [i for i in range(2, INF) if li[i]]

print(prime_list[K - 1])
