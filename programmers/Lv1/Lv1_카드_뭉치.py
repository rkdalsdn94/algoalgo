# 프로그래머스 - Lv1 - 카드 뭉치 - 그리디, 시뮬레이션 문제
'''
그리디, 시뮬레이션 문제

[핵심 아이디어]
1. 두 카드 뭉치(cards1, cards2)에서 카드를 순서대로만 사용하여 목표 단어 배열(goal)을 만들 수 있는지 확인합니다.
2. 각 카드 뭉치의 현재 위치를 인덱스로 관리하면서, 목표 배열의 각 단어가 현재 위치의 카드와 일치하는지 확인합니다.
3. 목표 단어가 어느 카드 뭉치의 현재 카드와도 일치하지 않으면 목표 배열을 만들 수 없습니다.

[풀이 과정]
1. 두 카드 뭉치의 현재 위치를 가리키는 인덱스(i, j)를 0으로 초기화합니다.
2. 목표 배열의 각 단어를 순차적으로 확인합니다.
3. 현재 단어가 첫 번째 카드 뭉치의 현재 카드와 일치하면, 첫 번째 카드 뭉치의 인덱스를 1 증가시킵니다.
4. 그렇지 않고, 현재 단어가 두 번째 카드 뭉치의 현재 카드와 일치하면, 두 번째 카드 뭉치의 인덱스를 1 증가시킵니다.
5. 현재 단어가 어느 카드 뭉치의 현재 카드와도 일치하지 않으면, "No"를 반환합니다.
6. 모든 단어를 성공적으로 처리했다면 "Yes"를 반환합니다.'''

def solution(cards1, cards2, goal):
    i, j = 0, 0

    for word in goal:
        if i < len(cards1) and word == cards1[i]:
            i += 1
        elif j < len(cards2) and word == cards2[j]:
            j += 1
        else:
            return "No"

    return "Yes"

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]) == "Yes")
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]) == "No")
