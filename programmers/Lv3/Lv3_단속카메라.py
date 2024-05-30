# 프로그래머스 - Lv3 - 단속카메라 - 그리디 문제
'''
그리디 문제

차량이 나가는 시점을 오름차순으로 정렬해야 된다.
temp의 값을 -int(1e9)로 초기화 한 뒤, 진입하는 차량(i)이 temp보다 크면 카메라를 설치하고,
temp의 값을 해당 차량이 나가는 값으로 변경한다.
핵심은 temp의 값을 해당 차량이 고속도로를 나가는 시점의 값(j)으로 변경하고,
진입하는 차량(i)이랑 비교하면 된다.

풀이 과정
 1. routes를 진출하는 시점을 기준으로 정렬한다.
 2. temp를 -int(1e9)로 초기화하고, routes를 순회하면서 temp와 비교한다.
 3. temp보다 크면 카메라를 설치하고, temp를 j로 변경한다.
 4. 카메라의 개수를 출력한다.
'''

def solution(routes):
    res = 0
    routes.sort(key=lambda x: x[1])
    temp = -int(1e9)

    for i, j in routes:
        if i > temp:
            res += 1
            temp = j

    return res

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) # 2
