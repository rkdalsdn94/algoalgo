# 백준 - 실버4 - Maximum Word Frequency - 9612 - 자료 구조(해시), 문자열, 정렬 문제
'''
자료 구조(해시), 문자열, 정렬 문제

단순히 해시(딕셔너리)를 이용하여 문제를 풀 수 있다.

풀이 과정
    1. 입력 받기
    2. 딕셔너리를 이용하여 각 단어의 빈도수를 구한다.
    3. 빈도수가 가장 높은 단어를 출력한다.
        3.1. 빈도수가 같은 경우 사전 순으로 출력한다.
'''

n = int(input())
n_list = [input() for _ in range(n)]

# 테스트
# n = 10
# n_list = [
#     'mountain', 'lake', 'lake',
#     'zebra', 'tree', 'lake', 'zebra',
#     'zebra', 'animal', 'lakes'
# ] # zebra 3

dic = {}
for i in n_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

sorted_res = sorted(dic.items(), key=lambda x: (x[1], x[0]), reverse=True)
print(sorted_res[0][0], sorted_res[0][1])
