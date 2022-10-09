# 백준 - 실버4 - 대칭 차집합 - 1269 - 자료 구조, 집합(set)
'''
자료 구조(set), 집합 문제

set 자료 구조를 이용해 -, + 를 한 후에 출력하면 된다.
'''

a, b = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

# 테스트
# a, b = 3, 5
# a_set = set([1,2,4])
# b_set = set([2,3,4,5,6]) # 4

print(len(a_set - b_set) + len(b_set - a_set))
