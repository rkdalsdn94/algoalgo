# 백준 - 실버5 - 줄 세우기 - 11536 - 단순 구현, 정렬 문제
'''
단순 구현, 정렬 문제

정렬한 값이 오름차순인지 내림차순인지 확인 후 해당 값을 출력하면 된다.
둘 다 아닐경우 NEITHER을 출력하면 된다.
'''

n = int(input())
n_list = [ input() for _ in range(n) ]

# 테스트
# n = 5
# n_list = ['JOE','BOB','ANDY','AL','ADAM'] # DECREASING
# n = 11
# n_list = ['HOPE', 'ALI', 'BECKY', 'JULIE', 'MEGHAN', 'LAUREN',
#             'MORGAN', 'CARLI', 'MEGAN', 'ALEX', 'TOBIN'] # NEITHER
# n = 4
# n_list = ['GEORGE','JOHN','PAUL','RINGO'] # INCREASING

INCREASING = False
DECREASING = False

if n_list == sorted(n_list):
    INCREASING = True
elif n_list == sorted(n_list, reverse=True):
    DECREASING = True

if INCREASING:
    print('INCREASING')
elif DECREASING:
    print('DECREASING')
else:
    print('NEITHER')
