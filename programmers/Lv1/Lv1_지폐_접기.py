# 프로그래머스 - Lv1 - [PCCE 기출문제 9번] 지폐 접기 - 구현, 시뮬레이션
'''
[문제 분류]
구현, 시뮬레이션 문제

[핵심 아이디어]
    1. 지폐의 크기가 지갑에 들어갈 때까지 반복해서 접는다.
    2. 매번 더 긴 쪽을 반으로 접는다.
    3. 접은 지폐를 그대로 또는 90도 회전해서 넣을 수 있는지 확인한다.

[풀이 과정]
    1. 지폐가 지갑에 들어갈 수 있는지 확인하는 check 함수를 구현한다.
       - 지폐의 작은 변이 지갑의 작은 변 이하이고, 지폐의 큰 변이 지갑의 큰 변 이하인지 확인
       - 또는 지폐의 작은 변이 지갑의 큰 변 이하이고, 지폐의 큰 변이 지갑의 작은 변 이하인지 확인
    2. 지폐가 들어갈 수 있을 때까지 반복:
       - 지폐의 더 긴 쪽을 찾아 반으로 접는다 (더 긴 쪽을 2로 나누고 소수점 이하는 버림)
       - 접은 횟수(answer)를 1 증가시킨다.
    3. 지폐가 지갑에 들어갈 수 있게 되면 접은 횟수를 반환한다.
'''

def solution(wallet, bill):
    answer = 0

    # 지폐가 지갑에 들어갈 수 있는지 확인
    while not check(bill, wallet):
        if bill[0] > bill[1]:  # 첫 번째 차원이 더 크면
            bill[0] = bill[0] // 2  # 첫 번째 차원을 반으로 접음
        else:  # 두 번째 차원이 더 크거나 같으면
            bill[1] = bill[1] // 2  # 두 번째 차원을 반으로 접음
        answer += 1

    return answer

def check(bill, wallet):
    # 지폐를 그대로 또는 90도 회전해서 지갑에 넣을 수 있는지 확인
    return (min(wallet) >= min(bill) and max(wallet) >= max(bill))

print(solution([30, 15], [26, 13]) == 0)
print(solution([30, 15], [26, 17]) == 1)
print(solution([50, 50], [100, 241]) == 4)
