books = [input() for _ in range(int(input()))]
# books = ['top', 'top', 'top', 'top', 'kimtop']
# books = ['a', 'a', 'top', 'top', 'kimtop']
temp = {}
res = []
for i in books:
    if i not in temp:
        temp[i] = 1
    else:
        temp[i] += 1

for i, j in temp.items():
    if j == max(temp.values()):
        res.append(i)


print(sorted(res)[0])
