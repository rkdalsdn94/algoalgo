# 백준 - 실버3 - N과 M 8 - 15657 - 백 트래킹 문제
'''
백 트래킹 문제

전에 풀었던 N과 M 문제들과 같이 백 트래킹 방식으로 풀었다.

res 리스트의 길이가 m과 같아질 때 출력하고 return 하고,
길이가 같지 않을 경우 for 문으로 x부터 시작해서 n까지 res에 담고, 다시 백 트래킹을 실행한다.
for 문 내에서 백 트래킹 함수가 종료 될 때 res를 pop 하면 된다.
'''

n, m = map(int, input().split())
k_list = sorted(list(map(int, input().split())))

# 테스트
# n, m = 3, 1
# k_list = sorted([4, 5, 2]) # 2  \  4  \  5
# n, m = 4, 2
# k_list = sorted([9, 8, 7, 1]) # 1 1  \  1 7  \  1 8  \  1 9  \  7 7  \  7 8  \  7 9  \  8 8  \  8 9  \  9 9
# n, m = 4, 4
# k_list = sorted([1231, 1232, 1233, 1234])
# '''
#     1231 1231 1231 1231
#     1231 1231 1231 1232
#     1231 1231 1231 1233
#     1231 1231 1231 1234
#     1231 1231 1232 1232
#     1231 1231 1232 1233
#     1231 1231 1232 1234
#     1231 1231 1233 1233
#     1231 1231 1233 1234
#     1231 1231 1234 1234
#     1231 1232 1232 1232
#     1231 1232 1232 1233
#     1231 1232 1232 1234
#     1231 1232 1233 1233
#     1231 1232 1233 1234
#     1231 1232 1234 1234
#     1231 1233 1233 1233
#     1231 1233 1233 1234
#     1231 1233 1234 1234
#     1231 1234 1234 1234
#     1232 1232 1232 1232
#     1232 1232 1232 1233
#     1232 1232 1232 1234
#     1232 1232 1233 1233
#     1232 1232 1233 1234
#     1232 1232 1234 1234
#     1232 1233 1233 1233
#     1232 1233 1233 1234
#     1232 1233 1234 1234
#     1232 1234 1234 1234
#     1233 1233 1233 1233
#     1233 1233 1233 1234
#     1233 1233 1234 1234
#     1233 1234 1234 1234
#     1234 1234 1234 1234
# '''

res = []
def back_tracking(x):
    if len(res) == m:
        print(*res)
        return

    for i in range(x, n):
        res.append(k_list[i])
        back_tracking(i)
        res.pop()

back_tracking(0)
