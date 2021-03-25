n = input()
# n = '26' # 4
# n = '0' # 1
# n = '1' # 60
# n = '55' # 3
temp = n
res = 0    

while 1:
    if n == '0':
        res += 1
        break
    if len(temp) == 1:
        temp = '0' + temp
    add_temp = str(int(temp[0]) + int(temp[1]))
    temp = temp[-1] + add_temp[-1]
    res += 1
    if int(temp) == int(n):
        break

print(res)


