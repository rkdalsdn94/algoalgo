n = list(input())
# 테스트
# n = list('1236') # YES
# n = list('1') # NO
# n = list('1221') # YES
# n = list('4729382') # NO
# n = list('42393338') # YES
res = 'NO'

for i in range(1, len(n)):
    front_digit = back_digit = 1

    for j in n[:i]:
        front_digit *= int(j)

    for z in n[i:]:
        back_digit *= int(z)

    if front_digit == back_digit:
        res = 'YES'
        break

print(res)