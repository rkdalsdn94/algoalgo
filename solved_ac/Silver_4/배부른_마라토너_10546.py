# 백준 - 실버4 - 배부른 마라토너 - 10546 - 자료 구조(해시)
'''
자료 구조(해시) 문제

해시(딕셔너리)만 활용하면 쉽게 구할 수 있는 문제다.
단, input을 readline 으로 바꾸거나, PyPy3로 제출해야 통과할 수 있다.

해시에 이름으로 들어오는 값을 0부터 1씩 증가시켜 최종적으로 2로 나눴을 때 몫이 0이 되는 값이 통과하지 못한 선수이다.
'''

import sys; input=sys.stdin.readline
n = int(input())
n_list = [input() for _ in range(n * 2 - 1)]

# 테스트
# n = 3
# n_list = ['leo', 'kiki', 'eden', 'eden', 'kiki'] # leo
# n = 5
# n_list = [
#     'marina',
#     'josipa',
#     'nikola',
#     'vinko',
#     'filipa',
#     'josipa',
#     'filipa',
#     'marina',
#     'nikola'
# ] # vinko
# n = 4
# n_list = [
#     'mislav',
#     'stanko',
#     'mislav',
#     'ana',
#     'stanko',
#     'ana',
#     'mislav'
# ] # mislav

res = dict()
for i in n_list:
    if i in res:
        res[i] += 1
    else:
        res[i] = 0

for i, j in res.items():
    if j % 2 == 0:
        print(i)
        exit(0)
