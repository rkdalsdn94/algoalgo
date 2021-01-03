def solution(board, moves):
    answer = 0
    temp = []
    moves = [i - 1 for i in moves]
    for i in moves:
        for idx in board:
            # print(idx[i])
            if idx[i] != 0:
                temp.append(idx[i])
                idx[i] = 0
                if len(temp) >= 2 and temp[-1] == temp[-2]:
                    answer += 2
                    temp.pop()
                    temp.pop()
                break

    # print(temp)
    return answer

# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
