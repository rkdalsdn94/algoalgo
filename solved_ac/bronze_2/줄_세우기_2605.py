# 백준 - 브론즈2 - 줄 세우기 - 2605 - 단순 구현, 자료 구조 문제
'''
단순 구현, 자료 구조 문제

리스트에서 insert 함수를 이용하는 단순하 문제이다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 5
# n_list = [0, 1, 1, 3, 2] # 4 2 5 3 1

res = []

for i in range(n):
    res.insert(n_list[i], i + 1)

print(*res[::-1])
