# 백준 - 브론즈1 - Game - 21623 - 구현 문제
"""
구현 문제

[핵심 아이디어]
    1. 각 라운드는 점수 n에서 시작하며, 생성기 값을 빼서 0이 되면 라운드 종료
    2. 빼기 연산 결과가 음수면 무시 (점수 유지)
    3. 마지막 움직임이 라운드를 끝냈다면 새 라운드를 시작하지 않으므로 점수는 0

[풀이 과정]
    1. 현재 점수를 n으로 초기화하고 라운드 카운터를 0으로 설정
    2. 각 움직임마다 다음을 수행
       - 현재 점수에서 움직임 값을 뺄 수 있으면 빼기
       - 결과가 0이면 라운드 증가, 다음 움직임을 위해 점수를 n으로 재설정
    3. 모든 움직임 처리 후:
       - 점수가 n이고 라운드가 1개 이상이면 → 마지막이 라운드 종료 → 점수 = 0
    4. 라운드 수와 최종 점수 출력
"""

k, n = map(int, input().split())
moves = list(map(int, input().split()))

# 테스트
# k, n = 4, 3
# moves = [1, 2, 4, 1] # 1  \  2

current_score = n  # 현재 점수
rounds = 0  # 완료된 라운드 수

# 각 움직임 처리
for move in moves:
    # 현재 점수에서 뺄 수 있는 경우에만 빼기
    if current_score >= move:
        current_score -= move

        # 점수가 0이 되면 라운드 종료
        if current_score == 0:
            rounds += 1
            current_score = n  # 다음 움직임을 위해 점수 재설정

# 마지막 움직임이 라운드를 끝냈는지 확인
# (점수가 n이고 라운드가 1개 이상이면 마지막 움직임에서 라운드가 종료된 것)
if current_score == n and rounds > 0:
    current_score = 0

print(rounds)
print(current_score)
