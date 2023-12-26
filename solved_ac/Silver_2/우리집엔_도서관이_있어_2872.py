# 백준 - 실버2 - 우리집엔 도서관이 있어 - 2872 - 그리디 문제
'''
그리디 문제

입력으로 들어오는 책 리스트(n_list) 중 역순으로 검사하면서 내림차순으로 정렬되어 있는지만 검사하면 된다.
다른 사람 코드를 확인해보면 res 변수를 안 써도 된다. (n_list[i]와 n의 값이 같을 때 n을 1씩 빼고, n을 출력하면 됨)
'''

import sys; input = sys.stdin.readline

n = int(input())
n_list = [int(input()) for _ in range(n)]

# 테스트
# n = 3
# n_list = [3, 2, 1] # 2
# n = 4
# n_list = [1, 3, 4, 2] # 2

res = 0

for i in range(n - 1, -1, -1):
    if n_list[i] != n:
        res += 1
    else:
        n -= 1

print(res)
