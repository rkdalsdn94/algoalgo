'''
수학, dp, 게임 이론 문제

n = 1 -> 상근
n = 2 -> 창영
n = 3 -> 상근
n = 4 -> 창영

n을 2로 나눈 나머지가 0이면 창영 아니면 상근이가 이긴다.
'''

n = int(input())

if n % 2 == 0:
    print('CY')
else:
    print('SK')
