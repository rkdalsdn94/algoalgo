'''
완전 탐색, 구현 문제

board에서 map함수를 통해 만든 min, max 값들을 하나의 수로 다시 min, max으로 만든다.(이 값 사이중에 나중에 높이가 된다.)
그리고 입력받은 보드 만큼 다시 반복문을 돈 후에
블록을 더할 경우, 뺄 경우를 다 구해 본 후 최종 반환해야 될 값을 계산 해준후에 출력한다.

https://pythontutor.com/live.html#mode=edit 여기서 입력으로 주어진 값을 한번씩 돌려보면 이해가 좀 더 편하다.
'''

N, M, B = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]

# 테스트
# N, M, B = 3, 4, 99
# board = [[0,0,0,0],[0,0,0,0],[0,0,0,1]] # 2 0
# N, M, B = 3, 4, 1
# board = [[64,64,64,64],[64,64,64,64],[64,64,64,63]] # 1 64
# N, M, B = 3, 4, 0
# board = [[64,64,64,64],[64,64,64,64],[64,64,64,63]] # 22 63

min_board_num = min(map(min, board))
max_board_num = max(map(max, board))
res = 6.4 * (10 ** 7) + 1

for i in range(min_board_num, max_board_num + 1):
    block_plus_cnt, block_minus_cnt = 0, 0

    for j in range(N):
        for k in range(M):
            temp = board[j][k] - i

            if temp > 0: # 블록을 빼야 될 상황
                block_minus_cnt += temp
            
            if temp < 0: # 블록을 더해야 되는 상황
                block_plus_cnt += abs(temp)
            
    if block_minus_cnt + B >= block_plus_cnt:
        time = block_minus_cnt * 2 + block_plus_cnt

        if res >= time:
            res = time
            height = i

print(res, height)
