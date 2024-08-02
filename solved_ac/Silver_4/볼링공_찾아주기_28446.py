# 백준 - 실버4 - 볼링공 찾아주기 - 28446 - 구현, 해시 문제
'''
구현, 해시 문제

단순한 해시(딕셔너리) 문제이다.

풀이 과정
 1. 요청의 개수(m)를 입력 받고, 요청들(m_list)을 입력 받는다.
 2. m_list의 값을 꺼내 요청이 1이면 dict에 볼링 공의 무게인 c를 key로, 사물함 번호인 b를 value로 저장한다.
 3. 요청이 2이면 dict에서 볼링 공의 무게인 b를 key로 value를 출력한다.
'''

import sys; input=sys.stdin.readline

m = int(input())
m_list = [list(map(int, input().split())) for _ in range(m)]

# 테스트
# m = 5
# m_list = [
#     [1, 5, 900], [1, 7, 300], [1, 15, 100],
#     [2, 300], [2, 100]
# ] # 7  \  15
# m = 4
# m_list = [
#     [1, 900, 1], [2, 1]
#     [1, 1, 10000], [2, 10000]
# ] # 900  \  1

res = dict()

for i in m_list:
    if i[0] == 1:
        a, b, c = i
        res[c] = b

    elif i[0] == 2:
        a, b = i
        print(res[b])
