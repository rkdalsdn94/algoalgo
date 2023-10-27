# 프로그래머스 - Lv1 - 달리기 경주 - 자료 구조(hash)
'''
단순하게 풀다가 시간 초과를 받았다 (제일 아래 시간 초과 코드)

해시(파이썬에서는 dict)를 활용해서 풀면 된다.

풀이 과정
 - 처음 players 의 순위대로 temp_dic 을 만든다. (key가 플레이어 이름, value가 등수)
 - callings의 값을 꺼내 temp_dic에서 해당 키를 가진 밸류 (이게 players의 인덱스가 된다.)
    - 위에서 구한 인덱스를 이용해 temp_dic의 밸류를 1빼고, 앞선 순위는 1을 더한다.
 - 위에서 구한 idx로 (idx, idx - 1) 두 위치를 스왑한다.
'''

def solution(players, callings):
    temp_dic = {j: i for i, j in enumerate(players)}

    for i in callings:
        idx = temp_dic[i]
        temp_dic[i] -= 1
        temp_dic[players[idx - 1]] += 1
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
    return players


print(
    solution(
        ["mumu", "soe", "poe", "kai", "mine"],
        ["kai", "kai", "mine", "mine"])
)  # ["mumu", "kai", "mine", "soe", "poe"]

'''
시간 초과 코드

callings를 반복하는 만큼 players.index 이 부분 때문에 시간 초과가 나는듯?
이 부분을 딕셔너리의 키 밸류를 활용하면 시간을 줄일 수 있다.

def solution(players, callings):
    for i in callings:
        idx = players.index(i) # O(players * callings) 복잡도
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
    return players
'''
