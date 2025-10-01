# 백준 - 실버3 - HJS - 30046 - 완전 탐색, 많은 조건 분기 문제
"""
완전 탐색, 많은 조건 분기

시간 초과 해결

[핵심 아이디어]
    H, J, S에 1~9 중 서로 다른 3개 숫자를 할당하는 경우의 수는 9P3 = 504가지
    P < Q를 만족하려면 처음 다른 문자가 나오는 위치에서 P[i] < Q[i]여야 함
    → 제약 조건을 미리 수집한 후, 이를 만족하는 순열만 확인

[풀이 과정]
    1. P와 Q를 비교해 처음 다른 문자 위치의 제약 조건 수집 (c1 < c2)
    2. Q와 R을 비교해 처음 다른 문자 위치의 제약 조건 수집 (c3 < c4)
    3. 504개 순열 중 두 제약 조건을 모두 만족하는 것이 있는지 O(1) 확인
    4. 하나라도 만족하면 "HJS! HJS! HJS!" 출력
"""

from itertools import permutations

def get_constraint(s1, s2):
    """
    s1 < s2를 만족하기 위한 제약 조건 반환
    처음으로 다른 문자가 나오는 위치에서 s1[i] < s2[i]여야 함
    """
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return s1[i], s2[i]  # (c1, c2) → c1 < c2여야 함
    return None  # 완전히 같은 경우 (조건 만족 불가)

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

# P < Q를 위한 제약 조건
constraint_pq = get_constraint(p, q)
# Q < R을 위한 제약 조건
constraint_qr = get_constraint(q, r)

# 제약 조건이 없으면 (완전히 같으면) 조건 만족 불가
if constraint_pq is None or constraint_qr is None:
    print("Hmm...")
else:
    found = False
    c1, c2 = constraint_pq  # c1 < c2여야 함
    c3, c4 = constraint_qr  # c3 < c4여야 함

    # 504개 순열 중 두 제약 조건을 모두 만족하는 것 찾기
    for perm in permutations(range(1, 10), 3):
        mapping = {'H': perm[0], 'J': perm[1], 'S': perm[2]}

        # 두 제약 조건을 모두 만족하는지 O(1) 확인
        if mapping[c1] < mapping[c2] and mapping[c3] < mapping[c4]:
            found = True
            break

    if found:
        print("HJS! HJS! HJS!")
    else:
        print("Hmm...")
