'''
구현, 완전 탐색 문제

문제 그대로 m부터, n까지의 범위 중
완전제곱수인 것의 합이랑, 그 중 최솟값을 반환하면 된다.
없을 경우 -1을 반환하면 돼서, m의 범위부터 n까지 모든 수를 검사해도 괜찮다.(최대 범위가 10000이라서)
'''

m, n = int(input()), int(input())

# 테스트
# m, n = 60, 100
# m, n = 75, 80

res = []

for i in range(m, n + 1):
    if i == int(i ** 0.5) ** 2:
        res.append(i)

if res:
    print(sum(res), min(res), sep='\n')
else:
    print(-1)
