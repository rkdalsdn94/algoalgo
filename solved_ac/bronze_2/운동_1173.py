'''
구현, 시뮬레이션 문제

단순한 구현 문제이다. 아래의 조건만 잘 신경쓰면 금방 구현할 수 있다.

- 운동을 선택한 경우, 영식이의 맥박이 T만큼 증가한다.
  ( 영식이의 맥박이 X였다면, 1분 동안 운동을 한 후 맥박이 X+T가 되는 것이다. )

- X+T가 M보다 작거나 같을 때만 운동을 할 수 있다. 
  ( 영식이의 맥박이 X였다면, 1분 동안 휴식을 한 후 맥박은 X-R이 된다. )

- 맥박은 절대로 m보다 낮아지면 안된다.
  ( X-R이 m보다 작으면 맥박은 m이 된다. )

영식이의 초기 맥박은 m이다. 운동을 N분 하려고 한다.
이때 운동을 N분하는데 필요한 시간의 최솟값을 구해보자.
운동하는 시간은 연속되지 않아도 된다.

- 한 부분들만 신경 쓰면 된다.
'''

# N, m, M, T, R = map(int, input().split())

# 테스트
N, m, M, T, R = 5, 70, 120, 25, 15 # 10
# N, m, M, T, R = 100, 50, 100, 5, 200 # 109
# N, m, M, T, R = 1, 60, 70, 11, 11 # -1
# N, m, M, T, R = 200, 50, 200, 150, 1 # 30050
# N, m, M, T, R = 19, 89, 143, 17, 13 # 40

res = 0
temp = m
flag = True

while N != 0:
    if m + T > M:
        flag = False
        break
    if temp + T <= M:
        temp += T
        N -= 1
    else:
        temp = max(temp - R, m)
    res += 1

print(res if flag else -1 )
