# 백준 - 브론즈1 - 두부 게임 (Tofu Game) - 14564 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

두부 게임의 모 수를 try, except를 사용하여 입력 받는다.

풀이 과정
1. 입력 값을 입력 받는다. 
    1.1. 주의할 점으론 m_list를 입력 받을 때, try, except를 사용하여 입력 받아야 한다.
2. m_list를 순회하면서 다음을 수행한다.
    2.1. 만약 i가 m // 2 + 1이면 0을 res에 추가하고 반복문을 종료한다.
    2.2. 그렇지 않으면, idx를 계산한다.
    2.3. idx를 res에 추가하고, a에 idx를 할당한다.
3. res를 원소 한개 씩 출력한다.
'''

n, m, a = map(int, input().split())
m_list = []

while True:
    try:
        m_list.append(int(input()))
    except:
        break

# 테스트
# n, m, a = 3, 5, 1
# m_list = [4, 1, 2, 5, 3] # 2  \  3  \  2  \  1  \  0
# n, m, a = 5, 5, 2
# m_list = [4, 5, 4, 2, 3] # 3  \  5  \  1  \  5  \  0
# n, m, a = 6, 7, 5
# m_list = [6, 2, 1, 7, 3, 6, 4] # 1  \  5  \  2  \  5  \  4  \  6  \  0

res = []

for i in m_list:
    if i == (m // 2 + 1):
        res.append(0)
        break
    else:
        idx = (a + i - (m // 2 + 1) - 1) % n + 1
        res.append(idx)
        a = idx

for i in res:
    print(i)
