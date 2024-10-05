# 백준 - 실버3 - 가희와 키워드 - 22233 - 자료 구조(해시), 문자열, 파싱 문제
'''
자료 구조(해시), 문자열, 파싱 문제

키워드를 입력받고, 키워드를 포함하는 문장을 입력받는다.
키워드를 포함하는 문장의 개수를 출력하는 문제이다.
이 문제를 풀 때 해시를 사용해야 한다. (set, list는 시간 초과)

풀이 과정
    1. n, m을 입력받는다.
    2. n_dict에 키워드를 입력받는다.
    3. m_list를 입력받는다.
    4. m_list를 순회하며 n_dict에 있는 키워드를 찾아 개수를 센다.
        4.1. 키워드가 있다면 res에서 1씩 뺀다.
    5. 개수를 출력한다.
'''

import sys
input=sys.stdin.readline

n, m = map(int, input().split())
n_dict = {input().rstrip(): 1 for _ in range(n)}
m_list = [list(input().rstrip().split(',')) for _ in range(m)]

# 테스트
# n, m = 5, 2
# n_dict = {'map': 1, 'set': 1, 'dijkstra': 1, 'floyd': 1, 'os': 1}
# m_list = [list('map,dijkstra'.split(',')), list('map,floyd'.split(','))] # 3  \  2
# n, m = 2, 2
# n_dict = {'gt26cw': 1, '1211train': 1}
# m_list = [list('kiwoom,lottegiant'.split(',')), list('kbo'.split(','))] # 2  \  2

res = n

for i in m_list:
    for j in i:
        if j in n_dict.keys() and n_dict[j] == 1:
            res -= 1
            n_dict[j] = 0

    print(res)
