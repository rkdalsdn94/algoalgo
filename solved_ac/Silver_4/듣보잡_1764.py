'''
in
    3 4
    ohhenrie
    charlie
    baesangwook
    obama
    baesangwook
    ohhenrie
    clinton
out
    2
    baesangwook
    ohhenrie
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
n_list, m_list = [input().strip() for _ in range(n)], [input().strip() for _ in range(m)]

res = sorted(list(set(n_list) & set(m_list)))
print(len(res))
print('\n'.join(res))
