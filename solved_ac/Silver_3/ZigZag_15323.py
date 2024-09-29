# 백준 - 실버3 - ZigZag - 15323 - 자료 구조(해시), 문자열, 정렬 문제
'''
자료 구조(해시), 문자열, 정렬 문제

해시를 이용해서 정렬을 하고, 출력하면 되는 문제이다.
이때 반복이 가능하게끔 하려면 인덱스와 나머지 연산이 필요하다.

풀이 과정
    1. k와 n을 입력받는다.
    2. k_list와 n_list를 입력받는다.
    3. alpha_dic에 k_list의 첫번째 문자를 키로, k_list를 가으로 저장한다.
    4. alpha_dic의 각 키들에 대한 값들을 정렬하고 저장한다.
    5. alpha_dic의 각 키들에 대한 값들의 개수를 세기 위해 alpha_index를 만들고 0으로 초기화한다.
    6. n_list를 순회하며 alpha_dic의 각 키들에 대한 값들을 res에 append한다.
        6.1. 이때 alpha_index는 인덱스와 나머지 연산을 이용하여 반복이 가능하게끔 한다.
    7. 위에서 구한 res 값들을 출력한다.
'''

k, n = map(int, input().split())
k_list = [input() for _ in range(k)]
n_list = [input() for _ in range(n)]

# 테스트
# k, n = 4, 5
# k_list = ['zagreb', 'split', 'zadar', 'sisak']
# n_list = ['z', 's','s', 'z', 'z'] # zadar  \  sisak  \  split  \  zagreb  \  zadar
# k, n = 5, 3
# k_list = ['london', 'rim', 'pariz', 'moskva', 'sarajevo']
# n_list = ['p', 'r', 'p'] # pariz  \  rim  \  pariz
# k, n = 1, 3
# k_list = ['zagreb']
# n_list = ['z', 'z', 'z'] # zagreb  \  zagreb  \  zagreb

alpha_dic = {}
alpha_index = [0] * 26

for i in k_list:
    if i[0] in alpha_dic:
        alpha_dic[i[0]].append(i)
    else:
        alpha_dic[i[0]] = [i]

for i, j in alpha_dic.items():
    j.sort()
    alpha_dic[i] = j

res = []
for i in n_list:
    res.append(alpha_dic[i][alpha_index[(ord(i) - 97)] % len(alpha_dic[i])])
    alpha_index[(ord(i) - 97)] += 1

for i in res:
    print(i)
