# 프로그래머스 - Lv1 - 푸드 파이트 대회 - 문자열, 시뮬레이션 문제
'''
문자열, 시뮬레이션 문제

[핵심 아이디어]
    - 두 선수가 동일한 종류와 양의 음식을 먹어야 하므로, 각 음식의 수는 짝수 개만 대회에 사용할 수 있습니다.
    - 음식을 배치할 때는 중앙에 물(0)을 두고, 대칭적으로 배치해야 합니다.
    - 요구된 출력 형태인 "1223330333221"과 같은 문자열을 생성하려면 각 음식의 수를 절반으로 나누어 왼쪽에 배치하고, 이를 뒤집어 오른쪽에 배치합니다.

[풀이 과정]
    - 주어진 food 배열에서 각 음식 별로 양쪽 선수가 먹을 수 있는 최대 개수(짝수)를 계산합니다.
    - 왼쪽 선수가 먹을 음식 배열(왼쪽 절반)을 구성합니다.
    - 중앙에 물(0)을 배치합니다.
    - 오른쪽 선수가 먹을 음식 배열(왼쪽 배열의 역순)을 구성합니다.
    - 최종적으로 세 부분(왼쪽 배열 + 물 + 오른쪽 배열)을 이어붙여 결과 문자열을 생성합니다.
'''

def solution(food):
    answer = ''

    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)

    return answer + '0' + answer[::-1]

print(solution([1, 3, 4, 6]) == "1223330333221")
print(solution([1, 7, 1, 2]) == "111303111")
