# 백준 - 실버2 - 가장 큰 증가 부분 수열 - 11055 - dp 문제
'''
dp 문제

https://pythontutor.com/visualize.html#mode=display
위의 링크에서 아래 코드를 실행하고, 값이 한 단계씩 바뀌는 과정을 보면 좀 더 이해하기 쉽다.

풀이 과정
1. input들은 잘 입력 받은 후, n_list의 값을 dp 배뎔에 깊은 복사로 복사한다.
2. 첫 번째 반복문은 1 ~ n 까지, 두 번째 반복문은 첫 번째 반복문의 반복 중인 값(i)까지 반복한다.
3. 첫 번째 반복문의 값이 두 번째 반복문의 값보다 클때만 dp[i]의 값을 아래 두 값중 더 큰 값으로 바꾼다.
    dp[i], dp[j] + n_list[i] 두 값중 더 큰 값으로 바꾸기
4. dp 리스트의 max 값을 출력한다.
'''

from copy import deepcopy

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 10
# n_list = [ 1, 100, 2, 50, 60, 3, 5, 6, 7, 8 ] # 113

dp = deepcopy(n_list)

for i in range(1, n):
    for j in range(i):
        if n_list[i] > n_list[j]:
            dp[i] = max(dp[i], dp[j] + n_list[i])

print(max(dp))