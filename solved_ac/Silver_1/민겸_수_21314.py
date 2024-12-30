# 백준 - 실버1 - 민겸 수 - 21314 - 구현, 그리디 문제
'''
구현, 그리디 문제

풀이 과정
    1. 민겸 수의 최댓값과 최솟값을 구하는 문제
    2. 민겸 수는 'M'과 'K'로 이루어진 문자열
    3. 'M'은 5, 'K'는 1로 치환
    4. 'M'이 연속되면 5의 배수, 'K'가 연속되면 1의 배수
    5. 최댓값은 'M'을 5로, 'K'를 1로 치환
    6. 최솟값은 'M'을 1로, 'K'를 5로 치환

풀이 방법
    1. 최댓값 구하기
        - 'M'이 연속되면 5의 배수로 치환
        - 'K'가 연속되면 1의 배수로 치환
    2. 최솟값 구하기
        - 'M'이 연속되면 1로 치환
        - 'K'가 연속되면 5로 치환
    3. 결과 출력
'''

num = input()

# 테스트
# num = 'MKM' # 501  \  151
# num = 'MKKMMK' # 505500  \  155105
# num = 'MKMM' # 5011  \  1510

def max_res(num):
    res = []
    m_cnt = 0

    for i in range(len(num)):
        if num[i] == 'M':
            m_cnt += 1
        elif num[i] == 'K':
            if m_cnt > 0:
                res.append('5' + '0' * m_cnt)
            else:
                res.append('5')
            m_cnt = 0

    if m_cnt > 0:
        res.append('1' * m_cnt)

    return ''.join(res)

def min_res(num):
    res = []
    m_cnt = 0

    for i in range(len(num)):
        if num[i] == 'M':
            m_cnt += 1
        elif num[i] == 'K':
            if m_cnt > 0:
                res.append('1' + '0' * (m_cnt - 1) + '5')
            else:
                res.append('5')
            m_cnt = 0

    if m_cnt > 0:
        res.append('1' + '0' * (m_cnt - 1))

    return ''.join(res)

print(max_res(num))
print(min_res(num))
