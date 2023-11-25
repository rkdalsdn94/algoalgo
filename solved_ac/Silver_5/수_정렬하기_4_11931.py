# 백준 - 실버5 - 수 정렬하기 4 - 11931 - 단순 정렬 문제
'''
단순 정렬 문제

PyPy3로 제출해야 된다.
내림차순으로 정렬 후 출력하면 되는 단순한 문제이다.
'''

n = int(input())
n_list = [int(input()) for _ in range(n)]

# 테스트
# n = 5
# n_list = [1, 2, 3, 4, 5] # 5  \  4  \  3  \  2  \  1

for i in sorted(n_list, reverse=True):
    print(i)
