# 프로그래머스 - Lv1 - 삼총사 - 조합, 완전 탐색 문제
'''
조합, 완전 탐색 문제

[핵심 아이디어]
    - 주어진 학생 번호 배열에서 3명을 선택하는 모든 경우의 수를 구한다.
    - 선택된 3명의 번호 합이 0인 경우를 찾아 개수를 센다.
    - Python의 combinations 라이브러리를 활용하여 모든 조합을 효율적으로 탐색한다.

[풀이 과정]
    1. itertools 라이브러리의 combinations 함수를 사용하여 학생 번호 배열에서 3개를 선택하는 모든 조합을 생성한다.
    2. 각 조합에 대해 합이 0인지 확인한다.
    3. 합이 0인 조합의 개수를 세어 반환한다.
'''

from itertools import combinations as combi

def solution(number):
    answer = 0

    for i in combi(number, 3):
        if sum(i) == 0:
            answer += 1

    return answer

print(solution([-2, 3, 0, 2, -5]) == 2)
print(solution([-3, -2, -1, 0, 1, 2, 3]) == 5)
print(solution([-1, 1, -1, 1]) == 0)
