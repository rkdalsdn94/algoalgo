# 백준 - 실버4 - 간판 - 5534 - 문자열, 완전 탐색 문제
"""
문자열, 완전 탐색 문제

[핵심 아이디어]
    1. 각 간판에서 가게 이름의 첫 글자가 등장하는 모든 위치를 찾음
    2. 각 첫 글자 위치에서 가능한 모든 간격(공차)을 시도하여 가게 이름이 만들어지는지 확인
    3. 한 간판에서 여러 방법으로 이름을 만들 수 있어도 간판 수는 1개만 증가

[풀이 과정]
    1. 가게 이름과 N개의 기존 간판을 입력 받음
    2. 각 간판에 대해:
        a. 가게 이름의 첫 글자가 등장하는 모든 위치 찾기
        b. 각 첫 글자 위치에서 가능한 모든 간격(공차)을 시도
        c. 일정한 간격으로 문자를 선택했을 때 가게 이름이 완성되는지 확인
        d. 완성되면 해당 간판은 사용 가능하므로 카운트 증가 후 다음 간판으로 넘어감
    3. 최종 카운트 출력
"""

n = int(input())
name = input()
n_list = [input() for _ in range(n)]

# 테스트
# n = 4
# name = 'bar'
# n_list = ['abracadabra', 'bear', 'bar', 'baraxbara'] # 3

res = 0

# 각 간판에 대해 확인
for sign in n_list:
    can_make = False  # 현재 간판으로 가게 이름을 만들 수 있는지 여부

    # 첫 글자의 모든 가능한 위치 찾기
    for i in range(len(sign)):
        if sign[i] != name[0]:
            continue  # 첫 글자가 일치하지 않으면 건너뜀

        # 가능한 모든 간격(공차) 시도
        for interval in range(1, len(sign)):
            match = True

            # 마지막 글자 위치가 간판 범위를 벗어나면 해당 간격은 불가능
            if i + interval * (len(name) - 1) >= len(sign):
                continue

            # 각 글자 위치 확인
            for j in range(len(name)):
                pos = i + j * interval
                if pos >= len(sign) or sign[pos] != name[j]:
                    match = False
                    break

            if match:
                can_make = True
                break

        if can_make:
            break

    if can_make:
        res += 1

print(res)
