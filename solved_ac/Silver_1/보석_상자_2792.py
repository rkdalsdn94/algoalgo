# 백준 - 실버1 - 보석 상자 - 2792 - 이진 탐색, 매개 변수 탐색 문제
'''
이진 탐색, 매개 변수 탐색 문제

풀이 과정
1. left, right를 1, 보석 중 가장 큰 값으로 설정한다.
2. left가 right보다 작거나 같을 때까지 반복한다.
3. mid를 구하고 cnt를 0으로 초기화한다.
4. 보석을 돌면서 다음을 확인한다.
    4.1. cnt에 i를 mid로 나눈 몫을 더하고 i를 mid로 나눈 나머지가 0이 아니라면 1을 더한다.
5. cnt가 n보다 작거나 같다면 res를 mid로 설정하고 right를 mid - 1로 설정한다.
6. cnt가 n보다 크다면 left를 mid + 1로 설정한다.
7. res를 출력한다.
'''

n, m = map(int, input().split())
jewel = [int(input()) for _ in range(m)]

# 테스트
# n, m = 5, 2
# jewel = [7, 4] # 3
# n, m = 7, 5
# jewel = [7, 1, 7, 4, 4] # 4

left, right = 1, max(jewel)
res = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for i in jewel:
        cnt += i // mid + (1 if i % mid else 0)

    if cnt <= n:
        res = mid
        right = mid - 1
    else:
        left = mid + 1

print(res)
