# 백준 - 평범한 배낭 - 12865 - 골드5 - dp, 배낭(knapsack) 문제
'''
dp, 배낭(knapsack) 문제

knapsack 알고리즘을 잘 모른다면 https://kbs77.tistory.com/9 여기에서 공부하면 좋다.

혹시, 1차원 배열로 푸는 중에 97%에서 에러가 나면 'j - n_list[i][0] >= 0' 조건을 생각해보면 좋을거 같다.
2차원 배열로 풀면 단순하게 풀 수 있다. 해당 코드는 제일 아래에 있다.

풀이 과정
1. input 값 들을 잘 입력받은 후, 정답을 출력한 dp 배열을 최대 무게(k)의 + 1한 값으로 만들어 준다.
2. 배낭의 수 만큼 반복문을 진행하고, 해당 반복문 안에서 최대 무게부터 시작해서 0까지 - 1 하면서 2중 반복문을 실행한다.
    2.1. 현재 반복중인 배낭의 무게(n_list[i][0])가 최대 무게를 1씩 줄여(j)가면서 1씩 줄여가는 최대 무게에서 배낭에 든 무게를 뺐을 때 0보다 크거나 같다면
        2.1.1. dp[j]를 dp[j] 와  dp[j - 현재 반복중인 배낭의 무게] + 현재 반복중인 배낭의 가치를 갱신해준다.
        2.1.2. 'j - n_list[i][0]'이 0보다 적거나, n_list[i][0]가 j보다 크다면 다음 배낭을 검사한다.
3. dp의 가장 큰 값을 출력한다. -> max(dp)로 해도 되고, dp[k] 로 해도 된다.
'''

n, k = map(int, input().split())
n_list = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n, k = 4, 7
# n_list = [ [6, 13], [4, 8], [3, 6], [5, 12] ] # 14
# n, k = 5, 10
# n_list = [ [3, 8], [4, 7], [1, 9], [5, 6], [2, 1] ] # 25
# n, k = 1, 2
# n_list = [ [1, 1] ] # 1
# n, k = 6, 304
# n_list = [[99, 98],[4, 4],[6,6],[100,100],[101,101],[103,103]] # 304

dp = [0] * (k + 1)

for i in range(n):
    for j in range(k, 0, -1):
        if n_list[i][0] <= j and j - n_list[i][0] >= 0:
            dp[j] = max(dp[j], dp[j - n_list[i][0]] + n_list[i][1])
        else:
            break

# print(max(dp))
print(dp[k])



'''
2차원 배열로 풀기
n, k를 주어진 그대로 사용하기 위해 각 배열을 1씩 크게 잡았다. (n_list는 insert를 통해 [0,0]을 추가했다.)

n, k = map(int, input().split())
n_list = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n, k = 4, 7
# n_list = [ [6, 13], [4, 8], [3, 6], [5, 12] ] # 14

n_list.insert(0, [0, 0])
dp = [ [0] * (k + 1) for _ in range(n + 1) ]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j < n_list[i][0]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - n_list[i][0]] + n_list[i][1])

print(dp[n][k])
'''