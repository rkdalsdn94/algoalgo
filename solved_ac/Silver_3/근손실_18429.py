# 백준 - 실버3 - 근손실 - 18429 - 완전 탐색, 백 트래킹 문제
'''
완전 탐색, 백 트래킹 문제

solved 문제 분류 상의 풀이는 백 트래킹이 있는데, 순열을 활용한 완전 탐색 방식으로만 풀었다. (permutations 이용)
 - 입력 범위가 적어서 충분히 가능할 것으로 생각했다.
 - 나중에 백 트래킹으로 다시 풀어봐야겠다.
    - 백 트래킹을 체그하기 위한 ck 리스트를 n_list의 크기로 둔 뒤, 방문을 체크하면서 back_tracking 함수를 재귀로 실행하면 됨. (인자로 idx, num을 두고?)

풀이 과정
 - 입력값들을 받은 뒤, n_list의 값들을 n의 크기로 permuations을 돌린다.
    - 함수를 실행하기 전에 num을 500으로 초기화해야 된다.
    - 위 순열의 값을 ck 함수로 전달한 뒤 num에서 k를 빼고, arr의 값을 더하면서 num이 500 미만으로 떨어지는지 검사한다.
    - 500 미만으로 떨어지면 즉시 0을 return하고, 순열로 구한 리스트를 모두 반복해도 500보다 크거나 같다면 1을 return 한다.
 - 위 함수의 값을 res에 더해주고, 추력하면 된다.
'''

from itertools import permutations

n, k = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, k = 3, 4
# n_list = [3, 7, 5] # 4

res = 0

def ck(arr):
    global num

    for i in arr:
        num -= k
        num += i

        if num < 500:
            return 0
    return 1

for i in permutations(n_list, n):
    num = 500
    res += ck(i)

print(res)
