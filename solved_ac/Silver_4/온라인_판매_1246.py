# 백준 - 온라인 판매 - 1246 - 실버4 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

달걀 수(n)와 고객 수(m)를 입력 받고 각 고객의 달걀 가격(m_list)을 입력받은 후 해당 리스트를 정렬한다.
총 달걀 수를 넘지 않으며, m_list에서 i - 1번째의 고객은 빼고 남은 고객의 수로 수익을 계산한 후 res에 append 한다.
res의 값에서 가장 큰 값이 답이고, 해당 값으로 몇 번째 인덱스인지 찾으면 책정한 가격과 수익을 알 수 있다.
'''

n, m = map(int, input().split())
m_list = sorted([ int(input()) for _ in range(m) ])

# 테스트
# n, m = 5, 4
# m_list = sorted([ 2, 8, 10, 7 ]) # 7 21

res = []

for i in range(m):
    temp = m_list[i] * (m - i) if m - i <= n else n
    res.append(temp)

print(m_list[res.index(max(res))], max(res))
