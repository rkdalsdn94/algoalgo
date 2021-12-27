# n, m = 3, 4    # res = 2
# matrix_A = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
# matrix_B = [[1, 0, 0, 1], [1, 0, 1, 1], [1, 0, 0, 1]]

# n, m = 18, 3     # res = 7
# matrix_A = [[0,0,1], [1,0,0], [1,0,0], [0,0,0], [0,1,1], [0,1,0], \
# [1,0,0], [1,0,0], [0,1,0], [0,1,0], [0,1,0], [1,1,0], \
# [1,0,1], [1,0,1], [0,0,0], [1,1,0], [0,0,0], [1,1,0]]

# matrix_B = [[0,0,1], [1,0,0], [0,1,1], [0,0,0], [1,0,0], [0,1,0], \
# [0,1,1], [1,0,0], [1,0,1], [1,0,1], [0,1,0], [0,0,1], \
# [0,1,0], [0,1,0], [1,1,1], [1,1,0], [1,1,1], [0,0,1]]

n, m = map(int, input().split())
matrix_A = [list(map(int, input())) for _ in range(n)]
matrix_B = [list(map(int, input())) for _ in range(n)]
res = 0

def converter(x, y, matrix_A):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            matrix_A[i][j] = 1 - matrix_A[i][j]

for i in range(n - 2):
    for j in range(m - 2):
        if matrix_A[i][j] != matrix_B[i][j]:
            converter(i, j, matrix_A)
            res += 1

# 여기서 테스트케이스 오류가 있다.. 예를 들어 1, 1 -> 1 -> 1 이렇게 in 정보가 주어진다고 했을 때 -1로 출력되어야 통과인데 내 코드는 0을 출력하는데 정답 처리가 되었다.. 테케 추가 요청이 활성화 되면 요청 해야겠다.
if matrix_A == matrix_B:
    print(res)
else:
    print(-1)
