# 백준 - 브론즈2 - 서강의 역사를 찾아서 - 25177 - 구현
"""
구현 문제

[핵심 아이디어]
    각 장소에서 예전 시설과 현재 시설의 점수 차이를 계산하고, 그 중 가장 큰 양수 차이값을 찾는다.
    만약 모든 차이가 0 이하라면 아무것도 바꾸지 않는 것이 최적이므로 0을 반환한다.

[풀이 과정]
1. 현재 시설 점수 배열과 예전 시설 점수 배열을 입력받는다.
    2. 두 배열의 길이가 다를 수 있으므로, 짧은 배열을 0으로 패딩하여 길이를 맞춘다.
    3. 각 위치 i에서 (예전 점수 - 현재 점수)를 계산한다.
    4. 이 차이값들 중 최댓값을 구한다. 단, 음수는 의미가 없으므로 0과 비교하여 더 큰 값을 선택한다.
"""

n, m = map(int, input().split())
current_scores = list(map(int, input().split()))
past_scores = list(map(int, input().split()))

# 두 배열의 길이를 max(n, m)으로 맞추기 (짧은 배열을 0으로 패딩)
max_length = max(n, m)
current_scores.extend([0] * (max_length - n))
past_scores.extend([0] * (max_length - m))

# 각 위치에서 점수 증가량을 계산하고 최댓값 찾기
max_increase = 0
for i in range(max_length):
    score_increase = past_scores[i] - current_scores[i]
    max_increase = max(max_increase, score_increase)

print(max_increase)
