# 프로그래머스 - Lv1 - 햄버거 만들기 - 자료 구조(스택) 문제
"""
자료 구조(스택) 문제

[핵심 아이디어]
    1. 스택을 활용하여 재료가 쌓이는 과정을 시뮬레이션한다.
    2. 새로운 재료가 추가될 때마다 스택의 최상단 4개의 재료가 햄버거 패턴(1-2-3-1)과 일치하는지 확인한다.
    3. 햄버거 패턴과 일치할 경우, 해당 재료들을 스택에서 제거하고 햄버거 카운트를 증가시킨다.

[풀이 과정]
    1. 빈 스택(temp)을 생성하여 재료를 쌓아갈 준비를 한다.
    2. ingredient 배열의 각 재료를 순서대로 스택에 추가한다.
    3. 재료를 추가할 때마다 스택의 마지막 4개 요소가 [1, 2, 3, 1] 패턴(빵-야채-고기-빵)과 일치하는지 확인한다.
    4. 패턴이 일치하면, 해당 4개 재료를 스택에서 제거(pop)하고 만든 햄버거 개수(answer)를 1 증가시킨다.
    5. 모든 재료를 처리한 후, 만들어진 햄버거의 총 개수를 반환한다.
"""

def solution(ingredient):
    answer = 0
    temp = []

    for i in ingredient:
        temp.append(i)

        if temp[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                temp.pop()

    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]) == 2)
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]) == 0)
