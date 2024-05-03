# 백준 - 실버2 - 연산자 끼워넣기 2 - 15658 - 완전 탐색, 백 트래킹
'''
완전 탐색, 백 트래킹

연산자 끼워넣기(14888번, 실버1) 문제와 똑같이 풀면 된다.
아래 설명이 부족하면 14888번 풀이를 참고하자.
https://pythontutor.com/visualize.html#mode=edit 여기서 실행해보는 것이 이해가 빠르다.

풀이 과정
1. 입력을 받는다.
2. 백트래킹을 사용해 모든 경우의 수를 구한다.
3. 연산자의 개수만큼 백트래킹을 하고, 연산자를 사용하면 1씩 빼고, 연산자를 사용하지 않으면 1씩 더한다.
4. 연산자를 사용할 때마다 연산을 하고, 최대값과 최소값을 갱신한다.
5. 최대값과 최소값을 출력한다.
'''

import sys; sys.setrecursionlimit(10 ** 6)

n = int(input())
nums = list(map(int, input().split()))
operation_list = list(map(int, input().split())) # 더하기 빼기 곱하기 나누기 순으로 되어 있음

# 테스트
# n = 2
# nums = [5, 6]
# operation_list = [1, 1, 1, 1] # 30  \  -1
# n = 3
# nums = [3, 4, 5]
# operation_list = [2, 1, 2, 1] # 60  \  -5
# n = 6
# nums = [1, 2, 3, 4, 5, 6]
# operation_list = [3, 2, 1, 1] # 72  \  -48

max_res = -1e9
min_res = 1e9

def back_tracking(depth, num):
    global max_res, min_res

    if depth == n - 1:
        max_res = max(max_res, num)
        min_res = min(min_res, num)
        return

    for i in range(4):
        if operation_list[i]:
            operation_list[i] -= 1

            if i == 0:
                back_tracking(depth + 1, num + nums[depth + 1])
            elif i == 1:
                back_tracking(depth + 1, num - nums[depth + 1])
            elif i == 2:
                back_tracking(depth + 1, num * nums[depth + 1])
            else:
                back_tracking(depth + 1, int(num / nums[depth + 1]))

            operation_list[i] += 1

back_tracking(0, nums[0])

print(int(max_res))
print(int(min_res))
