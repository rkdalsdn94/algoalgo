# 백준 - 실버3 - 과제는 끝나지 않아! - 17952 - 구현, 시뮬레이션, 자료 구조(스택) 문제
'''
구현, 시뮬레이션, 자료 구조(스택) 문제

문제에서 나온 다음의 규칙을 풀면 된다.
    1. 과제는 가장 최근에 나온 순서대로 한다. 또한 과제를 받으면 바로 시작한다.
    2. 과제를 하던 도중 새로운 과제가 나온다면, 하던 과제를 중단하고 새로운 과제를 진행한다.
    3. 새로운 과제가 끝났다면, 이전에 하던 과제를 이전에 하던 부분부터 이어서 한다. (성애는 기억력이 좋기 때문에 아무리 긴 시간이 지나도 본인이 하던 부분을 기억할 수 있다.)
위 규칙 중 2번을 만족하기 위해 stack을 사용하면 된다.

풀이 과정
 - 미리 과제의 정보를 n_list 라는 이름으로 받은 뒤 계산했다.
 - n_list의 값을 반복하면서 과제의 정보가 정보가 나오는 순간(i의 [0] 번째 인덱스가 1일 때) stack에 append 한다.
    - 주의할 점으론 time을 1 뺀 상태로 stack의 append 해야 된다.
 - 위 반복문 내에서 stack 의 값이 있다면 담긴 두 번째 값(걸리는 시간, time)을 1씩 빼주면서 이 값(time)이 0이되면 첫 번째 값(score)을 res에 더해준다.
 - 이러한 과정을 반복한 뒤 최종 res를 출력하면 된다.
'''

import sys; input=sys.stdin.readline

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 3
# n_list = [[1, 100, 3], [0], [0]] # 100
# n = 5
# n_list = [[1, 10, 3], [0], [1, 100, 2], [1, 20, 1], [0]] # 120

stack = []
res = 0

for i in n_list:
    if i[0] == 1:
        stack.append([i[1], i[2] - 1])

    if stack:
        score, time = stack.pop()

        if time == 0:
            res += score
        else:
            stack.append([score, time - 1])

print(res)
