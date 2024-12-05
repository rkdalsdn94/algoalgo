# 백준 - 실버4 - Strping Permutation - 14534 - 구현, 문자열, 완전 탐색, 백 트래킹 문제
'''
구현, 문자열, 완전 탐색, 백 트래킹 문제

python은 permuations 함수를 제공하므로 이를 이용하여 쉽게 순열을 구할 수 있다.

풀이 과정
    1. 입력 받기
    2. permutations를 이용하여 순열을 구한다.
    3. 순열을 출력한다.
'''

from itertools import permutations

n = int(input())
n_list = [input() for _ in range(n)]

# 테스트
# n = 3
# n_list = ['abc', 'zxyw', 'p7*']
# '''
#     Case # 1:
#     abc
#     acb
#     bac
#     bca
#     cab
#     cba
#     Case # 2:
#     zxyw
#     zxwy
#     zyxw
#     zywx
#     zwxy
#     zwyx
#     xzyw
#     xzwy
#     xyzw
#     xywz
#     xwzy
#     xwyz
#     yzxw
#     yzwx
#     yxzw
#     yxwz
#     ywzx
#     ywxz
#     wzxy
#     wzyx
#     wxzy
#     wxyz
#     wyzx
#     wyxz
#     Case # 3:
#     p7*
#     p*7
#     7p*
#     7*p
#     *p7
#     *7p
# '''

for i in range(1, n + 1):
    print(f'Case # {i}:')

    for j in permutations(n_list[i - 1], len(n_list[i - 1])):
        print(''.join(j))
