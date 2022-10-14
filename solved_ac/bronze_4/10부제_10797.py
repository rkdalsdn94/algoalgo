# 백준 - 10부제 - 브론즈4 - 10797 - 단순 구현 문제
'''
단순 구현 문제

n_list 중에 n이 몇번 들어가 있는지 출력하면 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 1
# n_list = [1,2,3,4,5] # 1
# n = 3
# n_list = [1,2,3,5,3] # 2
# n = 5
# n_list = [1,3,0,7,4] # 0

res = n_list.count(n)

print(res)
