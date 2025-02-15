# 백준 - 골드5 - 조 짜기 - 2229 - dp 문제
'''
dp 문제

[핵심 아이디어]
    1. 동적 프로그래밍을 활용하여 각 학생까지의 최적해를 순차적으로 구합니다.
    2. dp[i]는 i번째 학생까지 고려했을 때 얻을 수 있는 최대 점수를 의미합니다.
    3. 각 학생마다 이전 학생들과 새로운 조를 구성하는 모든 경우의 수를 고려합니다.
    4. 새로운 조 구성 시, 이전까지의 최적해(dp[j-1])와 현재 조의 점수(group_score)를 합산하여 최대값을 찾습니다.

[풀이 과정]
    1. dp 배열을 생성하고 첫 번째 학생의 점수를 0으로 초기화합니다.
    2. 두 번째 학생부터 시작하여 각 학생까지의 최대 점수를 계산합니다:
      - 현재 학생 i를 포함하는 모든 가능한 조합을 고려합니다.
      - j를 조의 시작점으로 하여 i까지의 학생들로 조를 구성합니다.
      - 각 조합에 대해 (최대 점수 - 최소 점수)를 계산합니다.
      - 이전까지의 최적해(dp[j-1])와 현재 조의 점수를 합산하여 최대값을 갱신합니다.
    3. 마지막 학생까지 계산이 완료되면 dp[n-1]이 전체 문제의 최적해가 됩니다.
'''

def solve_team_formation(n, scores):
    # dp[i]: i번째 학생까지 고려했을 때의 최대 점수
    dp = [0] * n

    # 첫 번째 학생은 혼자서 조를 이룰 수밖에 없으므로 0점
    dp[0] = 0

    # 두 번째 학생부터 시작
    for i in range(1, n):
        # i번째 학생까지의 최대 점수를 계산
        dp[i] = dp[i-1]  # 이전까지의 최대 점수를 기본값으로 설정

        # i번째 학생을 포함하는 새로운 조를 만들어보기
        # j는 조의 시작점
        for j in range(i, -1, -1):
            # j부터 i까지의 학생들로 조를 구성
            current_group = scores[j:i+1]
            group_score = max(current_group) - min(current_group)

            # j가 0이면 이전 점수가 없으므로 group_score만 사용
            prev_score = dp[j-1] if j > 0 else 0

            # 최대 점수 갱신
            dp[i] = max(dp[i], prev_score + group_score)

    return dp[n-1]

n = int(input())
scores = list(map(int, input().split()))

# 테스트
# n = 10
# scores = [2, 5, 7, 1, 3, 4, 8, 6, 9, 3] # 20

result = solve_team_formation(n, scores)
print(result)
