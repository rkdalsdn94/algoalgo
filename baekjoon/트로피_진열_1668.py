
t = [int(input()) for _ in range(int(input()))]
# t = [1, 2, 3, 4, 5]
# t = [3, 5, 4, 5, 7, 2, 5]

l, r = 1, 1
temp = t[0]
for i in range(1, len(t)):
    if temp < t[i]:
        l += 1
        temp = t[i]

t.reverse()
temp = t[0]
for i in range(1, len(t)):
    if temp < t[i]:
        r += 1
        temp = t[i]

print(l, r, sep='\n')
