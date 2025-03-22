# 프로그래머스 - Lv2 - 롤케이크 자르기 - 구현, 자료구조(해시) 문제
"""
구현, 자료구조(해시) 문제

[핵심 아이디어]
    1. 딕셔너리를 사용해 각 토핑의 개수를 카운팅한다.
    2. 한쪽은 토핑의 종류를 추가하고, 다른 쪽은 토핑의 종류를 제거해가며 양쪽의 토핑 종류 수를 비교한다.
    3. 집합(set)의 길이를 사용하는 대신 딕셔너리로 토핑 종류 수를 실시간으로 계산하여 시간 복잡도를 개선한다.

[풀이 과정]
    1. 오른쪽 부분의 모든 토핑과 그 개수를 딕셔너리(right_dict)에 저장한다.
    2. 왼쪽 부분의 토핑 종류를 저장할 딕셔너리(left_dict)를 초기화한다.
    3. 토핑 배열을 순회하면서:
       - 현재 토핑을 왼쪽 딕셔너리에 추가
       - 오른쪽 딕셔너리에서 현재 토핑의 개수를 감소
       - 오른쪽 딕셔너리에서 토핑 개수가 0이 되면 해당 토핑 종류 제거
       - 왼쪽과 오른쪽 딕셔너리의 키 개수(토핑 종류의 수)가 같으면 answer 증가
    4. 최종적으로 구해진 answer를 반환
"""

def solution(topping):
    answer = 0

    # 오른쪽 부분의 모든 토핑 개수 카운팅
    right_dict = {}
    for t in topping:
        right_dict[t] = right_dict.get(t, 0) + 1

    # 왼쪽 부분의 토핑 종류 저장할 딕셔너리
    left_dict = {}

    # 토핑을 하나씩 왼쪽으로 이동시키며 비교
    for t in topping:
        # 현재 토핑을 왼쪽에 추가
        left_dict[t] = left_dict.get(t, 0) + 1

        # 오른쪽에서 현재 토핑 개수 감소
        right_dict[t] -= 1

        # 오른쪽에서 토핑이 더 이상 없으면 제거
        if right_dict[t] == 0:
            del right_dict[t]

        # 양쪽의 토핑 종류 수가 같으면 정답 증가
        if len(left_dict) == len(right_dict):
            answer += 1

    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]) == 2)
print(solution([1, 2, 3, 1, 4]) == 0)
