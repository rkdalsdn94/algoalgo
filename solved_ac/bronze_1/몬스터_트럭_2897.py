# 백준 - 브론즈1 - 몬스터 트럭 - 2897 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

처음 문제를 풀 때는 bfs 방식으로 풀려고 했는데, 문제 난이도로 봤을 때 굳이 bfs를 적용하지 않아도 풀 수 있는 난이도라 판단했다.
그래서 생각을 좀 더 해보니 어차피 0, 0 위치에서 r행의 c를 한 칸씩 전진하면서 2행 2열의 크기(temp)만 만든 다음 이 값을 기준으로 X의 값을 count 하는 방식으로 풀었다.

res 배열을 다음의 길이를 만족하기 위해 5칸의 길이로 잡고 값은 0으로 초기화한 다음 temp를 기준으로 각각의 값들을 더해주는 방식으로 풀었다.
    - 아무 차도 부수지 않으면서 주차할 수 있는 공간의 개수
    - 둘째 줄은 차 한 대를 부수고 주차할 수 있는 공간의 개수
    - 셋째 줄은 차 두 대
    - 넷째 줄은 차 세 대
    - 다섯째 줄은 차 네 대를 부수고 주차할 수 있는 공간의 개수

해당 크기가 board 크기보다 커지면 안 되기 때문에 i + 1의 크기가 r이거나 j + 1의 크기가 c라면 다음을 실행하기 위해 continue를 사용해야 한다.
'''

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

# 테스트
# r, c = 4, 4
# board = [
#     list('#..#'),
#     list('..X.'),
#     list('..X.'),
#     list('#XX#')
# ] # 1  \  1  \  2  \  1  \  0
# r, c = 4, 4
# board = [
#     list('....'),
#     list('....'),
#     list('....'),
#     list('....')
# ] # 9  \  0  \  0  \  0  \  0
# r, c = 4, 5
# board = [
#     list('..XX.'),
#     list('.#XX.'),
#     list('..#..'),
#     list('.....')
# ] # 2  \  1  \  1  \  0  \  1

res = [0] * 5

for i in range(r):
    for j in range(c):
        if i + 1 == r or j + 1 == c:
            break

        x1, y1 = board[i][j], board[i][j + 1]
        x2, y2 = board[i + 1][j], board[i + 1][j + 1]
        temp = x1 + y1 + x2 + y2

        if '#' in temp:
            continue

        car = temp.count('X')
        if car == 0:
            res[0] += 1
        elif car == 1:
            res[1] += 1
        elif car == 2:
            res[2] += 1
        elif car == 3:
            res[3] += 1
        elif car == 4:
            res[4] += 1

for i in res:
    print(i)
