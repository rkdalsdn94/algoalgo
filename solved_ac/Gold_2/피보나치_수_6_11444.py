# 백준 - 골드2 - 피보나치 수 6 - 11444 - 분할 정복, 행렬 제곱 문제
'''
분할 정복, 행렬 제곱 문제

피보나치 수를 구하는 문제인데, 분할 정복을 사용하여 행렬 제곱 방식으로 구해야 된다.
  일반적인 피보나치 수열을 구하는 방식과 행렬 제곱을 사용한 방식의 차이
    1. 일반적인 피보나치 수열을 구하는 방식
        - 재귀함수를 사용하여 피보나치 수열을 구한다.
        - 시간 복잡도는 O(2^n)이다.
    2. 행렬 제곱을 사용한 방식
        - 분할 정복을 사용하여 행렬을 제곱하는 방식을 사용한다.
        - 시간 복잡도는 O(logN)이다.

풀이 과정
    1. 분할 정복을 사용하여 행렬을 제곱한다.
    2. 결과 출력
'''

n = int(input())

# 테스트
# n = 1000 # 517691607

MOD = 1000000007

def mul(a, b):
    res = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += a[i][k] * b[k][j]
            res[i][j] %= MOD
    return res

def pow(n):
    if n == 1:
        return [[1, 1], [1, 0]]
    elif n % 2 == 0:
        temp = pow(n // 2)
        return mul(temp, temp)
    else:
        return mul(pow(n - 1), [[1, 1], [1, 0]])

print(pow(n)[0][1])
