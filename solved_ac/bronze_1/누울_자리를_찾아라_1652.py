'''
    단순 구현으로 풀었다
    세로로 누울때만 [j][i] 이렇게 찾는거 빼곤 크게 생각할게 많이 없었다
'''

def solution(n, room):
    temp_row, temp_col = 0, 0
    answer_row, answer_col = 0, 0

    for i in room: # row 검사
        for j in i:
            if j == '.':
                temp_row += 1
            else:
                if temp_row > 1:
                    answer_row += 1
                temp_row = 0
        if temp_row > 1:
            answer_row += 1
        temp_row = 0
    
    for i in range(len(room)): # col 검사
        for j in range(len(room[i])):
            if room[j][i] == '.':
                temp_col += 1
            else:
                if temp_col > 1:
                    answer_col += 1
                temp_col = 0
        if temp_col > 1:
            answer_col += 1
        temp_col = 0
    
    return answer_row, answer_col

# n = int(input())
# room = [list(input()) for _ in range(n)]

# row, col = solution(n, room)
# print(row, col)
print(solution(5, [['.', '.', '.', '.', 'X'], ['.', '.', 'X', 'X', '.'], ['.', '.', '.', '.', '.'], ['.', 'X', 'X', '.', '.'], ['X', '.', '.', '.', '.']])) # 5 4
