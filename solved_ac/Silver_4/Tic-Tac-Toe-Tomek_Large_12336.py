# 백준 - 실버4 - Tic-Tac-Toe-Tomek (Large) - 12336 - 구현 문제
'''
구현 문제

풀이 과정
    1. 입력을 받는다.
    2. board를 만들어 입력을 받는다.
    3. result를 만들어 빈 문자열로 초기화한다.
    4. 4번 반복하여 각각의 경우를 확인한다.
        4.1. 만약 T와 X의 개수가 4개라면 X가 이긴 것이므로 result에 "X won"을 추가하고 break한다.
        4.2. 만약 T와 O의 개수가 4개라면 O가 이긴 것이므로 result에 "O won"을 추가하고 break한다.
        4.3. 만약 T와 X의 개수가 4개라면 X가 이긴 것이므로 result에 "X won"을 추가하고 break한다.
        4.4. 만약 T와 O의 개수가 4개라면 O가 이긴 것이므로 result에 "O won"을 추가하고 break한다.
    5. 만약 result가 빈 문자열이라면 다음의 과정을 실행한다.
        5.1. T와 X의 개수가 4개라면 X가 이긴 것이므로 result에 "X won"을 추가한다.
        5.2. T와 O의 개수가 4개라면 O가 이긴 것이므로 result에 "O won"을 추가한다.
        5.3. T와 X의 개수가 4개라면 X가 이긴 것이므로 result에 "X won"을 추가한다.
        5.4. T와 O의 개수가 4개라면 O가 이긴 것이므로 result에 "O won"을 추가한다.
    6. 만약 result가 빈 문자열이라면 다음의 과정을 실행한다.
        6.1. board를 돌면서 "."의 개수가 0이라면 무승부이므로 result에 "Draw"를 추가한다.
        6.2. 그렇지 않다면

in
    6
    XXXT
    ....
    OO..
    ....

    XOXT
    XXOO
    OXOX
    XXOO

    XOX.
    OX..
    ....
    ....

    OOXX
    OXXX
    OX.T
    O..O

    XXXO
    ..O.
    .O..
    T...

    OXXX
    XO..
    ..O.
    ...O
out
    Case #1: X won
    Case #2: Draw
    Case #3: Game has not completed
    Case #4: O won
    Case #5: O won
    Case #6: O won
'''

t = int(input())

for i in range(t):
    board = [list(input()) for _ in range(4)]
    input()

    result = ""

    for j in range(4):
        if board[j].count("T") + board[j].count("X") == 4:
            result = "X won"
            break
        elif board[j].count("T") + board[j].count("O") == 4:
            result = "O won"
            break
        elif [board[k][j] for k in range(4)].count("T") + [board[k][j] for k in range(4)].count("X") == 4:
            result = "X won"
            break
        elif [board[k][j] for k in range(4)].count("T") + [board[k][j] for k in range(4)].count("O") == 4:
            result = "O won"
            break

    if result == "":
        if [board[k][k] for k in range(4)].count("T") + [board[k][k] for k in range(4)].count("X") == 4:
            result = "X won"
        elif [board[k][k] for k in range(4)].count("T") + [board[k][k] for k in range(4)].count("O") == 4:
            result = "O won"
        elif [board[k][3 - k] for k in range(4)].count("T") + [board[k][3 - k] for k in range(4)].count("X") == 4:
            result = "X won"
        elif [board[k][3 - k] for k in range(4)].count("T") + [board[k][3 - k] for k in range(4)].count("O") == 4:
            result = "O won"

    if result == "":
        if sum([board[k].count(".") for k in range(4)]) == 0:
            result = "Draw"
        else:
            result = "Game has not completed"

    print(f"Case #{i + 1}: {result}")
