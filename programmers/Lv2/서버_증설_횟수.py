# 프로그래머스 - 서버 증설 횟수 - 시뮬레이션, 그리디 문제
"""
시뮬레이션, 그리디 문제

[핵심 아이디어]
    1. 각 시간대별로 필요한 서버 수를 계산한다 (이용자 수를 m으로 나눈 몫).
    2. 24시간 동안의 서버 증설 현황을 추적할 배열을 만든다.
    3. 각 시간에서 k시간 전에 증설된 서버는 반납된다.
    4. 현재 운영 중인 서버 수는 add_server 배열의 합으로 계산한다.
    5. 필요한 서버 수가 운영 중인 서버 수보다 많다면, 추가 서버를 증설한다.

[풀이 과정]
    1. 24시간에 대한 서버 증설 현황을 저장할 add_server 배열을 초기화한다.
    2. 각 시간대별로:
       a. k시간 전에 증설된 서버를 반납한다 (k시간 전의 add_server 값을 0으로 설정).
       b. 현재 필요한 서버 수를 계산한다 (이용자 수 / m의 몫).
       c. 현재 운영 중인 서버 수를 add_server 배열의 합으로 계산한다.
       d. 필요한 서버 수가 운영 중인 서버 수보다 많다면, 추가 서버를 증설하고 총 증설 횟수를 업데이트한다.
    3. 총 증설 횟수를 반환한다.
"""

def solution(players, m, k):
    answer = 0
    add_server = [0] * 24

    for i, j in enumerate(players):
        # k시간 전에 증설된 서버 반납
        if i - k >= 0:
            add_server[i - k] = 0

        # 현재 필요한 서버 수 계산 (이용자 수 / m의 몫)
        required_servers = j // m

        # 현재 운영 중인 서버 수가 필요한 서버 수보다 적으면 서버 증설
        if required_servers >= 1 and required_servers > sum(add_server):
            additional_servers = required_servers - sum(add_server)
            add_server[i] = additional_servers
            answer += additional_servers

    return answer

players = [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5]
print(solution(players, 3, 5)) # 7

players = [0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0]
print(solution(players, 5, 1)) # 11

players = [0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
print(solution(players, 1, 1)) # 12
