# 백준 - 실버2 - Programiranje - 15355 - 누적 합 문제
'''
누적 합 문제

[핵심 아이디어]
   문자열에서 두 구간이 서로 재배열하여 같은 문자열이 될 수 있는지 판단하는 문제입니다.
   각 알파벳의 출현 빈도를 효율적으로 계산하기 위해 누적 합을 사용합니다.
   각 알파벳별로 누적 합 배열을 만들어 특정 구간의 알파벳 빈도수를 O(1)로 계산할 수 있습니다.
   두 구간에서 각 알파벳의 출현 빈도가 정확히 일치하면 재배열이 가능함을 의미합니다.

[풀이 과정]
   1. 입력값 처리
       - 문자열 S를 입력받습니다
       - 쿼리의 개수 Q를 입력받습니다
       - 각 쿼리마다 네 개의 정수 A, B, C, D를 입력받습니다

   2. 누적 합 전처리
       - 알파벳 26개에 대한 2차원 누적 합 배열을 생성합니다
       - prefix_sum[i][j]는 문자열의 i번째 위치까지 j번째 알파벳의 등장 횟수를 저장합니다
       - 각 위치마다 이전 위치의 모든 알파벳 빈도수를 복사한 후, 현재 위치의 알파벳 카운트를 1 증가시킵니다

   3. 쿼리 처리
       - 각 쿼리마다 두 구간 [A,B]와 [C,D]를 확인합니다
       - 두 구간의 각 알파벳 출현 빈도를 계산합니다
           구간 [P,Q]의 알파벳 빈도 = prefix_sum[Q][알파벳] - prefix_sum[P-1][알파벳]
       - 모든 알파벳의 빈도가 동일하면 "DA", 하나라도 다르면 "NE"를 출력합니다
'''

S = input()
Q = int(input())
q_list = [list(map(int, input().split())) for _ in range(Q)]

# S = 'kileanimal'
# Q = 2
# q_list = [[2, 2, 7, 7], [1, 4, 6, 7]] # DA  \  NE
# S = 'abababba'
# Q = 2
# q_list = [[3, 5, 1, 3], [1, 2, 7, 8]] # DA  \  DA
# S = 'vodevovode'
# Q = 2
# q_list = [[5, 8, 3, 6], [2, 5, 3, 6]] # NE  \  DA

# 알파벳 26개에 대한 누적 합 배열 생성
# prefix_sum[i][j]: i번째 위치까지 j번째 알파벳의 등장 횟수
prefix_sum = [[0] * 26 for _ in range(len(S) + 1)]

# 누적 합 계산
for i in range(len(S)):
    for j in range(26):
        prefix_sum[i + 1][j] = prefix_sum[i][j]

    prefix_sum[i + 1][ord(S[i]) - ord('a')] += 1

# 각 쿼리 처리
for A, B, C, D in q_list:
    # 두 범위의 알파벳 출현 횟수가 동일한지 확인
    is_possible = True

    for i in range(26):
        count_x = prefix_sum[B][i] - prefix_sum[A-1][i]
        count_y = prefix_sum[D][i] - prefix_sum[C-1][i]

        if count_x != count_y:
            is_possible = False
            break

    print("DA" if is_possible else "NE")
