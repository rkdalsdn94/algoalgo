s = input()
# s = '()(((()())(())()))(())'   # 17
# s = '(((()(()()))(())()))(()())' # 24

res, temp = 0, 0

for i in range(len(s)):
    if s[i] == '(':
        temp += 1
    else:
        temp -= 1
        if s[i-1] == '(':
            res += temp
        else:
            res += 1
print(res)
