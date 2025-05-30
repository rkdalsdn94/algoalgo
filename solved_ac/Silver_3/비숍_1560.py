# 백준 - 실버3 - 비숍 - 1560 - 에드 훅, 임의 정밀도 / 큰 수 연산 문제
'''
에드 훅, 임의 정밀도 / 큰 수 연산 문제

n * n 체스 판에서 비숍을 놓을 수 있는 경우의 수를 구하는 문제이다.
에드 훅 문제이다. n * n의 board를 그려보면서 풀 수 있다.

n = 4 라고 가정했을 때 다음과 같다.
    . B . B
    B . B .
    . B . B
    B . B .
n = 3 이라면
    B . B
    . . .
    B . B

풀이 과정
 1. 입력을 받는다.
 2. 비숍을 놓을 수 있는 위치를 구한다.
 3. 비숍을 놓을 수 있는 위치를 출력한다.
'''

n = int(input())

# 테스트
# n = 3 # 4
# n = 2 # 2

if n == 1:
    print(1)
else:
    print(2 * n - 2)
