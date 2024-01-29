# 백준 - 브론즈1 - Send me the moon - 15786 - 구현, 그리디, 문자열 문제
'''
구현, 그리디, 문자열 문제

완전 탐색 방식으로 입력으로 들어온 문자열을 매 순간 비교하면서 target과 같은지 찾으면 되는 문제다.
인덱스와 word가 target과 같을 때마다 하나 씩 추가하고, 중간에 target과 같아지거나,
가운데 반복문이 다 끝났을 때 target과 다르다면 false를 출력하고, 나머지는 true를 출력하면 된다.
'''

n, m = map(int, input().split())
target = input()
m_list = [input() for _ in range(m)]

# 테스트
# n, m = 4, 5
# target = 'PPAP'
# m_list = ['PPAPP', 'PPPPA', 'APPPP', 'PPPAP', 'PAPAP'] # true  \  false  \  false  \  true  \  true
# n, m = 3, 2
# target = 'CTP'
# m_list = ['P', 'CHALLENGETHEPROGRAMING'] # false  \  true

for i in m_list:
    idx = 0
    word = ''

    for j in i:
        if target[idx] == j:
            idx += 1
            word += j

            if word == target:
                print('true')
                break

    if word != target:
        print('false')
