# 백준 - 실버4 - 붙임성 좋은 총총이 - 26069 - 자료 구조(해시) 문제
'''
자료 구조(해시) 문제

해시(파이썬에선 set)을 이용하는 문제이다.
처음 res에 set으로 'ChongChong'을 넣어놓고, 입력받은 n_list의 값 중 res에 들어가 있다면 i, j를 다 add 한다.
    - 어차피 중복은 제거되므로 다 add해도 된다.
    - 또한, 문제의 범위가 크지 않으므로 속도도 상관없다.
그 후 res의 길이를 출력하면 되는 간단한 문제이다.
'''

n = int(input())
n_list = [list(input().split()) for _ in range(n)]

# 테스트
# n = 12
# n_list = [
#     ['bnb2011', 'chansol'], ['chansol', 'chogahui05'], ['chogahui05', 'jthis'],
#     ['jthis', 'ChongChong'], ['jthis', 'jyheo98'], ['jyheo98', 'lms0806'],
#     ['lms0806', 'pichulia'], ['pichulia', 'pjshwa'], ['pjshwa', 'r4pidstart'],
#     ['r4pidstart', 'swoon'], ['swoon', 'tony9402'], ['tony9402', 'bnb2011']
# ]

res = set(['ChongChong'])

for i, j in n_list:
    if i in res or j in res:
        res.add(i)
        res.add(j)

print(len(res))
