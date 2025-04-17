# 백준 - 브론즈1 - Falling Apart - 15008 - 그리디, 정렬 문제
"""
그리디, 정렬 문제

[핵심 아이디어]
    1. 각 플레이어는 매 턴 가장 큰 값을 가져가는 것이 최적 전략
    2. 정수 조각들을 내림차순으로 정렬하여 번갈아 가져가도록 함
    3. Alice가 먼저 시작하므로 짝수 인덱스(0, 2, 4...)의 조각을 가져감

[풀이 과정]
    1. 주어진 정수 조각들을 내림차순으로 정렬
    2. Alice는 0, 2, 4... 인덱스의 조각을, Bob은 1, 3, 5... 인덱스의 조각을 가져감
    3. 각자 가져간 조각들의 합을 계산하여 출력
"""

n = int(input())
pieces = list(map(int, input().split()))

# 테스트
# n = 3
# pieces = [3, 1, 2] # 4 2
# n = 4
# pieces = [1, 2, 2, 1] # 3 3

pieces.sort(reverse=True)

alice_score = sum(pieces[0::2])  # 0, 2, 4, ... 번째 조각 (Alice 차례)
bob_score = sum(pieces[1::2])    # 1, 3, 5, ... 번째 조각 (Bob 차례)

print(alice_score, bob_score)
