# 프로그래머스 - Lv3 - 자물쇠와 열쇠 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

왜 입력 예제가 통과하는지도 모르겠어서 풀이 영상을 참고했다. 다음의 영상을 보고 이런 식으로 푸는구나 감을 잡으면 좋을 거 같다.
 - https://www.youtube.com/watch?v=RrWnBaflV2o

자세한 풀이 과정
 1. 자물쇠의 크기를 3배로 늘려준다.
 2. 자물쇠의 중앙에 열쇠를 놓을 수 있는 모든 경우의 수를 확인한다.
 3. 열쇠를 놓은 후 자물쇠와 열쇠가 맞물리는지 확인한다.
 4. 맞물리면 True, 아니면 False를 반환한다.

주의할 점
 1. 자물쇠의 크기를 3배로 늘려주는 이유는 열쇠를 놓을 수 있는 모든 경우의 수를 확인하기 위함이다.
 2. 열쇠를 놓은 후 자물쇠와 열쇠가 맞물리는지 확인할 때, 자물쇠의 중앙에 있는 부분만 확인하면 된다.
 3. 열쇠를 놓을 수 있는 모든 경우의 수를 확인할 때, 열쇠를 회전시키는 것을 고려해야 한다.
 4. 열쇠를 놓을 수 있는 모든 경우의 수를 확인할 때, 열쇠를 이동시키는 것을 고려해야 한다.
 5. 열쇠를 놓을 수 있는 모든 경우의 수를 확인할 때, 열쇠를 놓을 수 있는 위치를 고려해야 한다.
 6. 열쇠를 놓을 수 있는 모든 경우의 수를 확인할 때, 열쇠를 놓을 수 있는 위치를 고려할 때, 열쇠가 자물쇠를 벗어나는 경우를 고려해야 한다.
 7. 열쇠를 놓을 수 있는 모든 경우의 수를 확인할 때, 열쇠를 놓을 수 있는 위치를 고려할 때, 열쇠가 자물쇠를 벗어나는 경우를 고려할 때,
    자물쇠의 크기를 3배로 늘려주는 이유는 열쇠가 자물쇠를 벗어나는 경우를 고려하기 위함이다.
'''

def match(arr, key, rot, r, c):
    n = len(key)

    for i in range(n):
        for j in range(n):
            if rot == 0:
                arr[r + i][c + j] += key[i][j]
            elif rot == 1:
                arr[r + i][c + j] += key[n - 1 - j][i]
            elif rot == 2:
                arr[r + i][c + j] += key[n - 1 - i][n - 1 - j]
            else:
                arr[r + i][c + j] += key[j][n - 1 - i]

def check(arr, offset, n):
    for i in range(n):
        for j in range(n):
            if arr[offset + i][offset + j] != 1:
                return False
    return True

def solution(key, lock):
    offset = len(key) - 1

    for r in range(offset + len(lock)):
        for c in range(offset + len(lock)):
            for rot in range(4):
                arr = [[0] * 58 for _ in range(58)]

                for i in range(len(lock)):
                    for j in range(len(lock)):
                        arr[offset + i][offset + j] = lock[i][j]

                match(arr, key, rot, r, c)
                if check(arr, offset, len(lock)):
                    return True
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])) # true
