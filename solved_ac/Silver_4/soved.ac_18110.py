# 백준 - 실버4 - solved.ac - 18110 - 구현, 수학, 정렬 문제
'''
구현, 수학, 정렬 문제

n의 15%를 절사 평균 값으로 둔다.
n_list를 정렬한 후 앞과 뒤에서 절사 평균의 범위에 속한 값을 제거한다.
나머지 원소들의 평균을 출력하면 된다.
단, python에서는 사사오입이라는 반올림을 사용한다고 한다.
이 문제에서는 오사오입이 필요해서 그걸 따로 구현하거나 + 0.0000001을 더한 뒤 round 함수를 사용하면 된다.
해당 문제에선 my_round 함수를 구현했다. (0.5를 더한 뒤 내림처리)

in
    5
    1
    5
    5
    7
    8
out
    6
in
    10
    1
    13
    12
    15
    3
    16
    13
    12
    14
    15
out
    13
'''

import sys; input=sys.stdin.readline

n = int(input())
n_list = sorted([ int(input()) for _ in range(n) ])

# 테스트
# n = 5
# n_list = sorted([1, 5, 5, 7, 8]) # 6
# n = 10
# n_list = sorted([1, 13, 12, 15, 3, 16, 13, 12, 14, 15]) # 13

def my_round(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)

if n:
    n_list = sorted([int(input()) for _ in range(n)])
    trimmed_mean = my_round(n * 0.15)
    print(my_round(sum(n_list[trimmed_mean:-trimmed_mean] if trimmed_mean else n_list) / (n - 2 * trimmed_mean)))
else:
    print(0)