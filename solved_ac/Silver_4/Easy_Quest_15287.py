# 백준 - 실버4 - Easy Quest - 15287 - 구현, 그리디, 시뮬레이션 문제
"""
구현, 그리디, 시뮬레이션 문제

[핵심 아이디어]
    1. 양수(ai > 0)로 만나면 해당 타입 아이템을 획득해서 보관(딕셔너리로 개수 관리).
    2. 0(ai == 0)으로 만나면 유니콘 인덱스를 스택(리스트)에 저장해 두고, 실제 요청 타입은 나중에 결정.
    3. 음수(ai < 0)로 만나면 필요한 아이템(−ai)이 있는지 확인.
       3-1. 딕셔너리(items)에 해당 타입 개수가 있으면, 개수를 하나 차감한다.
       3-2. 없다면 스택(unicorns)에서 마지막에 만난(=가장 최근에 저장된) 유니콘 인덱스를 꺼내서
            그 유니콘에게 필요한 타입을 요청(unicorn_items[idx] = 필요타입).
            만약 스택이 비어 있으면(사용 가능한 유니콘이 없으면) 즉시 “No” 출력하고 종료.
    4. 모든 ai를 순회한 뒤에도 스택에 남아 있는 인덱스(=사용되지 않은 유니콘)가 있을 수 있다.
       이 유니콘들은 실제로 적을 만났을 때 쓰이지 않은 것이므로, 출력 개수를 맞추기 위해
       남은 모든 유니콘 인덱스에 임의의 타입(예: 1)을 할당(unicorn_items[idx] = 1).
    5. 마지막으로 n_list의 처음부터 끝까지 순회하면서 ai == 0인 위치마다 unicorn_items[i]에 저장된 값을
       순서대로 출력하면, “만난 모든 유니콘(0의 개수)만큼” 정수를 한 줄에 나열할 수 있다.

[풀이 과정]
    1. 입력으로 n과 n_list(정수 배열)를 받는다.
    2. items={} 딕셔너리: “획득한 아이템 타입별 개수”를 관리.
       unicorns=[] 리스트: “만난 유니콘의 인덱스”를 스택처럼 저장.
       unicorn_items={} 딕셔너리: “각 유니콘 인덱스가 요청할 아이템 타입”을 기록.
       possible=True 플래그: 만약 불가능 상황이면 False로 바꾼다.
    3. for i, ai in enumerate(n_list) 순회:
       3-1. ai > 0: items[ai] = items.get(ai,0) + 1 (해당 타입 아이템 획득)
       3-2. ai == 0: unicorns.append(i) (유니콘 인덱스만 쌓아 둠)
       3-3. ai < 0: need = -ai
            - items.get(need, 0) > 0 이면 items[need] -= 1 (이미 보유한 아이템 사용)
            - else: 스택(unicorns)이 비어 있으면 possible=False 후 종료
                    스택에 남은 인덱스가 있으면 last = unicorns.pop(), unicorn_items[last] = need (유니콘에게 요청)
    4. 순회가 끝난 후:
       4-1. if not possible: “No” 출력 후 종료
       4-2. else: “Yes” 출력
             - 스택(unicorns)에 남은 인덱스(=사용되지 않은 유니콘)들을 순회하면서 unicorn_items[idx] = 1 (임의 타입 채우기)
             - n_list의 처음부터 끝까지 다시 순회하면서, ai == 0인 위치마다 unicorn_items[i] 값을 순서대로 수집해 res 리스트에 append
             - print(*res) 로 최종 결과를 한 줄에 나열
"""

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 10
# n_list = [1, 0, -4, 0, 0, -1, -3, 0, -1, -2] # Yes  \  4 1 3 2
# n = 5
# n_list = [5, 8, 0, -6, -3] # No
# n = 3
# n_list = [2, -2, -2] # No

items = {} # 보유 중인 아이템 개수 {타입: 개수}
unicorns = [] # 만난 유니콘들의 인덱스(0 기반)
unicorn_items = {} # {유니콘_인덱스: 요청한_아이템_타입}
possible = True

for i, ai in enumerate(n_list):
    if not possible:
        break

    if ai > 0:
        items[ai] = items.get(ai, 0) + 1

    elif ai == 0:
        # 유니콘을 만났다는 표시만 해 두고, 실제 요청 타입은 나중에 채운다
        unicorns.append(i)

    else:  # ai < 0, 악한 생물
        need = -ai

        if items.get(need, 0) > 0:
            items[need] -= 1
        else:
            # 사용할 만한 아이템이 없으면 유니콘에게 요청
            if not unicorns:
                possible = False
            else:
                last_unicorn_idx = unicorns.pop()
                unicorn_items[last_unicorn_idx] = need

if not possible:
    print("No")
else:
    print("Yes")

    # 사용되지 않은 유니콘(인덱스)을 순회하며 임의 타입(1) 할당
    # (딕셔너리에 키가 이미 있으면 사용된 것이므로 그대로 두고, 없으면 1로 채운다)
    for idx in unicorns:
        unicorn_items[idx] = 1

    # 이제 “만난 순서” 대로 모든 유니콘 인덱스를 정렬해서 출력
    # (0부터 n-1까지 탐색하며 ai==0인 위치에서 unicorn_items 값을 꺼낸다)
    res = []
    for i, ai in enumerate(n_list):
        if ai == 0:
            # unicorn_items에는 반드시 키가 있으므로 바로 꺼내면 된다
            res.append(unicorn_items[i])

    print(*res)
