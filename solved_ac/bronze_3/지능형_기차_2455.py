'''
단순 구현, 수학 문제
'''

train = [ list(map(int, input().split())) for _ in range(4) ]
res = 0
temp = 0

for a, b in train:
    if temp > a:
        temp -= a
    else:
        temp = 0
    temp += b

    res = max(res, temp)

print(res)
