# 백준 - 실버3 - HJS - 30046 - 완전 탐색, 많은 조건 분기 문제
"""
완전 탐색, 많은 조건 분기

[핵심 아이디어]
    H, J, S에 1~9 중 서로 다른 3개 숫자를 할당하는 경우의 수는 9P3 = 504가지
    문자열이 최대 30만 길이이므로 정수 변환 불가 → 숫자 리스트로 변환 후 비교
    파이썬 리스트 비교는 lexicographic order로 동작하여 숫자 대소 비교와 동일

[풀이 과정]
    1. permutations로 1~9 중 3개를 선택하는 모든 순열 생성 (504가지)
    2. 각 순열에 대해:
       - H, J, S에 숫자 할당
       - P, Q, R을 숫자 리스트로 변환
       - 리스트 비교로 p < q < r 확인 (lexicographic order)
    3. 하나라도 조건 만족 시 "HJS! HJS! HJS!" 출력

"""

from itertools import permutations

n = int(input())
p = input().strip()
q = input().strip()
r = input().strip()

# 테스트
# n = 6
# p = 'HJSHJS'
# q = 'JHSJHS'
# r = 'SHJSHJ' # HJS! HJS! HJS!
# n = 10
# p = 'HHJHSSHJJH'
# q = 'HHJHHJHJJS'
# r = 'HHJSHJHJSJ' # Hmm...

# H, J, S에 1~9 중 3개를 할당하는 모든 경우의 수 (9P3 = 504가지)
found = False
for perm in permutations(range(1, 10), 3):
    h, j, s = perm

    # 문자를 숫자로 매핑
    mapping = {'H': h, 'J': j, 'S': s}

    # P, Q, R을 숫자 리스트로 변환
    p_num = [mapping[c] for c in p]
    q_num = [mapping[c] for c in q]
    r_num = [mapping[c] for c in r]

    # 리스트 비교 (lexicographic order)로 p < q < r 확인
    # [4,7,9] < [7,4,9]는 첫 번째 자리에서 4 < 7이므로 True
    if p_num < q_num < r_num:
        found = True
        break

if found:
    print("HJS! HJS! HJS!")
else:
    print("Hmm...")
