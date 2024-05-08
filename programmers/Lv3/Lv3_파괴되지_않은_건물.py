# 프로그래머스 - Lv3 - 파괴되지 않은 건물 - 누적 합
'''
누적 합 문제

n과 m, skill 범위의 작고(모두 100) 제한시간이 10초라서 완전 탐색 방식으로 문제를 풀려고 했다가 효율성 테스트에서 시간 초과가 발생했다.
따라서 코드를 최적화해야 되는데, 어떤 값을 누적 값으로 사용할 지 감이 안 왔다.
그래서 다른 사람의 풀이를 참고해보니 누적 값을 신기하게 활용했다.
행과 열을 기준으로 skill의 시작 부분과 끝 부분을 +, - 하고, 행 별로 더하고, 열 별로 더하는 방식이다.
https://pythontutor.com/visualize.html#mode=edit 여기에서 아래 코드를 실행해보면서 이해해보자.

풀이 과정
 1. board 보다 행, 열이 각각 1씩 큰 prefix_board를 만든다.
 2. skill을 순회하면서 t가 1이면 degree를 -degree로 바꿔준다.
 3. prefix_board에서 skill의 시작 부분과 끝 부분에 degree를 더하고 빼준다.
 4. 위에서 skill 부분의 위치를 계산한 뒤 열과 행을 기준으로 누적 합을 계산한다.
 5. 누적 합으로 구한 prefix_board와 원래의 board와 합치면서 해당 위치가 0보다 크면 res에 1씩 더한다.
'''

def solution(board, skill):
    res = 0
    n, m = len(board), len(board[0]) # n: 행, m: 열
    prefix_board = [[0] * (m + 1) for _ in range(n + 1)]

    for i in skill:
        t, r1, c1, r2, c2, degree = i
        if t == 1:
            degree = -degree

        prefix_board[r1][c1] += degree
        prefix_board[r1][c2 + 1] += -degree
        prefix_board[r2 + 1][c1] += -degree
        prefix_board[r2 + 1][c2 + 1] += degree

    # 열기준 누적 합 계산
    for i in range(m):
        for j in range(1, n):
            prefix_board[j][i] += prefix_board[j - 1][i]

    # 행기준 누적 합 계산
    for i in range(n):
        for j in range(1, m):
            prefix_board[i][j] += prefix_board[i][j - 1]

    # 기존의 board와 합치면서 res 구하기
    for i in range(n):
        for j in range(m):
            board[i][j] += prefix_board[i][j]

            if board[i][j] > 0:
                res += 1

    return res

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill)) # 10
board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board, skill)) # 6

'''
시간 초과 풀이

def solution(board, skill):
    res = 0

    for i in skill:
        t, r1, c1, r2, c2, degree = i
        if t == 1:
            degree = -degree

        for j in range(r1, r2 + 1):
            for k in range(c1, c2 + 1):
                board[j][k] += degree

    for i in board:
        res += len(list(filter(lambda x: x > 0, i)))

    return res

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill)) # 10

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board, skill)) # 6
'''
