'''
그리디, 구현, 문자열 문제

S로만 주어졌을 때는 문자열의 길이 그대로 출력하면 된다.
LL이 주어졌을 땐 ll의 길이만큼 뺀 후에 1을 더하면 된다.
'''

n = int(input())
n_list = input()

# 테스트
# n = 3
# n_list = 'SSS' # 3
# n = 4
# n_list = 'SLLS' # 4
# n = 9
# n_list = 'SLLLLSSLL' # 7

ll_ck = n_list.count('LL')

if ll_ck <= 1:
    print(len(n_list))
else:
    print(len(n_list) - ll_ck + 1)
