'''
문제를 구하는 로직 자체는 어렵지 않다.
근데 board가 a1, a2 이런 식으로 문자랑 숫자가 같이 나와서 이거 구현하는데 까다로웠다.
구현에 대한 문제를 더 풀어야 되겠다 라는 생각이 들었다.
'''
# king, stone, cnt = input().split()
# move_map = [ input() for _ in range(int(cnt)) ]

# 테스트
# king, stone, cnt = 'A1', 'A2', '5'
# move_map = [ 'B', 'L', 'LB', 'RB', 'LT' ] # A1 \n A2
# king, stone, cnt = 'A1', 'H8', '1'
# move_map = [ 'T' ] # A2 \n H8
# king, stone, cnt = 'A1', 'A2', '1'
# move_map = [ 'T' ] # A2 \n A3
king, stone, cnt = 'A8', 'B7', '18'
move_map = [ 'RB', 'RB', 'RB', 'RB', 'RB', 'RB',
             'RB', 'RB', 'RB', 'RB', 'RB', 'RB',
             'RB', 'RB', 'RB', 'RB', 'RB', 'RB', ] # G2 \n H1

map_dic = { "R": (1, 0), "L": (-1, 0), "B": (0, -1),
            "T": (0, 1), "RT": (1, 1), "LT": (-1, 1),
            "RB": (1, -1), "LB": (-1, -1) }
king_x, king_y = ord(king[0]) - ord('A'), int(king[1]) - 1
stone_x, stone_y = ord(stone[0]) - ord('A'), int(stone[1]) - 1

for i in move_map:
    king_nx, king_ny = king_x + map_dic[i][0], king_y + map_dic[i][1]

    if king_nx < 0 or king_ny < 0 or king_nx > 7 or king_ny > 7:
        continue

    if king_nx == stone_x and king_ny == stone_y:
        stone_nx, stone_ny = stone_x + map_dic[i][0], stone_y + map_dic[i][1]

        if stone_nx < 0 or stone_ny < 0 or stone_nx > 7 or stone_ny > 7:
            continue
        stone_x, stone_y = stone_nx, stone_ny

    king_x, king_y = king_nx, king_ny

print(f'{chr(king_x + ord("A"))}{king_y + 1}')
print(f'{chr(stone_x + ord("A"))}{stone_y + 1}')
