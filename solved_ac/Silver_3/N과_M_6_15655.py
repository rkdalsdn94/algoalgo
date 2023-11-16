# 백준 - 실버3 - N과 M 6 - 15655 - 백 트래킹 문제
'''
백 트래킹 문제

다른 N과 M 문제들과 똑같이 백 트래킹 방식으로 풀면 된다.
전의 방법들과 유사하고, 코드도 읽기 어렵지 않아서 풀이는 따로 안 적으려고 한다.
그래도 이해가 잘 안 되면 https://pythontutor.com/render.html#mode=display 여기서 확인하면 된다.
'''

n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))

# 테스트
# n, m = 3, 1
# n_list = sorted([4, 5, 2]) # 2  \  4  \  5
# n, m = 4, 2
# n_list = sorted([9, 8, 7, 1]) # 1 7  \  1 8  \  1 9  \  7 8  \  7 9  \  8 9
# n, m = 4, 4
# n_list = sorted([1231, 1232, 1233, 1234]) # 1231 1232 1233 1234

res = []
ck = [0] * n

def back_tracking(depth, cnt):
    if cnt == m:
        print(*res)
        return

    for i in range(depth, n):
        if ck[i] == 0:
            ck[i] = 1
            res.append(n_list[i])
            back_tracking(i + 1, cnt + 1)
            ck[i] = 0
            res.pop()

back_tracking(0, 0)
