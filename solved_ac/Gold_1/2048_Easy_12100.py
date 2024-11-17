# 백준 - 골드1 - 2048 (Easy) - 12100 - 구현, 완전 탐색, 시뮬레이션, 백 트래킹 문제
'''
구현, 완전 탐색, 시뮬레이션, 백 트래킹 문제

참고할 수 있는 다양한 자료들이 많다. 이해가 안 가면 해당 영상이나 글들을 참고해보자.

풀이 과정
    1. 5번 이동을 통해 얻을 수 있는 최대값을 구하는 문제
    2. 이동 방향은 상하좌우 4가지
    3. 이동 방향에 따라 이동 처리
    4. 5번 이동 후 최대값 출력

풀이 방법
    1. 이동 함수 생성
        - 행 단위로 이동(같은 값 합치기)
    2. dfs 함수 생성
        - 5번 이동 후 최대값 출력
    3. 결과 출력

in
    3
    2 2 2
    4 4 4
    8 8 8
out
    16
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def move(arr): # 행 단위로 이동(같은 값 합치기)
    for i in range(len(arr)): # 행 개수만큼 처리
        num = 0
        tlst = []

        for n in arr[i]:
            if n == 0:
                continue

            if n == num: # 기준 숫자와 같은 경우 합치기
                tlst.append(num * 2)
                num = 0
            else: # 기준 숫자와 다른 경우
                if num == 0: # 처음 숫자를 만난 경우
                    num = n
                else: # 다른 숫자가 있는 경우
                    tlst.append(num)
                    num = n

        # 종료 후 기준 숫자 있으면 tlst추가 그리고 남은 자리 0
        if num > 0: # 마지막 숫자가 남은 경우
            tlst.append(num)

        arr[i] = tlst + [0] * (N - len(tlst)) # tlst 남은 길이를 0으로 채우기

def dfs(n, arr):
    global ans

    if n == 5:
        ans = max(ans, max(map(max, arr)))
        return

    # 좌측 이동(좌측으로 기울이기)
    narr = [lst[::] for lst in arr]
    move(narr)
    dfs(n + 1, narr)

    # 우측 이동(우측으로 기울이기)
    narr = [lst[::-1] for lst in arr]
    move(narr)
    dfs(n + 1, narr)

    # 위쪽 이동(위쪽으로 기울이기)
    arr_t = list(map(list, zip(*arr))) # 열을 행으로 처리 (열 => 행)
    narr = [lst[::] for lst in arr_t]
    move(narr)
    dfs(n + 1, narr)

    # 아래쪽 이동(아래쪽으로 기울이기)
    narr = [lst[::-1] for lst in arr_t]
    move(narr)
    dfs(n + 1, narr)

ans = 0
dfs(0, arr)
print(ans)
