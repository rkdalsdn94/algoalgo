num = '55-50+40'.split('-') # -35
# num = input().split('-')
res = 0
for i in num[0].split('+'):
    res += int(i)

for i in num[1:]:
    for j in i.split('+'):
        res -= int(j)
print(res)
