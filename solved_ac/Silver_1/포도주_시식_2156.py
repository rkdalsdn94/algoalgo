'''
처음에 함수로 안하고 생각없이 조건만 단 상태에서 print를 했었는데,
조건이 일치한 후에도 나머지 print를 찍게돼서 함수로 return하는 방식으로 수정했다.
dp식은 문제에서 주어진 조건 그대로 생각하면서 만들었다.

근데 코드를 너무 지저분하게 만든거 같아서 다음에 수정 해야겠다.....
'''

n = int(input())
n_list = [ int(input()) for _ in range(n) ]

# 테스트
# n = 6
# n_list = [6, 10, 13, 9, 8, 1] # 33

dp = [0] * n
dp[0] = n_list[0]

def solution(dp, n_list, n):
    if n > 1:
        if n > 2:
            dp[1] = n_list[0] + n_list[1]
            dp[2] = max(n_list[2] + n_list[0], n_list[2] + n_list[1], dp[1])

            for i in range(3, n):
                dp[i] = max(n_list[i] + dp[i-2], n_list[i-1] + dp[i-3] + n_list[i], dp[i-1])

            return max(dp)

        return n_list[0] + n_list[1]

    return max(n_list)

print(solution(dp, n_list, n))