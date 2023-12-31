# 백준 - 실버2 - N과 M 11 - 15665 - 백 트래킹 문제
'''
백 트래킹 문제

N과 M 시리즈 문제이다.
기존에는 ck 변수를 두고 방문한 곳의 여부를 확인했었는데, 이 문제에선 그럴 필요가 없다.
이 전의 값(temp)만 잘 기억해두고 현재 방문하는 값(n_list[i])과 같은 값인지 다른 값인지 체크만 하면 된다.
'''

n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n, m = 3, 1
# n_list = sorted([4, 4, 2]) # 2  \  4
# n, m = 4, 2
# n_list = sorted([9, 7, 9, 1])
# '''
#     1 1
#     1 7
#     1 9
#     7 1
#     7 7
#     7 9
#     9 1
#     9 7
#     9 9
# '''
# n, m = 4, 4
# n_list = sorted([1, 1, 2, 2])
# '''
#     1 1 1 1
#     1 1 1 2
#     1 1 2 1
#     1 1 2 2
#     1 2 1 1
#     1 2 1 2
#     1 2 2 1
#     1 2 2 2
#     2 1 1 1
#     2 1 1 2
#     2 1 2 1
#     2 1 2 2
#     2 2 1 1
#     2 2 1 2
#     2 2 2 1
#     2 2 2 2
# '''

res = []

def back_tracking(depth):
    if depth == m:
        print(' '.join(map(str, res)))
        return

    temp = 0
    for i in range(n):
        if temp != n_list[i]:
            res.append(n_list[i])
            temp = n_list[i]
            back_tracking(depth + 1)
            res.pop()

back_tracking(0)
