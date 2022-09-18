# 백준 - 캠프가는 영식 - 실버4 - 1590 - 이분 탐색, 완전 탐색 문제
'''
이분 탐색, 완전 탐색 문제

n만큼 주어지는 버스의 최종 시간이 영식이가 버스터미널의 도착 시간(T)보다 작으면 skip(continue)한다.
그게 아니라면 while 반복 문으로 start(0), end(c - 1) 를 만든 후에 이분 탐색을 진행한다.
start와 end를 더하고 나눈 2의 몫으로 mid 값을 정한 후에
해당 mid 인덱스로 t시간 보다 작은 지 큰지 값을 구해가며 start가 end값을 넘어서는 순간 while문을 종료하고
res에 temp(idx)로 정한 값의 - t를 한 후 res에 값을 추가한다.
최종적으로 res에 값이 있으면 해당 list 중에서 제일 작은 수를 출력하고,
res가 비어 있으면 -1을 출력한다.

in
    1 285
    150 50 10
out
    15

in
    1 123456
    123456 10000 1
out
    0

in
    3 1
    270758 196 67
    904526 8930 66
    121164 3160 56
out
    121163

in
    3 1000000
    718571 2557 74
    480573 9706 54
    16511 6660 90
out
    -1

in
    5 395439
    407917 8774 24
    331425 4386 58
    502205 9420 32
    591461 1548 79
    504695 8047 53
out
    1776
'''

n, t = map(int, input().split())
res = []

for _ in range(n):
    s, l, c = map(int, input().split())
    bus_information = [ s + l * i for i in range(c) ]

    if bus_information[-1] < t:
        continue

    start, end = 0, c - 1
    idx = 0

    while start <= end:
        mid = (start + end) // 2

        if bus_information[mid] < t:
            start = mid + 1
        else:
            idx = mid
            end = mid - 1

    res.append(bus_information[idx] - t)

res.sort() # min 함수보다 sort 함수가 더 빠르다.
print( res[0] if res else -1 )
