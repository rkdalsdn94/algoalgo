# 백준 - 실버2 - 도영이가 만든 음식 - 2961 - 완전 탐색, 비트마스킹, 백 트래킹 문제
'''
완전 탐색, 비트마스킹, 백 트래킹 문제

combinations 를 활용해서 완전 탐색 방식으로 풀었다.

입력들을 모두 입력받은 뒤 n_list의 값들을 1 ~ n 까지 조합을 만든다.
해당 조합의 값을 신맛(sour, a) 쓴맛(bitter, b) 값으로 꺼낸다.
신맛의 기본 값은 1로 초기화하고, 쓴맛은 0으로 초기화 한 뒤, 신맛끼리는 곱하고, 쓴맛끼리는 더한다.
곱하고 더한 값의 차를 res와 비교해서 더 작은 값으로 바꿔주면 된다.
'''

from itertools import combinations as combi

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 7
# n_list = [[3, 10]] # 7
# n = 2
# n_list = [[3, 8], [5, 8]] # 1
# n = 4
# n_list = [[1, 7], [2, 6], [3, 8], [4, 9]] # 1

res = int(1e9)

for i in range(1, n + 1):
    for j in combi(n_list, i):
        sour, bitter = 1, 0

        for a, b in j:
            sour *= a
            bitter += b

        res = min(res, abs(sour - bitter))

print(res)
