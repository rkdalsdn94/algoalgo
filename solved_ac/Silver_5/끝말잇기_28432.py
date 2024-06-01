# 백준 - 실버5 - 끝말잇기 - 28432 - 구현, 문자열 문제
'''
구현, 문자열 문제

풀이 과정
 1. n과 m을 입력받고, n_list와 m_list를 입력받는다.
 2. n_list에서 '?'의 인덱스를 찾고, '?'의 인덱스가 0이면 pre를 찾고, '?'의 인덱스가 n-1이면 next를 찾는다.
 3. '?'의 인덱스가 0이면 pre와 m_list의 첫 번째 문자열의 첫 번째 문자가 같고, m_list의 첫 번째 문자열이 n_list에 없으면 res에 m_list의 첫 번째 문자열을 저장한다.
 4. '?'의 인덱스가 n-1이면 next와 m_list의 첫 번째 문자열의 마지막 문자가 같고, m_list의 첫 번째 문자열이 n_list에 없으면 res에 m_list의 첫 번째 문자열을 저장한다.
 5. '?'의 인덱스가 0이나 n-1이 아니면 pre, next를 찾고, pre의 마지막 문자와 next의 첫 번째 문자가 같고, m_list의 첫 번째 문자열이 n_list에 없으면 res에 m_list의 첫 번째 문자열을 저장한다.
 6. res를 출력한다.
'''

n = int(input())
n_list = [input() for _ in range(n)]
m = int(input())
m_list = [input() for _ in range(m)]

# 테스트
# n = 5
# n_list = ['charlie', 'echo', '?', 'romeo', 'oscar']
# m = 3
# m_list = ['alfa', 'oscar', 'or'] # or

res = 0
question_mark_idx = n_list.index('?')

if n == 1:
    print(m_list.pop())
    exit(0)

if question_mark_idx == 0:
    pre = n_list[question_mark_idx + 1]

    for i in m_list:
        if i[-1] == pre[0] and i not in n_list:
            res = i
            break

elif question_mark_idx == n - 1:
    next = n_list[question_mark_idx - 1]

    for i in m_list:
        if i[0] == next[-1] and i not in n_list:
            res = i
            break
else:
    pre = n_list[question_mark_idx - 1]
    next = n_list[question_mark_idx + 1]

    for i in m_list:
        if pre[-1] == i[0] and i[-1] == next[0] and i not in n_list:
            res = i
            break

print(res)
