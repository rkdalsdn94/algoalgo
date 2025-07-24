# 백준 - 브론즈2 - Rock, Paper, Scissors - 4593 - 구현, 문자열 문제
"""
구현, 문자열 문제

[핵심 아이디어]
    1. 가위바위보의 승부 규칙을 조건문으로 구현한다.
    2. 각 턴마다 두 플레이어의 선택을 비교하여 승자를 판정한다.
    3. 같은 선택이면 무승부로 처리하고, 다른 경우에만 승리 카운트를 증가시킨다.

[풀이 과정]
    1. 'E'가 두 줄 연속으로 나올 때까지 입력을 받는다.
    2. 각 게임마다 두 플레이어의 승리 횟수를 0으로 초기화한다.
    3. 문자열의 각 위치에서 두 플레이어의 선택을 비교한다.
       - 같으면 무승부 (아무것도 하지 않음)
       - 플레이어1이 이기는 경우: (R,S), (P,R), (S,P)
       - 그 외의 경우는 플레이어2 승리
    4. 각 게임의 결과를 출력한다.
"""

while True:
    player1 = input().strip()
    player2 = input().strip()

    # 종료 조건 확인
    if player1 == 'E' and player2 == 'E':
        break

    # 승리 카운트 초기화
    p1_wins = 0
    p2_wins = 0

    # 각 턴마다 승부 판정
    for i in range(len(player1)):
        choice1 = player1[i]
        choice2 = player2[i]

        # 무승부인 경우
        if choice1 == choice2:
            continue

        # 플레이어1이 이기는 경우
        if (choice1 == 'R' and choice2 == 'S') or \
                (choice1 == 'P' and choice2 == 'R') or \
                (choice1 == 'S' and choice2 == 'P'):
            p1_wins += 1
        # 플레이어2가 이기는 경우
        else:
            p2_wins += 1

    print(f"P1: {p1_wins}")
    print(f"P2: {p2_wins}")
