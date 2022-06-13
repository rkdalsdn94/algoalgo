'''
구현 문제

학년이랑 성별을 넣을 변수(temp)를 설정한 후 (input값 그대로 사용하기 위해서 7을 곱했다.)
temp[성별][학년] --> [[0] * 7(학년) for _ in range(2: 성별)]
내장 함수 math.ceil을 이용해
현재 학년, 성별이 갖고 있는 인원수 나누기 방 최대 인원수로 올림 값으로 res에 더해줬다.

in
    16 2
    1 1
    0 1
    1 1
    0 2
    1 2
    0 2
    0 3
    1 3
    1 4
    1 3
    1 3
    0 6
    1 5
    0 5
    1 5
    1 6
out
    12

in
    3 3
    0 3
    1 5
    0 6
out
    3
'''

from math import ceil

n, k = map(int, input().split())
res = 0
temp = [ [0] * 7 for _ in range(2) ]

for _ in range(n):
    s, y = map(int, input().split())
    temp[s][y] += 1

for i in temp:
    for j in i:
        res += ceil(j / k)

print(res)
