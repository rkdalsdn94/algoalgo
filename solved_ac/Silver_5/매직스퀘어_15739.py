# 백준 - 실버5 - 매직스퀘어 - 15739 - 구현 문제
'''
구현 문제

문제에 주어진 요구사항을 구현하기만 하면 된다.
문제를 잘 안 읽고 풀었을 경우 틀릴수도 있다.(처음에 제대로 안 읽고 제출했다가 틀렸다...)

구해야 되는 값은 다음과 같다.
    1. 중복되는 수가 없이 모두 달라야 한다.
    2. 행의 합, 열의 합, 2개의 대각선의 수열의 합이 같아야 한다.

아래 코드에서 각 상황을 주석으로 달아놨다.
'''

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 3
# matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]  # TRUE
# n = 4
# matrix = [
#     [4, 14, 15, 1],
#     [9, 7, 6, 12],
#     [5, 11, 10, 8],
#     [16, 2, 3, 13]
# ] # TRUE

row_temp = []
duplication_ck = set()
diagonal_a, diagonal_b = [], []

for i in matrix:
    for j in i: # 중복되는 수를 체크하기 위해
        duplication_ck.add(j)
    if sum(i) != n * (n ** 2 + 1) // 2: # 행의 합이 다를 경우 'FALSE'를 출력하고 프로그램 종료
        print('FALSE')
        exit(0)
    row_temp.append(sum(i))

for i in range(n):
    aa = []

    for j in range(n):
        aa.append(matrix[j][i])

    if sum(aa) != n * (n ** 2 + 1) // 2: # 열의 합이 다를 경우 'FALSE'를 출력하고 프로그램 종료
        print('FALSE')
        exit(0)

for i in range(n): # 1번째 대각선
    for j in range(i, i + 1):
        diagonal_a.append(matrix[i][j])

for i in range(n): # 2번째 대각선
    for j in range(n - 1 - i, n):
        diagonal_b.append(matrix[i][j])
        break

if sum(diagonal_a) != sum(diagonal_b): # 두 대각선의 합이 다를 경우 'FALSE'를 출력하고 프로그램 종료
    print('FALSE')
    exit(0)

if len(duplication_ck) != n ** 2: # 중복되는 수가 있으면 'FALSE'를 출력하고 프로그램 종료
    print('FALSE')
    exit(0)

print('TRUE') # 위 과정을 종료 없이 통과하면 'TRUE' 출력
