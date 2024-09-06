# 백준 - 실버4 - 참가자 명단 - 23056 - 정렬 문제
'''
정렬 문제

문제에서 주어진 다음의 조건들을 잘 생각하면서 정렬로 해결하면 되는 문제이다.
 - 홀수일 때 청팀, 짝수일 때 백팀
 - 청팀 먼저 출력, 그 후 백팀 출력
 - 각각 팀에 대해 학급을 오름차순으로 출력
 - 각각 학급에 대해 학생의 이름을 길이가 짧은 것부터, 같다면 사전 순으로 출력

풀이 과정
    1. n, m을 입력받는다.
    2. classroom을 만들어 입력을 받는다.
    3. blue_team, white_team을 defaultdict(list)로 만든다.
    4. classroom을 돌면서 다음을 확인한다.
        4.1. i가 홀수라면 blue_team에 추가한다.
        4.2. i가 짝수라면 white_team에 추가한다.
    5. blue_team과 white_team을 정렬하고 다음을 확인한다.
        5.1. blue_team을 돌면서 다음을 확인한다.
            5.1.1. blue_team[i]를 길이와 사전 순으로 정렬한다.
            5.1.2. 출력한다.
        5.2. white_team을 돌면서 다음을 확인한다.
            5.2.1. white_team[i]를 길이와 사전 순으로 정렬한다.
            5.2.2. 출력한다.

in
    4 2
    3 sunyoung
    2 junkyu
    2 dohyun
    1 minjun
    3 kihyun
    2 damin
    4 hyunsu
    0 0
out
    1 minjun
    3 kihyun
    3 sunyoung
    2 dohyun
    2 junkyu
    4 hyunsu
'''

from collections import defaultdict

n, m = map(int, input().split())
classroom = []
while 1:
    a, b = input().split()
    if a == '0' and b == '0':
        break

    a = int(a)
    classroom.append((a, b))

blue_team, white_team = defaultdict(list), defaultdict(list)

for i, j in classroom:
    if i % 2 == 1:
        if len(blue_team[i]) < m:
            blue_team[i].append(j)
    else:
        if len(white_team[i]) < m:
            white_team[i].append(j)

for i in sorted(blue_team):
    blue_team[i].sort(key=lambda x: (len(x), x))

    for j in blue_team[i]:
        print(i, j)

for i in sorted(white_team):
    white_team[i].sort(key=lambda x: (len(x), x))

    for j in white_team[i]:
        print(i, j)
