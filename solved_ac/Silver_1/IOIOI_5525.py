'''
문자열, 구현 문제

while 반복 문으로 'IOI'가 n이랑 숫자가 맞는지 확인한다.
('IOI' -> 'IOIOI' -> 'IOIOIOI' -> 이런 식으로 'OI'가 2씩 늘어나니까 idx += 2를 했다.)
맞으면 res를 + 1 씩 하고 없으면 ck를 0으로 만들고 확인하기.
'''

n, m = int(input()), int(input())
s = input()

# 테스트
# n, m = 1, 13
# s = 'OOIOIOIOIIOII' # 4
# n, m = 2, 13
# s = 'OOIOIOIOIIOII' # 2

res, idx, ck = 0, 0, 0

while idx < m - 2:
    if s[idx] == 'I' and s[idx + 1] == 'O' and s[idx + 2] == 'I':
        ck += 1

        if ck == n:
            res += 1
            ck -= 1
        idx += 2
    else:
        ck = 0
        idx += 1

print(res)
