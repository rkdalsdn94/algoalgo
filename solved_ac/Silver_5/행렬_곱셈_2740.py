# 백준 - 실버5 - 행렬 곱셈 - 2740 - 구현, 수학, 선형대수학 문제
'''
구현, 수학, 선형대수학 문제

전에 풀었던 '프로그래머스 Lv2 행렬의 곱셈'이랑 똑같이 풀면 된다.
따로 풀이는 없고 행렬의 곱셈에 대해서만 알면 된다.
행렬의 곱셈을 모르면 https://www.youtube.com/watch?v=hbnWDWWph-E 여기서 보면 된다.
여기에 나오는 방법으로 전체 matrix를 반복해면서 res 에 값을 더해주면 된다.
'''

n, m = map(int, input().split())
a_matrix = [ list(map(int, input().split())) for _ in range(n) ]
m, k = map(int, input().split())
b_matrix = [ list(map(int, input().split())) for _ in range(m) ]

# 테스트
# n, m = 3, 2
# a_matrix = [ [1, 2], [3, 4], [5, 6] ]
# m, k = 2, 3
# b_matrix = [ [-1, -2, 0], [0, 0, 3] ] # -1 -2 6  \  -3 -6 12  \  -5 -10 18

res = [ [0] * len(b_matrix[0]) for _ in range(len(a_matrix)) ]

for i in range(len(a_matrix)):
    for j in range(len(b_matrix[0])):
        for k in range(len(a_matrix[0])):
            res[i][j] += (a_matrix[i][k] * b_matrix[k][j])

for i in res:
    print(*i)
