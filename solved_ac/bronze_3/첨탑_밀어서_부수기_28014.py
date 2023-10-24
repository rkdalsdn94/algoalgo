# 백준 - 브론즈3 - 첨탑 밀어서 부수기 - 28014 - 단순 그리디 문제
'''
단순 그리디 문제

입력으로 들어오는 n_list 의 값을 하나 씩 방문하면서 이 전의 값이 이후의 값보다 작거나, 작으면 res를 1씩 더하면 되는 단순하 문제이다.
res를 추가하는 조건으론 작거나 같은 이유가 되는 이뉴는 초과시에만 넘어가기 때문이다.
    (같아도 다시 밀어줘야 함, 참고 - https://www.acmicpc.net/board/view/120862)
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 6
# n_list = [1, 3, 2, 5, 8, 1] # 4
# n = 8
# n_list = [1, 2, 3, 4, 5, 6, 7, 8] # 8

res = 1
for i in range(1, n):
    if n_list[i - 1] <= n_list[i]:
        res += 1

print(res)
