# 프로그래머스 - Lv2 - 광물 캐기 - 그리디, 정렬 문제
"""
그리디, 정렬 문제

[핵심 아이디어]
    1. 곡괭이는 한 번에 5개의 광물을 캐야 하므로, 5개 단위로 묶어서 다이아몬드/철/돌 개수를 세기
    2. 광물 그룹을 다이아몬드 > 철 > 돌 순서로 내림차순 정렬하여 가장 높은 피로도가 발생할 수 있는 그룹부터 처리
    3. 피로도가 가장 적게 드는 곡괭이(다이아몬드 곡괭이)부터 사용하여 최적의 선택 수행
    4. 사용할 수 있는 곡괭이보다 광물이 많은 경우, 처리할 수 있는 광물만 추려내기

[풀이 과정]
    1. 사용 가능한 곡괭이 총 개수 계산 (곡괭이 하나당 5개의 광물을 캘 수 있음)
    2. 곡괭이로 캘 수 있는 광물 개수보다 많은 광물은 무시 (앞에서부터 처리 가능한 만큼만 자르기)
    3. 광물을 5개씩 그룹으로 묶고, 각 그룹에 포함된 다이아몬드/철/돌 개수 계산
    4. 그룹을 다이아몬드 > 철 > 돌 순서로 내림차순 정렬 (피로도가 높은 그룹 우선 처리)
    5. 정렬된 그룹별로 가장 좋은 곡괭이(다이아몬드 곡괭이)부터 사용하여 피로도 계산
    6. 모든 그룹을 처리한 후 최종 피로도 반환
"""

def solution(picks, minerals):
    answer = 0

    # 가진 곡괭이로 캘 수 있는 최대 광물 개수 계산
    max_minerals = sum(picks) * 5

    # 가진 곡괭이로 캘 수 있는 만큼만 광물 자르기
    if len(minerals) > max_minerals:
        minerals = minerals[:max_minerals]

    # 광물 5개씩 묶어서 그룹화하고 각 광물 타입 개수 세기
    mineral_groups = [[0, 0, 0] for _ in range((len(minerals) + 4) // 5)]
    for i, mineral in enumerate(minerals):
        group_idx = i // 5
        if mineral == 'diamond':
            mineral_groups[group_idx][0] += 1
        elif mineral == 'iron':
            mineral_groups[group_idx][1] += 1
        else:  # stone
            mineral_groups[group_idx][2] += 1

    # 다이아몬드 > 철 > 돌 순서로 내림차순 정렬 (피로도가 높은 그룹 우선)
    mineral_groups.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

    # 피로도 계산
    for group in mineral_groups:
        dia_count, iron_count, stone_count = group

        # 가장 좋은 곡괭이부터 사용
        if picks[0] > 0:  # 다이아몬드 곡괭이
            picks[0] -= 1
            answer += dia_count + iron_count + stone_count  # 모든 광물당 피로도 1
        elif picks[1] > 0:  # 철 곡괭이
            picks[1] -= 1
            answer += dia_count * 5 + iron_count + stone_count  # 다이아당 5, 나머지 1
        elif picks[2] > 0:  # 돌 곡괭이
            picks[2] -= 1
            answer += dia_count * 25 + iron_count * 5 + stone_count  # 다이아당 25, 철당 5, 돌당 1
        else:
            break  # 사용할 곡괭이 없으면 종료

    return answer

minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
print(solution([1, 3, 2], minerals))  # 12

minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
print(solution([0, 1, 1], minerals))  # 50
