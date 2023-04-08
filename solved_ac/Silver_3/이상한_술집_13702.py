# 백준 - 실버3 - 이상한 술집 - 13702 - 이진 탐색 문제
'''
이진 탐색 문제

전형적인 이진 탐색 문제이다.
n_list 각각의 요소들을 mid로 나눈 뒤 sum 함수을 이용해 나눠진 값을 더해준다.
위 값을 이용해 k와 값을 비교한 후 이진 탐색을 진행하면 된다.
'''

n, k = map(int, input().split())
n_list = [ int(input()) for _ in range(n) ]

# 테스트
n, k = 2, 3
n_list = [702, 429] # 351

start, end = 1, max(n_list)
res = 0

while start <= end:
    mid = (start + end) // 2
    cnt = sum([i // mid for i in n_list])

    if cnt >= k:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)
