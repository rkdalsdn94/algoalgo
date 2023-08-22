# 백준 - 실버4 - 떡국 - 20937 - 그리디, 에드 훅 문제
'''
그리디, 에드 훅 문제

문제를 푸는 아이디어는 리스트로 들어오는 숫자 중에서 공통된 숫자의 값이 제일 큰 값을 반환하면 되는데, 시간 초과를 받은 방식과 정답으로 통과한 방식이 동일하다.
하지만 두 방식의 차이점은 시간 복잡도에 있다.
시간 초과를 받은 코드에선 count 함수를 써서 n ^ 2 방식이라 시간 초과를 받은거 같다.

따라서 count 함수를 안쓰고 어떻게 공통된 숫자의 값을 체크할 수 있을지 고민하다.
res 리스트를 0으로 초기화 한 뒤에 (떡국 그릇의 최대 사이즈로 초기화 해야 된다. 아니면 런타임 에러) n_list의 값 들을 res에 1씩 더한 다음
res에서 최댓값을 출력하면 된다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 5
# n_list = [4, 2, 3, 1, 2] # 2

res = [0] * 50_001 # 인덱스 에러 방지를 위해 떡국 그릇의 최대 크기로 넣어야 한다.
for i in n_list:
    res[i] += 1

print(max(res))

'''
시간 초과 코드

import sys; input=sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
set_n_list = set(n_list)

# 테스트
# n = 5
# n_list = [4, 2, 3, 1, 2] # 2
# set_n_list = set(n_list)

res = 0

for i in set_n_list:
    res = max(res, n_list.count(i))

print(res)
'''
