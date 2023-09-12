# 백준 - 브론즈1 - 그림 비교 - 2160 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

입력으로 들어오는 5개씩 들어오는 board 중 서로 비교했을 때 가장 비슷한 그림의 위치를 출력해야 한다.
    - 처음에 문제를 잘못 이해하고, 첫 번째 보드와 비교하는 문제인줄 알고 삽질을 좀 했다..

서로 비교하는 방식은 완전 탐색 방식으로 풀면 된다.
전체 보드를 비교하기 위해 4중 반복문을 사용했고, 그 중 2중은 board 들을 돌고, 중첩된 2중은 체크하는 부분이다. (이 부분을 함수로 빼면 코드가 더 좋을거 같다.)
    - 처음 2중을 돌 때 같은 board 끼리 비교하면 temp가 0이 되므로 i + 1 범위부터 시작해야 된다.
제일 안쪽 2중으로 된 반복문을 시작하기전에 그림이 서로 다른 위치가 더 적은걸 세기위해 temp를 만들어 놓고, 그림이 다를때마다 temp에 1씩 더한다.
미리 큰 값으로 cnt 만들어놓고, temp와 cnt를 비교해서 temp가 더 작은 값이면, 해당 그림의 번호를 기억해 놓는다.(i + 1, j + 1)
이러한 방식으로 완전 탐색을 돌고, 최종 res를 출력하면 된다.
'''

n = int(input())
board_list = []

for i in range(n):
    temp_list = []
    for j in range(5):
        temp_list.append(list(input()))
    board_list.append(temp_list)
# print(board_list)

# 테스트
# n = 3
# board_list =  [
#     [list('..X.....'), list('.XXX...'), list('.XX....'), list('.....X.'), list('.X...X.')],
#     [list('...X...'), list('..XX...'), list('.XX....'), list('.XX..X.'), list('.X...X.')],
#     [list('XX.....'), list('X......'), list('XX...XX'), list('XXXX.XX'), list('XXX..XX')]
# ] # 1 2

cnt = int(1e9)
res = []

for i in range(n - 1):
    for j in range(i + 1, n):
        temp = 0

        for k in range(5):
            for l in range(7):
                if board_list[i][k][l] != board_list[j][k][l]:
                    temp += 1

        if cnt > temp:
            cnt = temp
            res = [i + 1, j + 1]

print(*res)
