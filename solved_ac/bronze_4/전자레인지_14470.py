# 백준 - 브론즈4 - 전자레인지 - 14470 - 사칙연산, 단순 구현, 시뮬레이션 문제
'''
사칙연산, 단순 구현, 시뮬레이션 문제

간단한 사칙연산 방식으로 풀 수 있다. 문제에 주어진 다음과 같은 조건으로 문제를 풀면된다.
- 고기가 얼어 있고 온도가 0℃ 미만일 때 : 온도가 C초에 1℃씩 오른다.                         --> a가 음수일 때
- 고기가 얼어 있고 온도가 정확히 0℃일 때 : 얼어 있지 않은 상태로 만드는(해동하는) 데 D초가 걸린다. --> a가 음수일 때
- 고기가 얼어 있지 않을 때 : 온도가 E초에 1℃씩 오른다.                                   --> a가 양수일 때

input 데이터는 각각 다음과 같다.
a : 고기의 온도 (a는 -100 이상 100 이하이며, 0이 아니다.)
b : 목표 온도 (B는 1 이상 100 이하이며, A보다 크다.)
c : 얼어 있는 고기를 1℃ 데우는 데 걸리는 시간 c가 주어진다.
d : 얼어 있는 고기를 해동하는 데 걸리는 시간 d가 주어진다.
e : 얼어 있지 않은 고기를 1℃ 데우는 데 걸리는 시간 e가 주어진다.
'''

a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())

# 테스트
# a, b, c, d, e = -10, 20, 5, 10, 3 # 120
# a, b, c, d, e = 35, 92, 31, 50, 11 # 627

res = 0

if a < 0:
    res += (abs(a) * c) + d
    a = 0
res += (b - a) * e

print(res)
