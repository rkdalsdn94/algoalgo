# 백준 - 실버2 - 컨벤 데드가 하고싶어요 - 28450 - dp 문제
'''
dp 문제

풀이 과정
1. dp 문제로 풀이
2. n, m을 입력받고 n_list를 입력받는다.
3. h를 입력받는다.
4. n_list의 첫번째 행과 열을 누적합으로 변경한다.
5. n_list의 나머지 부분을 누적합으로 변경한다.
6. n_list의 마지막 값과 h를 비교해서 출력한다.
    6.1. 마지막 값이 h보다 작거나 같으면 n_list의 마지막 값을 출력한다.
    6.2. 마지막 값이 h보다 크면 NO를 출력한다.
'''

n, m = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]
h = int(input())

# 테스트
# n, m = 4, 2
# n_list = [
#     [4, 0], [0, 0], [0, 2], [3, 1]
# ]
# h = 9 # YES  \  7
# n, m = 3, 5
# n_list = [
#     [5, 5, 1, 2, 4], [2, 4, 2, 1, 4], [4, 2, 1, 3, 3]
# ]
# h = 5 # NO
# n, m = 5, 5
# n_list = [
#     [0, 0, 0, 1, 2], [0, 4, 0, 0, 0], [0, 0, 0, 0, 0],
#     [2, 3, 1, 0, 6], [6, 0, 0, 7, 0]
# ]
# h = 5 # NO
# n, m = 5, 5
# n_list = [
#     [0, 1, 0, 5, 3],[0, 3, 2, 0, 6], [2, 0, 0, 4, 0],
#     [0, 3, 0, 2, 0], [3, 0, 6, 0, 0]
# ]
# h = 5 # YES  \  4
# n, m = 5, 6
# n_list = [
#     [0, 0, 1, 0, 0, 5], [0, 0, 0, 0, 0, 0],
#     [0, 3, 0, 0, 0, 2], [0, 4, 4, 0, 3, 0],
#     [4, 0, 2, 0, 0, 0]
# ]
# h = 5 # YES  \  0

for i in range(1, n):
    n_list[i][0] = n_list[i - 1][0] + n_list[i][0]

for i in range(1, m):
    n_list[0][i] = n_list[0][i - 1] + n_list[0][i]

for i in range(1, n):
    for j in range(1, m):
        n_list[i][j] += min(n_list[i - 1][j], n_list[i][j - 1])

if n_list[-1][-1] <= h:
    print('YES')
    print(n_list[n - 1][m - 1])
else:
    print('NO')
