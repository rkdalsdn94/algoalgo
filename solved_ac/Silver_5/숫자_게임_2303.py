# 백준 - 실버5 - 숫자 게임 - 2303 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

3중 for 문으로 직접 구현하려다가 파이썬 itertools 모듈을 사용했다.
7%에서 '틀렸습니다.'가 나오면 '이긴 사람이 두 명 이상일 경우에는 번호가 가장 큰 사람의 번호를 출력한다.' 이 부분을 신경쓰면 된다.
이 부분을 신경안쓰고 풀었다가 틀렸었다. res를 역순으로 돌면서 max값과 같은 값이 나오면 출력하면 된다.
'''

from itertools import combinations

n = int(input())
n_list = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n = 3
# n_list = [
#     [7, 5, 5, 4, 9],
#     [1, 1, 1, 1, 1],
#     [2, 3, 3, 2, 10]
# ] # 1
# n = 3
# n_list = [
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1]
# ] # 3

res = [0] * (n)

def number_game(arr):
    temp = []
    for i in combinations(arr, 3):
        temp.append(int(str(sum(i))[-1]))

    return max(temp)

for i in range(n):
    res[i] = number_game(n_list[i])

max_res = max(res)
for i in range(n - 1, -1, -1):
    if max_res == res[i]:
        print(i + 1)
        break
