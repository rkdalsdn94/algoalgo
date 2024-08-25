# 백준 - 골드2 - 가장 긴 증가하는 부분 수열 3 - 12738 - 이분 탐색, 가장 긴 증가하는 부분 수열(LIS) 문제
'''
이분 탐색, 가장 긴 증가하는 부분 수열(LIS) 문제

일반적으로 LIS를 구하는 방법으로는 dp와 이분 탐색이 있다.
이 문제에서 dp로 풀면 시간 초과가 난다. 따라서 이분 탐색을 사용해야 한다.

이분 탐색을 사용하는 방법은 다음과 같다.
1. dp 배열을 만들어서 입력받은 n_list의 첫 번째 값을 넣는다.
2. n_list의 값을 하나씩 돌면서 dp의 마지막 값보다 크다면 dp에 추가한다.
3. dp의 마지막 값보다 작다면 다음의 이분 탐색을 통해 해당 값이 들어갈 위치를 찾아서 넣는다.
    3.1. 이분 탐색을 사용할 때 left, right를 사용한다.
    3.2. left의 값이 right가 같거나 클 때까지 반복한다.
    3.3. mid를 구하고 dp[mid]가 n_list[i]보다 작다면 left = mid + 1을 해준다.
4. dp의 길이가 가장 긴 증가하는 부분 수열의 길이가 되므로 dp의 길이를 출력하면 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 6
# n_list = [10, 20, 10, 30, 20, 50] # 4

dp = [n_list[0]]
for i in range(1, n):
    if dp[-1] < n_list[i]:
        dp.append(n_list[i])
    else:
        left, right = 0, len(dp) - 1

        while left < right:
            mid = (left + right) // 2

            if dp[mid] < n_list[i]:
                left = mid + 1
            else:
                right = mid
        dp[right] = n_list[i]

print(len(dp))
