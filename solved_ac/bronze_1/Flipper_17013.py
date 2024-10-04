# 백준 - 브론즈1 - Flipper - 17013 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

V : 좌우 반전
H : 상하 반전

풀이 과정
    1. sequence를 입력받는다.
    2. sequence를 순회하며 V일 때와 H일 때를 구분한다.
    3. V일 때와 H일 때를 구분하여 res를 변경한다.
        3.1. V일 때는 res[0]과 res[1]을 바꾼다.
        3.2. H일 때는 res[0]의 0번째와 1번째를 바꾼다.
    4. res를 출력한다.
'''

sequence = input()

# 테스트
# sequence = 'HV' # 4 3  \  2 1
# sequence = 'VVHH' # 1 2  \  3 4

res = [[1, 2], [3, 4]]

for s in sequence:
    if s == 'H':
        res[0], res[1] = res[1], res[0]
    else:
        res[0][0], res[0][1], res[1][0], res[1][1] = res[0][1], res[0][0], res[1][1], res[1][0]

for r in res:
    print(*r)
