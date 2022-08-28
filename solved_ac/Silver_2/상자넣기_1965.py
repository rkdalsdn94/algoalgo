'''
dp 문제

1로 초기화 한 dp 배열에서 2중 반복문으로 1 -> n까지, i -> j까지 가는 반복문을 만든 후에
검사하려는 값(j)의 값이 원본 값(i)보다 작으면 dp[i] = max(dp[i], dp[j] + 1)로 업데이트 한다.
반복문이 다 끝난 후에 dp 배열에서 제일 큰 값을 출력한다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 8
# n_list = [1, 6, 2, 5, 7, 3, 5, 6] # 5
# n = 10
# n_list = [1,2,3,4,5,6,7,8,9,10] # 10

dp = [ 1 for _ in range(n) ]

for i in range(1, n):
    for j in range(i):
        if n_list[j] < n_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
