# 백준 - 실버1 - 떡 먹는 호랑이 - 2502 - dp, 완전 탐색 문제
'''
dp, 완전 탐색 문제

나이브하게 입력으로 들어올 수 있는 모든 범위를 검사 하는 방식으로 풀었다.
시간 초과가 날거라고 생각하고 제출한 다음 리팩토링을 진행하려고 했는데, 코드가 통과해버려 수정하지 않았다.
다른 사람 풀이에 시간이 되게 효율적인 코드가 있길래 아래 적어놓았다. -> 내 코드는 1292ms 나 걸린다....
'''

d, k = map(int, input().split())

# 테스트
# d, k = 6, 41 # 2  \  7
# d, k = 7, 218 # 10  \  21

for x in range(1, 31):
    for y in range(x, k + 1):
        dp = [0] * (d + 1)
        dp[1], dp[2] = x, y

        for z in range(3, d + 1):
            dp[z] = dp[z - 1] + dp[z - 2]

        if dp[d] == k:
            print(dp[1], dp[2], sep='\n')
            exit(0)

'''
# 32ms 걸린 다른 사람 코드

d, k = map(int, input().split())

a = 1
b = 1
for _ in range(d-3): # -> 이 부분을 a, b = b, a + b 이렇게 하는게 좀 더 파이썬스러울 거 같다.
    temp = b
    b = a + b
    a = temp

for i in range(1, k//a):
    if (k - a*i) % b != 0:
        continue
    else:
        temp = k - a*i
        print(i)
        print(temp//b)
        break
'''