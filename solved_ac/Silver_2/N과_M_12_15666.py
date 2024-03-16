# 백준 - 실버2 - N과 M 12 - 15666 - 백 트래킹 문제
'''
백 트래킹 문제

기존의 N과 M 문제를 풀 듯이 백 트래킹으로 풀면 된다.
따라서, 따로 풀이 과정을 적진 않고 코드를 읽어보면 된다.
참고만 적는다면 여기에선 ck 변수를 활용하지 않고, 중복 체크만 진행하면 된다.
'''

n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n, m = 3, 1
# n_list = sorted([4, 4, 2]) # 2  \  4
# n, m = 4, 2
# n_list = sorted([9, 7, 9, 1]) # 1 1  \  1 7  \  1 9  \  7 7  \  7 9  \  9 9
# n, m = 4, 4
# n_list = sorted([1, 1, 2, 2]) # 1 1 1 1  \  1 1 1 2  \  1 1 2 2  \  1 2 2 2  \  2 2 2 2

arr = []

def back_tracking(num):
    if len(arr) == m:
        print(*arr)
        return

    temp = -1
    for i in range(num, n):
        if temp != n_list[i]:
            temp = n_list[i]
            arr.append(n_list[i])
            back_tracking(i)
            arr.pop()

back_tracking(0)
