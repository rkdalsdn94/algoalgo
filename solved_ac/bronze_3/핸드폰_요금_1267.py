'''
단순 구현, 수학, 사칙연산 문제

제일 아래 풀이는 중복값이 많을 경우를 생각해서
Counter로 중복값을 한 번만 곱해주기 위해서 해봤는데
그냥 단순하게 푸는게 더 빠르게 동작했다.

풀이 과정은 몫에다 +1 더한 후 곱해주면 되는 단순한 사칙연산 문제이다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n, n_list = 3, [40, 40, 40] # M 45
# n, n_list = 3, [61, 61, 61] # Y M 90
# n, n_list = 2, [61, 10] # Y 40
# n, n_list = 2, [60, 65] # Y M 60

y_score, m_score = 0, 0

for i in n_list:
    y_score += (i // 30 + 1) * 10
    m_score += (i // 60 + 1) * 15

if y_score == m_score:
    print('Y', 'M', y_score)
elif y_score > m_score:
    print('M', m_score)
else:
    print('Y', y_score)

'''
from collections import Counter

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n, n_list = 3, [40, 40, 40] # M 45
# n, n_list = 3, [61, 61, 61] # Y M 90
# n, n_list = 2, [61, 10] # Y 40
# n, n_list = 2, [60, 65] # Y M 60

y_score, m_score = 0, 0

for i, j in Counter(n_list).items():
    y_score += (i // 30 + 1) * 10 * j
    m_score += (i // 60 + 1) * 15 * j

if y_score == m_score:
    print('Y', 'M', y_score)
elif y_score > m_score:
    print('M', m_score)
else:
    print('Y', y_score)
'''