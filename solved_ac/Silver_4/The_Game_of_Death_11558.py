# 백준 - 실버4 - The Game of Death - 11558 - 구현, 그래프, 시뮬레이션 문제
'''
구현, 그래프, 시뮬레이션 문제

풀이 과정
 1. 테스트 케이스의 개수 t를 입력받는다.
 2. t만큼 반복하며 n을 입력받는다.
 3. n만큼 반복하며 arr에 값을 입력받는다.
 4. visited 배열을 만들어 0으로 초기화한다.
 5. idx를 0으로 초기화하고 visited[idx]를 1로 바꾼다.
 6. cnt를 0으로 초기화한다.
 7. while문을 돌면서
 8. cnt를 1 증가시키고 idx를 arr[idx] - 1로 바꾼다.
 9. 만약 visited[idx]가 1이면 0을 출력하고 break한다.
 10. 만약 idx가 n - 1이면 cnt를 출력하고 break한다.
 11. visited[idx]를 1로 바꾼다.

in
    1
    7
    2
    3
    4
    5
    6
    7
    1
out
    6
'''

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    visited = [0] * n
    idx = 0
    visited[idx] = 1
    cnt = 0

    while True:
        cnt += 1
        idx = arr[idx] - 1

        if visited[idx] == 1:
            print(0)
            break

        if idx == n - 1:
            print(cnt)
            break

        visited[idx] = 1
