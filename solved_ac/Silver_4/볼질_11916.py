# 백준 - 실버4 - 볼질 - 11916 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

아래의 3가지 경우를 처리하면 되는 구현, 시뮬레이션 문제이다.
1 : 볼
2 : 몸에 맞는 공
3 : 폭투

풀이 과정
    1. 입력을 받고, n_list를 만든다.
    2. res, ball_cnt, base_list를 만든다.
    3. n_list를 돌면서 볼, 몸에 맞는 공, 폭투를 처리한다.
    4. 볼 처리는 ball_cnt를 1씩 증가시키고, 4가 되면 주루를 처리한다.
    5. 몸에 맞는 공은 ball_cnt를 4로 바꾼다.
    6. 폭투는 주루를 처리한다.
        6.1. 주루 처리는 3루부터 주루를 처리한다.
    7. 볼 카운트가 4가 되면 주루를 처리한다.
        7.1. 주루 처리는 1루부터 주루를 처리한다.
    8. res를 출력한다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 16
# n_list = [1, 1, 2, 1, 3, 3, 1, 2, 1, 1, 3, 1, 1, 1, 3, 3] # 3

res = 0
ball_cnt = 0
base_list = [0, 0, 0]

for i in n_list:
    if i == 1: # 기본 볼 처리
        ball_cnt += 1
    elif i == 2: # 몸에 맞는 공이 되면 볼 카운트를 4로 바꾼다.
        ball_cnt = 4
    else: # 폭투인 경우 3루부터 주루
        ball_cnt += 1

        # 3루 -> 2루 -> 1루 순으로 검사해야 됨
        if base_list[2]:
            res += 1
            base_list[2] = 0
        if base_list[1]:
            base_list[2] = 1
            base_list[1] = 0
        if base_list[0]:
            base_list[1] = 1
            base_list[0] = 0

    # 볼 넷 카운트가 4가 되면 1루 -> 2루 -> 3루 순으로 검사해야 됨
    if ball_cnt == 4:
        ball_cnt = 0

        if base_list[0]:
            if base_list[1]:
                if base_list[2]:
                    res += 1
                    base_list[2] = 0
                base_list[1] = 0
                base_list[2] = 1
            base_list[0] = 0
            base_list[1] = 1
        base_list[0] = 1

print(res)
