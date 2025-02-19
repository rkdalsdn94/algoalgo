# 백준 - 실버4 - Bridge transport - 6754 - 누적 합, 슬라이딩 윈도우 문제
'''
누적 합, 슬라이딩 윈도우 문제

[핵심 아이디어]
    - 다리는 길이가 40m, 기차 한 칸은 10m이므로 다리에는 최대 4대의 기차가 동시에 있을 수 있음
    - 기차가 다리를 건너는 순서는 1, 2, 3, ... 순으로 정해져 있음
    - 다리 위 기차들의 무게 합이 한계치를 넘지 않아야 함
    - 슬라이딩 윈도우를 사용하여 다리 위에 있는 기차 무게의 합을 추적
    - 기차가 다리에 진입할 때마다 그 시점에 다리가 무너지는지 확인

[풀이 과정]
    1. 다리의 최대 하중(w)과 기차 수(n), 각 기차의 무게를 입력받음
    2. 다리 위 기차들의 무게 합(bridge_weight)과 통과할 수 있는 최대 기차 수(res) 변수 초기화
    3. 모든 기차(n_list)에 대해 순차적으로 처리:
       - 첫 4대 기차는 누적해서 더함
       - 5번째 기차부터는 슬라이딩 윈도우 적용: 새 기차가 들어오면 가장 먼저 들어온 기차는 나감(bridge_weight += current_weight - n_list[i - 4])
    4. 각 단계에서 다리 위 무게 합이 한계치를 초과하면 반복문 중단
    5. 통과할 수 있는 최대 기차 수 출력
'''

w = int(input())
n = int(input())
n_list = [int(input()) for _ in range(n)]

# 테스트
# w = 100
# n = 6
# n_list = [50, 30, 10, 10, 40, 50] # 5

res = 0
bridge_weight = 0

for i in range(n):
    current_weight = n_list[i]

    if i < 4:
        bridge_weight += current_weight
    else:
        bridge_weight += current_weight - n_list[i - 4]

    if bridge_weight > w:
        break

    res = i + 1

print(res)
