# 백준 - 실버3 - 크면서 작은 수 - 2992 - 완전 탐색, 백 트래킹 문제
'''
완전 탐색, 백 트래킹 문제

itertools 안에 있는 permutations 함수를 이용해 문제를 풀었다.
 - 직접 구현하고 싶다면 백 트래킹으로 구현할 수 있다.

풀이 과정
 - 입력으로 들어오는 x를 조합해야 하므로 permutations에서 x의 길이만큼 만들어 준다.
 - permutations으로 조합된 값을 temp를 이용해 합친 뒤 x보다 큰 값들만 res에 담는다.
 - res가 있을 경우 res 중에서 제일 작은 값을 출력하고, 없다면 0을 출력하면 된다.
'''

from itertools import permutations

x = input()

# 테스트
# x = '156' # 165
# x = '330' # 0
# x = '27711' # 71127

res = []

for i in permutations(x, len(x)):
    temp = ''.join(i)

    if int(temp) > int(x):
        res.append(temp)

print(min(res) if res else 0)
