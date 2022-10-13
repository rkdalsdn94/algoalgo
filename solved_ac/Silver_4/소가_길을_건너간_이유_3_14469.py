# 백준 - 소가 길을 건너간 이유 3 - 14469 - 정렬, 그리디 문제
'''
정렬, 그리디 문제

풀이 과정
1. 소의 도착 시간을 기준으로 정렬을 한다. -> 그렇지 않으면 최소 시간을 구할 수 없다.
2. 소의 도착 시간이 현재까지 걸린 시간(res)보다 크면 도착할 때까지 시간이 더 필요하기 때문에 도착할 때까지 걸리는 시간을 res에 더해준다.
    ㄴ> if res < a: 현재까지 진행된 시간(res)보다 소의 도착 시간이 늦을 경우 소가 도착하기까지 걸리는 시간을 더해야 한다.
3. res에 소의 검문 시간을 더한다.
'''

n = int(input())
n_list = sorted([ list(map(int, input().split())) for _ in range(n) ])

# 테스트
# n = 3
# n_list = sorted([ [2,1],[8,3],[5,7] ]) # 15

res = 0

for i in n_list:
    a, b = i

    if res < a:
        res += a - res
    res += b

print(res)
