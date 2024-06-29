# 백준 - 실버4 - 차집합 - 1822 - 자료 구조(해시), 정렬 문제
'''
자료 구조(해시), 정렬 문제

단순한 자료 구조 문제이다.
A와 B의 차집합을 구하는 문제이다.

풀이 과정
 1. A와 B의 원소를 입력 받는다.
 2. A와 B의 차집합을 구한다.
 3. 차집합이 존재하면 차집합의 길이와 원소를 출력한다.
 4. 차집합이 존재하지 않으면 0을 출력한다.
'''

a, b = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

# 테스트
# a, b = 4, 3
# a_list = [2, 5, 11, 7]
# b_list = [9, 7, 4] # 3  \  2 5 11
# a, b = 3, 5
# a_list = [2, 5, 4]
# b_list = [1, 2, 3, 4, 5] # 0

res = list(a_set - b_set)

if res:
    print(len(res))
    print(*sorted(res))
else:
    print(0)
