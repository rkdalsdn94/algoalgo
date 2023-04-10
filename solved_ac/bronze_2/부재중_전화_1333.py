# 백준 - 브론즈2 - 부재중 전화 - 1333 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

n : 총 노래의 곡
l : 노래의 길이
d : 전화벨이 울리는 시간 간격

완전 탐색처럼 풀었다.

전체 시간(total_time)만 구하면 풀기 쉬워진다. -> 전체 시간은  n * l + (5 * n)로 구하면 된다.
왜 인지는 노래의 총 곡(n) * 노래 시간(l) + 중간 쉬는 시간이 노래 만큼 있으니까 (5 * n)

total_time만큼 res list를 1로 초기화한다.
노래를 듣는 부분을 0으로 만든 후, 전체 시간만큼 반복하면서 범위를 d로 한 뒤, res가 1인 부분이 있으면 해당 번째를 출력하고,
없으면 i + d를 출력하면 된다.
'''

n, l, d = map(int, input().split())

# 테스트
# n, l, d = 2, 5, 7 # 7
# n, l, d = 4, 5, 20 # 40
# n, l, d = 6, 9, 20 # 40

total_time = n * l + (5 * n)
res = [1] * total_time

for i in range(0, total_time, l + 5):
    for j in range(i, i + l): # 노래를 듣는 중엔 전화를 못 받는다.
        res[j] = 0

for i in range(0, total_time, d):
    if res[i]:
        print(i)
        break
else:
    print(i + d)
