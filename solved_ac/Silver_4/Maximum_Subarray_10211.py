# 백준 - Maximum Subarray - 10211 - 실버4 - dp, 누적 합, 완전 탐색 문제
'''
dp, 누적 합, 완전 탐색 문제

n의 범위가 크지 않아 다른 알고리즘을 사용하지 않고 누적합을 완전 탐색으로 구할 수 있다.

풀이 과정
1. input값 들을 잘 입력받는다.
2. 출력할 때 사용하기 위해 dp 리스트를 n의 크기만큼 0으로 초기화 해준다.
3. 반복문을 1부터 시작하기 위해 dp[0]의 값을 input으로 받은 n_list[0]의 값으로 바꿔준다.
4. 1부터 n까지 반복문을 실행한다.
    4.1 dp[i]를 아래 세 값 중 제일 큰 값을 더해준다.(max)
                n_list[i - 1] + n_list[i]
                n_list[i]
                dp[i - 1] + n_list[i]
5. dp배열에서 제일 큰 값을 출력한다.(max)

in
    2
    5
    1 2 3 4 5
    5
    2 1 -2 3 -5
out
    15
    4
'''

t = int(input())

for _ in range(t):
    n = int(input())
    n_list = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = n_list[0]

    for i in range(1, n):
        dp[i] += max(n_list[i - 1] + n_list[i], n_list[i], dp[i - 1] + n_list[i])

    print(max(dp))