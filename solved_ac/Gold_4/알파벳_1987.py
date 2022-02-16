'''
bfs 풀듯이 deque을 사용하고 있었는데,
deque으로 하면 중복 값도 허용하게 돼서 그런지 시간 초과(python3), 메모리 초과(pypy3)가 나온다
중복 값 제거를 위해 set으로 바꾼 후 제출하니 통과되었다.
'''

from collections import deque # set으로 바꿈

r, c = map(int, input().split())
board = [ list(input()) for _ in range(r) ]

# 테스트
# r, c, board = 2, 4, ['CAAB' ,'ADCB'] # 3
# r, c, board = 3, 6, ['HFDFFB', 'AJHGDH', 'DGAGEH'] # 6
# r, c, board = 5, 5, ['IEFCJ', 'FHFKC', 'FFALF', 'HFGCF', 'HMCHH'] # 10
# r, c, board = 1, 1, ['A'] # 1

def bfs():
    q = set([(0, 0, board[0][0])])
    dx, dy = [0,1,0,-1], [1,0,-1,0]
    res = 1
    
    while q:
        a, b, word = q.pop()

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in word:
                q.add((nx, ny, word + board[nx][ny]))
                res = max(res, len(word) + 1)

    return res

print(bfs())

