# 백준 - 실버3 - 걸그룹 마스터 준석이 - 16165 - 자료 구조(해시, 딕셔너리) 문제
'''
자료 구조(해시, 딕셔너리) 문제

두 개의 해시(파이썬에서는 딕셔너리)를 이용해서 풀면 된다.
각 걸그룹의 이름들을 키로 밸류는 팀 이름을 갖는 딕셔너리 - girl_group_team
각 걸그룹의 팀 이름을 키로 걸그룹 이름 리스트를 갖는 딕셔너리 - girl_group_team
위처럼 입력을 준비한 뒤, 팀 또는 멤버 이름을 입력받고, 다음 입력으로 들어오는 커맨들에 따라 딕셔너리를 출력하면 된다.

in
    3 4
    twice
    9
    jihyo
    dahyeon
    mina
    momo
    chaeyoung
    jeongyeon
    tzuyu
    sana
    nayeon
    blackpink
    4
    jisu
    lisa
    rose
    jenny
    redvelvet
    5
    wendy
    irene
    seulgi
    yeri
    joy
    sana
    1
    wendy
    1
    twice
    0
    rose
    1
out
    twice
    redvelvet
    chaeyoung
    dahyeon
    jeongyeon
    jihyo
    mina
    momo
    nayeon
    sana
    tzuyu
    blackpink
'''

n, m = map(int, input().split())
girl_group_team, girl_group_name = {}, {}

for _ in range(n):
    team_name = input()
    member_cnt = int(input())
    member_list = []

    for _ in range(member_cnt):
        name = input()
        girl_group_team[name] = team_name
        member_list.append(name)
    girl_group_name[team_name] = sorted(member_list)

for _ in range(m):
    team_name_or_name = input()
    command = int(input())

    if command == 1:
        print(girl_group_team[team_name_or_name])
    else:
        print('\n'.join(girl_group_name[team_name_or_name]))
