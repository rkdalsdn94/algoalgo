# 백준 - 실버2 - On My Way Dorm - 27868 - 문자열, 애드 훅 문제
'''
문자열, 애드 훅 문제

문제의 분류가 애드 훅이 있는지 모르고 직접 풀려고 고생을 했다가 시간 초과가 나왔다.
어떻게 풀어야 될 지 도저히 감이 안와서 다른 사람의 풀이를 참고하니.. 너무 너무 간단했다.
문자열을 뒤집어서 풀면 되는 문제이다.
왔던 길이니까 그대로 돌아가면 된다.

[핵심 아이디어]
    - 어떤 경로로 이동했다면, 그 경로를 그대로 돌아가면 된다.

[풀이 과정]
    1. 입력으로 받은 command 문자열을 뒤집습니다 (command[::-1]).
    2. 뒤집은 문자열이 자동으로 올바른 해답이 됩니다. 이것이 가능한 이유는:
        - 속도 변화가 각 층에서 동일하게 적용됩니다
        - 명령어를 뒤집으면 이전 경로의 각 상태가 역순으로 정확히 재현됩니다
        - 원래 명령어가 유효했다면, 뒤집은 명령어도 반드시 유효합니다
'''

N, S = map(int, input().split())
A = list(map(int, input().split()))
command = input()

# 테스트
# N, S = 6, 1
# A = [1, 1, 1, 1, 1, 2]
# command = '++0-' # -+00+ 인데 -0++가 나와도 괜찮음
# N, S = 10, 3
# A = [5, 3, 2, 7, 1, 4, 3, 1, 6, 5]
# command = '++--+' # -0+- 인데, +--++가 나와도 괜찮음

print(command[::-1])

'''
처음 생각한 시간 초과 코드

def simulate_elevator(n, n_list, start_floor, command):
    # 현재 위치와 속도 초기화
    curr_floor = start_floor
    velocity = 0

    # 각 커맨드에 대해 시뮬레이션
    for cmd in command:
        # 속도 변화 계산
        if cmd == '+':
            velocity += n_list[curr_floor - 1]
        elif cmd == '-':
            velocity -= n_list[curr_floor - 1]

        # 새로운 위치 계산
        curr_floor += velocity

        # 유효성 검사
        if curr_floor < 1 or curr_floor > n:
            return False, 0

    # 최종 속도가 0이어야 함
    return curr_floor, velocity == 0

def find_return_command(n, s, n_list, command):
    # 출근 커맨드로 도착하는 층 찾기
    end_floor, valid = simulate_elevator(n, n_list, s, command)
    if not valid:
        return None

    # 가능한 모든 커맨드 조합 시도 (에드훅 알고리즘)
    def try_commands(length):
        commands = ['']
        valid_commands = []

        while commands:
            curr_cmd = commands.pop()

            if len(curr_cmd) == length:
                # 시뮬레이션 실행
                final_floor, is_valid = simulate_elevator(n, n_list, end_floor, curr_cmd)
                if is_valid and final_floor == s:
                    valid_commands.append(curr_cmd)
                continue

            # 다음 가능한 커맨드 추가
            for next_cmd in ['+', '-', '0']:
                commands.append(curr_cmd + next_cmd)

        return valid_commands[0] if valid_commands else None

    # 길이를 1부터 증가시키며 가능한 커맨드 찾기
    for length in range(1, len(command) * 2):
        result = try_commands(length)
        if result:
            return result

    return None

n, s = map(int, input().split())
n_list = list(map(int, input().split()))
command = input()

# 테스트
# n, s = 6, 1
# n_list = [1, 1, 1, 1, 1, 2]
# command = '++0-' # -+00+
# n, s = 10, 3
# n_list = [5, 3, 2, 7, 1, 4, 3, 1, 6, 5]
# command = '++--+' # -0+-

print(find_return_command(n, s, n_list, command))
'''
