# 프로그래머스 - Lv2 - 피로도 - 완전 탐색 문제
"""
완전 탐색 문제

[핵심 아이디어]
    1. 던전을 탐험할 수 있는 모든 순서(순열)를 고려한다.
    2. 각 순열마다 현재 피로도를 관리하며 최대한 많은 던전을 탐험한다.
    3. 탐험 가능한 최대 던전 수를 갱신해 나간다.

[풀이 과정]
    1. itertools의 permutations를 사용하여 던전을 탐험하는 모든 가능한 순서(순열)를 생성한다.
    2. 각 순열에 대해:
        a. 현재 피로도(temp_k)를 초기 피로도(k)로 설정한다.
        b. 탐험한 던전 수(cnt)를 0으로 초기화한다.
        c. 순열의 각 던전에 대해:
            - 현재 피로도가 최소 필요 피로도 이상과 피로도를 소모했을 때 0보다 크거나 같다면 던전을 탐험한다.
            - 던전 탐험 후 피로도를 소모시키고 탐험 횟수를 증가시킨다.
        d. 현재 순열로 탐험한 던전 수와 지금까지의 최대 던전 수를 비교하여 최대값을 갱신한다.
    3. 모든 순열을 확인한 후 최대 던전 수를 반환한다.
"""

from itertools import permutations

def solution(k, dungeons):
    answer = 0

    for i in permutations(dungeons, len(dungeons)):
        temp_k = k
        cnt = 0

        for j in i:
            if temp_k >= j[0] and temp_k - j[1] >= 0:
                temp_k -= j[1]
                cnt += 1

        answer = max(answer, cnt)

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]) == 3)
