# 뒤집기 - 1439

s = '0001100'
s = '01010'
# s = input()

temp = [s[0]]
for i in range(len(s)):
    if s[i] != temp[-1]:
        temp.append(s[i])
print(min(temp.count('0'), temp.count('1')))
