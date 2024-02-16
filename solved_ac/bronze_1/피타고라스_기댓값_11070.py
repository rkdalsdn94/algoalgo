# 백준 - 브론즈1 - 피타고라스 기댓값 - 11070 - 수학, 구현 문제
'''
수학, 구현 문제

문제를 해석하는데 시간이 더 걸린 문제이다.

풀이 과정
 - input 조건에 맞게 입력받는다.
 - team들의 점수를 계산하기 위해 team_list 를 [0: 득점, 0: 실점] 으로 초기화한 뒤 n + 1의 크기로 만든다. (+1은 input값 그대로 사용하기 위해)
 - a와 b팀의 경기에서 a팀이 p 득점을 했으므로 a팀의 득점 위치(0번째)에 p를 더하고, q를 실점했으므로 실점 위치(1번째)에 q를 더한다.
    - 이 과정을 m 만큼 반복하면서 입력을 받고 처리한다.
 - a와 b 팀 득실점이 모두 0점인 경우 res에 0을 append하고, 아닐땐 w를 계산한다.
 - res에 append 된 값중 제일 큰 값과, 제일 작은 값을 int 형으로 출력하면 된다.

in
    2
    3 5
    1 2 3 5
    1 3 10 1
    1 2 0 7
    2 3 9 3
    3 2 4 5
    4 6
    1 2 0 11
    1 3 17 13
    1 4 17 1
    2 3 7 12
    2 4 19 17
    3 4 17 0
out
    871
    100
    753
    103
'''

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    team_list = [[0, 0] for _ in range(n + 1)]

    for _ in range(m):
        a, b, p, q = map(int, input().split())
        team_list[a][0] += p
        team_list[a][1] += q
        team_list[b][0] += q
        team_list[b][1] += p

    res = []
    for i in range(1, n + 1):
        if team_list[i][0] == 0 and team_list[i][1] == 0:
            res.append(0)
            continue

        w = team_list[i][0] ** 2 / (team_list[i][0] ** 2 + team_list[i][1] ** 2)
        res.append(w * 1000)

    print(int(max(res)))
    print(int(min(res)))
