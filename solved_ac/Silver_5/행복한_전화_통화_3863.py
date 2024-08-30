# 백준 - 실버5 - 행복한 전화 통화 - 3863 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

source와 destination은 필요 없는 정보이다. 여기에 낚여서 시간을 많이 쏟으면 안 된다.
총 전화 구간인 calls 도청이 필요한 구간인 segments를 사용해서 풀었다.

풀이 과정
    1. n, m을 입력받는다.
    2. n_list와 m_list를 입력받는다.
    3. calls와 segments를 만들어 각각의 값을 넣는다.
        3.1. calls는 n_list의 start와 duration을 넣는다. (calls = [[start, duration], ...]) -> 여기서 낚이면 안 됨
        3.2. segments는 m_list의 start와 duration을 넣는다. (segments = [[start, duration], ...])
    4. res를 만들어서 segments를 돌면서 calls의 start와 duration을 비교한다.
        4.1. 도청이 필요한 구간의 끝(seg_end)을 구한다. (seg_end = seg_start + seg_duration - 1)
        4.2. cnt를 0으로 초기화한다.
        4.3. calls를 돌면서 전화가 끝나는 시간(call_end)을 구한다. (call_end = call_start + call_duration - 1)
        4.4. 만약 call_end가 seg_start보다 크거나 같고, call_start가 seg_end보다 작거나 같으면 cnt를 1 증가시킨다.
        4.5. cnt를 res에 추가한다.
    5. 차례대로 res를 출력하면 된다.

in
    3 2
    3 4 2 5
    1 2 0 10
    6 5 5 8
    0 6
    8 2
    1 2
    8 9 0 10
    9 1
    10 1
    0 0
out
    3
    2
    1
    0
'''

while 1:
    n, m = map(int, input().split())

    if n == m == 0:
        break

    n_list = [list(map(int, input().split())) for _ in range(n)]
    m_list = [list(map(int, input().split())) for _ in range(m)]

    calls = []
    for source, destination, start, duration in n_list:
        calls.append([start, duration])

    segments = []
    for start, duration in m_list:
        segments.append([start, duration])

    res = []
    for seg_start, seg_duration in segments:
        seg_end = seg_start + seg_duration - 1
        cnt = 0

        for call_start, call_duration in calls:
            call_end = call_start + call_duration - 1

            if not (call_end < seg_start or call_start > seg_end):
                cnt += 1

        res.append(cnt)

    for i in res:
        print(i)
