# 백준 - 실버2 - N과 M 10 - 15664 - 백 트래킹 문제
'''
백 트래킹 문제

set을 활용하고, 백 트래킹 함수 내에서 for문의 시작 위치만 조심하면 되는 문제이다.
'''

n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n, m = 3, 1
# n_list = sorted([4, 4, 2])  # 2 \ 4
# n, m = 4, 2
# n_list = sorted([9, 7, 9, 1]) # 1 7 \ 1 9 \ 7 9 \ 9 9
# n, m = 4, 4
# n_list = sorted([1, 1, 2, 2])  # 1 1 2 2

res = []
ck = [0] * n


def back_tracking(depth):
    if len(res) == m:
        print(*res)
        return
    temp = set()

    for i in range(depth, n):
        if not ck[i] and n_list[i] not in temp:
            ck[i] = 1
            res.append(n_list[i])
            temp.add(n_list[i])
            back_tracking(i + 1)
            ck[i] = 0
            res.pop()


back_tracking(0)
