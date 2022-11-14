# 백준 - 부분수열의 합 - 실버2 - 1182 - 완전 탐색, 백트래킹, 자료 구조 문제
'''
완전 탐색, 백트래킹, 자료 구조 문제

solved에서의 문제 분류는 완전 탐색과, 백트래킹 방법을 활용하는 문제라고 나와 있는데,
python 내장 함수인 combinations 자료 구조를 이용해서 단순하게 풀었다.

풀이 과정
1. 입력 값들을 형식에 맞춰 잘 입력 받는다.
2. combinations 자료 구조를 활용해서 부분 집합으로 만든 후 해당 집합의 총 합이 s와 같은지 확인한다.
    2.1 s와 같을때만 res에 1을 더한다.
3. s가 0이면 - 1을 한 후에 출력하고, 0이 아니면 그대로 출력한다.
    3.1 아무것도 뽑지 않는 경우는 제외하기 위해 s가 0일때 -1을 해야된다.
'''

from itertools import combinations as combi

n, s = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, s = 5, 0
# n_list = [-7, -3 ,-2 ,5, 8] # 1

res = 0

for i in range(n + 1):
    temp = combi(n_list, i)

    for j in temp:
        if sum(j) == s:
            res += 1

print(res if s != 0 else res - 1)
