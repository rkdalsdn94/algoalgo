'''
in
    100
out
    0 1 4
in
    189
out
    -1
'''

t = int(input())
temp = [300, 60, 10]
res = [0,0,0]

while t > 0:
    if t % temp[2] != 0:
        del res[0:3]
        res.append(-1)
        break
    if t >= temp[0]:
        res[0] = (t//temp[0])
        t %= temp[0]
    elif t >= temp[1]:
        res[1] = (t//temp[1])
        t %= temp[1]
    elif t >= temp[2]:
        res[2] = (t//temp[2])
        t %= temp[2]
print(*res)

