# 백준 - 브론즈1 - 팀 이름 정하기 - 1296 - 구현, 문자열, 정렬 문제
'''
구현, 문자열, 정렬 문제

문제에 주어진 요구사항을 그대로 구현하면 된다. 요구사항은 다음과 같다.

* 이환이가 만든 공식은 사용하려면 먼저 다음 4가지 변수의 값을 계산해야 한다.
  - L = 연두의 이름과 팀 이름에서 등장하는 L의 개수
  - O = 연두의 이름과 팀 이름에서 등장하는 O의 개수
  - V = 연두의 이름과 팀 이름에서 등장하는 V의 개수
  - E = 연두의 이름과 팀 이름에서 등장하는 E의 개수
 ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) mod 100

위에 주어진 요구사항으로 해당 팀 이름과 계산한 값을 res list에 추가한다.
그 다음 res를 정렬한 뒤 출력하면 되는 문제이다.
'''

name = input()
n = int(input())
team_list = [ input() for _ in range(n) ]

# 테스트
# name = 'LOVE'
# n = 3
# team_list = [ 'JACOB', 'FRANK', 'DANO' ] # FRANK

res = []

for i in range(n):
    L = name.count('L') + team_list[i].count('L')
    O = name.count('O') + team_list[i].count('O')
    V = name.count('V') + team_list[i].count('V')
    E = name.count('E') + team_list[i].count('E')
    value = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    res.append([team_list[i], value])

res.sort(key=lambda x: (-x[1], x[0]))
print(res[0][0])