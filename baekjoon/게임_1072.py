'''
in
    10 8
    100 80
    47 47
    99000 0
    1000000000 470000000
out
    1
    6
    -1
    1000
    19230770
'''
import math
x, y = map(int, input().split())
z = math.floor((y * 100) / x)
start, end = 0, 1000000001
if z < 99:
    while start <= end:
        mid = (start + end) // 2
        nx, ny = x + mid, y + mid
        if math.floor( (ny * 100) / nx) > z:
            end = mid - 1
        else:
            start = mid + 1
print(-1) if z >= 99 else print(end+1)


# 처음에 이 밑에 처럼 했다가 틀림..
'''
import math
x, y = map(int, input().split())
z = math.trunc((y / x) * 100) # 여기서 trunc 함수 써서 그런거 같음 -> floor는 내림인데 trunc는 int(실수)라고 하는 느낌
start, end = 0, 1000000001    # 위에 좀 더 풀어서 얘기하면 trunc는 0으로 향해서 내림 -> math.trunc(-3.14) = -3 <-> floor(-3.14) = -4
if z < 99:
    while start <= end:
        mid = (start + end) // 2
        nx, ny = x + mid, y + mid
        if math.trunc( (ny / nx) * 100) > z:
            end = mid - 1
        else:
            start = mid + 1
print(-1) if z >= 99 else print(end+1)
'''