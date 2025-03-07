# 프로그래머스 - Lv1 - 덧칠하기 - 그리디, 시뮬레이션 문제
'''
그리디, 시뮬레이션 문제

[핵심 아이디어]
    1. 칠해야 할 구역을 순차적으로 확인하면서 롤러의 최적 위치 결정
    2. 칠해지지 않은 구역을 발견하면 해당 위치에서 롤러 크기만큼 한 번에 칠하기
    3. 롤러를 사용한 후에는 롤러 크기(m)만큼 인덱스를 이동시켜 중복 작업 방지

[풀이 과정]
    1. 전체 벽을 나타내는 배열을 생성하고, 초기에는 모든 벽이 칠해진 상태(1)로 설정
    2. 다시 칠해야 하는 구역을 0으로 표시 (section 배열 기반).
    3. 벽을 처음부터 순회하며:
       a. 이미 칠해진 부분(값이 1)은 건너뜀
       b. 칠해야 할 부분(값이 0)을 발견하면 롤러로 m 길이만큼 칠하기
       c. 롤러 사용 횟수(answer)를 증가시키고, 인덱스를 롤러 길이(m)만큼 이동
    4. 모든 벽의 처리가 완료되면 최종 롤러 사용 횟수를 반환
'''

def solution(n, m, section):
    answer = 0
    idx = 0
    wall_list = [1] * n

    for i in section:
        wall_list[i - 1] = 0

    while idx < n:
        if wall_list[idx] == 1:
            idx += 1
            continue

        for i in range(idx, idx + m):
            if i >= n:
                break
            wall_list[i] = 1

        idx += m
        answer += 1

    return answer

print(solution(8, 4, [2, 3, 6]) == 2)
print(solution(5, 4, [1, 3]) == 1)
print(solution(4, 1, [1, 2, 3, 4]) == 4)
