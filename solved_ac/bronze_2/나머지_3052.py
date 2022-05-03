'''
단순 수학 문제

테스트는 input을 받으면서 나눌수 없어서 따로 리스트 컴프리헨션을 풀어서 했는데 괜찮았다.
'''

n_list = set([ int(input()) % 42 for _ in range(10) ])

# 테스트
# n_list = [1,2,3,4,5,6,7,8,9,10] # 10
# n_list = [42,84,252,420,840,126,42,84,420,126] # 1
# n_list = [39,40,41,42,43,44,82,83,84,85] # 6
# res = set()
# for i in n_list:
#     res.add(i%42)
# print(len(res))

print(len(n_list))
