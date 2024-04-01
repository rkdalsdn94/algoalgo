# 백준 - 브론즈1 - 피보나치 수 1 - 24416 - dp 문제
'''
dp 문제

PyPy3로 제출해야 된다.

문제에서 주어진 두 가지의 피보나치를 구하는 방법에서 각각의 방법들이 몇 번 실행했는지 구하면 되는 문제이다.
문제에 있는 수도 코드를 구현하고, cnt만 잘 하면 된다.
    - 재귀를 이용할 때는 n이 1이나 2일때만 1씩 더해야 되고,
    - 반복문을 이용할 때는 반복문이 실행될 때 1씩 더해야 된다.

다른 사람의 코드를 보는데 재귀를 이용해서 푸는 방식을 피보나치를 구하는 코드로 풀고, 반복문은 단순히 n - 2를 하면 된다.
이렇게 하면 코드의 시간이 훨씬 짧다. 해당하는 코드는 파일 제일 아래 적어놓았다.
'''

n = int(input())

# n = 5 # 5 3
# n = 30 # 932040 28

res_1, res_2 = 0, 0

def fibonacci_1(n):
    global res_1

    if (n == 1 or n == 2):
        res_1 += 1
        return 1
    else:
        return fibonacci_1(n - 1) + fibonacci_1(n - 2)

def fibonacci_2(n):
    global res_2
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 1

    for i in range(3, n + 1):
        res_2 += 1
        dp[i] = dp[i - 1] + dp[i - 2]

fibonacci_1(n), fibonacci_2(n)
print(res_1, res_2)

'''
다른 사람 코드 (시간 짧은 코드, 32ms) -> 시간 복잡도가 O(N) 이면 충분하다.

n = int(input())
dp = [0, 1, 1]
for i in range(3, n + 1):
    dp.append(dp[-1] + dp[-2])
print(dp[n], n - 2)
'''
