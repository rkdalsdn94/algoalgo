# 백준 - 실버2 - 키트 분배하기 - 24938 - 그리디 문제
'''
그리디 문제

[핵심 아이디어]
    누적합(prefix sum)을 활용하여 각 지점에서 필요한 키트 이동 횟수를 계산합니다.
    각 위치에서의 누적된 차이의 절대값이 해당 위치를 지나가야 하는 최소 이동 횟수가 됩니다.
    이는 양방향(왼쪽에서 오른쪽, 오른쪽에서 왼쪽)의 모든 키트 이동을 효과적으로 고려할 수 있게 합니다.

[풀이 과정]
    1. 입력값으로 방의 개수(n)와 각 방의 키트 수(n_list)를 받습니다.
    2. 목표로 하는 평균값을 계산합니다.
      - average = 전체 키트의 합 / 방의 개수
    3. 각 위치별로 누적된 차이와 필요한 이동 횟수를 계산합니다.
      - prefix_sum에 (현재 방의 키트 수 - 평균값)을 더해가며 누적된 차이를 추적
      - 각 위치에서 abs(prefix_sum)이 해당 위치를 지나가는 키트의 최소 이동 횟수
      - res에 모든 위치의 이동 횟수를 합산
    4. 최종적으로 계산된 총 이동 횟수(res)를 출력합니다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 3
# n_list = [1, 3, 2] # 1
# n = 7
# n_list = [2, 6, 3, 2, 5, 4, 6] # 10

average = sum(n_list) // n
res = 0
prefix_sum = 0
for i in range(n - 1):
    prefix_sum += n_list[i] - average
    res += abs(prefix_sum)

print(res)
