# 백준 - 카드 놓기 - 5568 - 자료 구조(permutations), 완전 탐색, 집합 문제
'''
자료 구조(permutations), 완전 탐색, 집합 문제

permutations 자료 구조를 활용해서 편하게 풀었다.
나중에 재귀로 구하는 방식을 따로 풀어봐도 좋을거 같다.

python 내장 함수인 permutations을 이용해서 k개의 순열을 구한다.
permutations을 이용해서 만든 글자를 temp에 담는다.
temp 글자를 res에 추가한다음에 마지막 res의 길이를 출력하면 된다.
'''

from itertools import permutations

n = int(input())
k = int(input())
n_list = [ input() for _ in range(n) ]

# 테스트
# n = 4
# k = 2
# n_list = ['1','2','12','1'] # 7
# n = 6
# k = 3
# n_list = ['72','2','12','7', '2', '1'] # 68

res = set()

for i in permutations(n_list, k):
    temp = ''.join(map(str, i))
    res.add(temp)

print(len(res))
