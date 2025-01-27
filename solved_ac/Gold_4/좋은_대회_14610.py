# 백준 - 골드4 - 좋은 대회 - 14610 - 그리디 문제
'''
그리디 문제

핵심 아이디어
    - 각 참가자별로 이미 확실히 풀었거나 풀 수 없는 문제를 먼저 체크한다.
    - 알 수 없는 결과(-1)에 대해서는 남은 풀어야 할 문제 수를 고려하여 가능성을 판단한다.
    - 풀어야 할 문제 수가 알 수 없는 문제의 개수보다 많으면 불가능하다.
    - 마지막 참가자부터 역순으로 처리하여 모든 문제가 최소 한 번은 풀리도록 한다.

풀이 과정
    1. 참가자 수(N)와 문제 수(M)를 입력받고, 문제 풀이 상태 배열을 초기화한다.
    2. 각 참가자별로 처리:
       - 풀어야 할 문제 수와 각 문제의 결과를 입력받는다.
       - 0문제나 전체 문제를 푼 경우 즉시 실패 처리한다.
       - 각 문제별로 1(풀음)인 경우 problems 배열에 표시하고 남은 문제 수를 감소시킨다.
       - -1(알 수 없음)인 경우 해당 문제가 아직 풀리지 않았다면 목록에 추가한다.
       - 남은 문제 수가 음수거나 가능한 문제보다 많으면 실패 처리한다.
    3. 마지막 참가자부터 역순으로:
       - 각 참가자의 남은 문제 수만큼 풀리지 않은 문제를 처리한다.
    4. 모든 문제가 풀렸는지 확인하여 결과를 반환한다.

시간 복잡도: O(N*M) - N은 참가자 수, M은 문제 수
공간 복잡도: O(N*M) - 참가자별 풀 수 있는 문제 목록을 저장

in
    4 5
    4 1 1 -1 -1 -1
    3 1 0 -1 -1 -1
    2 1 0 1 0 -1
    1 1 0 0 0 -1
out
    YES

in
    5 7
    4 1 1 1 -1 -1 -1 -1
    3 1 1 1 0 -1 -1 -1
    3 1 0 1 0 -1 -1 -1
    2 1 0 0 0 1 -1 -1
    1 0 0 1 0 0 -1 -1
out
    NO
'''

def solve_contest():
    # 참가자 수와 문제 수 입력
    n, m = map(int, input().split())
    problems = [0] * m  # 문제 풀이 상태 배열
    unsolved_tasks = []  # 미해결 문제와 참가자 정보를 저장할 리스트

    for participant_idx in range(n):
        # 각 참가자의 정보 입력
        data = list(map(int, input().split()))
        solved_count = data[0]
        results = data[1:]

        # 조건 1, 3 검증: 0문제 또는 모든 문제를 푼 경우
        if solved_count == 0 or solved_count == m:
            return "NO"

        remaining_problems = solved_count
        unknown_indices = []

        # 각 문제 결과 처리
        for problem_idx, result in enumerate(results):
            if result == 1:
                problems[problem_idx] = 1
                remaining_problems -= 1
            elif result == -1:
                # 아직 풀리지 않은 문제만 처리
                if problems[problem_idx] != 1:
                    problems[problem_idx] = -1
                    unknown_indices.append(problem_idx)

        # 남은 문제 수가 음수가 되면 불가능
        if remaining_problems < 0:
            return "NO"

        # 남은 문제 수가 있는 경우만 저장
        if remaining_problems > 0:
            # 풀어야 할 문제 수가 가능한 문제보다 많으면 불가능
            if remaining_problems > len(unknown_indices):
                return "NO"
            unsolved_tasks.append((remaining_problems, unknown_indices))

    # 마지막 참가자부터 처리 (역순)
    while unsolved_tasks:
        remaining, indices = unsolved_tasks.pop()
        for idx in indices:
            # 아직 풀리지 않은 문제만 처리
            if problems[idx] == -1 and remaining > 0:
                problems[idx] = 1
                remaining -= 1

    # 모든 문제가 풀렸는지 확인
    if any(problem != 1 for problem in problems):
        return "NO"

    return "YES"

print(solve_contest())
