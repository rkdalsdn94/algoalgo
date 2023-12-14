# 백준 - 실버1 - 부분수열의 합 - 14225 - 완전 탐색 문제
'''
완전 탐색 문제

combinations 를 활용해서 완전 탐색으로 풀었다.
합으로 들어올 수 있는 값의 최대를 착각해서 인덱스 에러를 맞았다.
s의 최댓값이 100_000 이고, n의 최댓값이 20이므로 100_000 * 20 + 1 로 res 배열을 초기화 한 후
combinations의 합으로 해당 값을 사용하고 있다고 표시를 남긴다.
그 후 0번째 인덱스를 제외한 값들 중 제일 처음 0이 나오는 인덱스를 출력하면 된다.
'''

from itertools import combinations as combi

n = int(input())
s_list = list(map(int, input().split()))

# 테스트
# n = 3
# s_list = sorted([5, 1, 2]) # 4
# n = 3
# s_list = sorted([2, 1, 4]) # 8
# n = 3
# s_list = sorted([2, 1, 2, 7]) # 6

res = [0] * (100_000 * 20 + 1)

for i in range(1, n + 1):
    for j in combi(s_list, i):
        res[sum(j)] = 1

print(res[1:].index(0) + 1)
