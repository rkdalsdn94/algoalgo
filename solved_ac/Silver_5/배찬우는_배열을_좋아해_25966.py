# 백준 - 실버5 - 배찬우는 배열을 좋아해 - 25966 - 구현 문제
'''
구현 문제

단순히 2차원 배열을 입력받고, 명령어에 따라 배열을 변경하는 문제이다.
PyPy3로 제출하거나 input을 sys.stdin.readline()을 사용해야 된다.

풀이 과정
    1. 입력 조건에 따라 알맞게 입력을 받는다.
    2. command에 따라 배열을 변경한다.
    3. 변경된 배열을 출력한다.
'''

n, m, q = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]
command = [list(map(int, input().split())) for _ in range(q)]

# 테스트
# n, m, q = 4, 3, 4
# n_list = [
#     [10, 3, 8], [2, 10, 4], [1, 8, 4], [1, 4, 2]
# ]
# command = [
#     [1, 2, 2], [0, 1, 0, 9], [1, 2, 1], [1, 3, 0]
# ]
# '''
#     1 4 2
#     1 8 4
#     9 10 4
#     10 3 8
# '''

for i in command:
    if i[0] == 0:
        n_list[i[1]][i[2]] = i[3]
    elif i[0] == 1:
        n_list[i[1]], n_list[i[2]] = n_list[i[2]], n_list[i[1]]

for i in n_list:
    print(*i)
