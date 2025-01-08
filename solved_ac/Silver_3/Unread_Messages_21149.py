# 백준 - 실버3 - Unread Messages - 21149 - 자료 구조(해시) 문제
'''
자료 구조(해시) 문제

핵심 아이디어
    - 메시지를 한 번도 보내지 않은 사람들의 안 읽은 메시지 수
    - 메시지를 한 번 이상 보낸 사람들의 안 읽은 메시지 수
    - 실제로 메시지를 보낸 사람만 저장

풀이 과정
    1. n, m을 입력받는다.
    2. m_list를 입력받는다.
    3. 실제로 메시지를 보낸 사람만 저장
    4. 메시지를 한 번도 보내지 않은 사람들의 안 읽은 메시지 수
    5. 메시지를 한 번 이상 보낸 사람들의 안 읽은 메시지 수
    6. 결과 출력
'''

def solve_message_group(n, m, m_list):
    # 실제로 메시지를 보낸 사람만 저장
    last_read = {}

    for current_time, sender in enumerate(m_list, 1):
        last_read[sender] = current_time

        # 메시지를 한 번도 보내지 않은 사람들의 안 읽은 메시지 수
        never_sent = n - len(last_read)
        total_unread = (never_sent * current_time) + sum(current_time - read_time for read_time in last_read.values())
        print(total_unread)

n, m = map(int, input().split())
m_list = [int(input()) for _ in range(m)]

# 테스트
# n, m = 2, 4
# m_list = [1, 2, 1, 2] # 1  \  1  \  1  \  1
# n, m = 3, 9
# m_list = [1, 2, 3, 2, 1, 3, 3, 2, 1]
# '''
# out
#     2
#     3
#     3
#     4
#     3
#     3
#     5
#     4
#     3
# '''

solve_message_group(n, m, m_list)
