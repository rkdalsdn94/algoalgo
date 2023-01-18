# 백준 - 실버2 - 병사 배치하기 - 18353 - dp, 가장 긴 증가하는 부분 수열(lis) 문제
'''
dp, 가장 긴 증가하는 부분 수열(lis) 문제

lis 알고리즘에서 내림차순 으로만 생각한 후 n에서 해당 값을 빼면된다.
lis알고리즘을 잘 모른다면 https://chanhuiseok.github.io/posts/algo-49 여기에서 보면 도움이 된다.

이 문제는 n의 범위가 작아서 n^2 으로도 풀리지만 n의 범위가 더 크다면 이분탐색도 활용해야 된다.

병사 한 명은 제외를 해야하므로 dp를 1로 초기화 해놓은 상태에서
2중 반복문으로 i가 j보다 작을 때마다 dp의 값을 1씩 더한 값보다 더 큰 값으로 바꾸면된다.
출력할 땐 전체 병사의 수 - dp의 가장 큰 값을 빼고 출력하면 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 7
# n_list = [ 15, 11, 4, 8, 5, 2, 4 ] # 2

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if n_list[i] < n_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
