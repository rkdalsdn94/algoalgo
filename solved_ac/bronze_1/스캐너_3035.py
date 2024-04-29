# 백준 - 브론즈1 - 스캐너 - 3035 - 구현, 문자열 문제
'''
구현, 문자열 문제

단순 구현 문제이다.

풀이 과정
1. r, c, zr, zc를 입력받고, word를 입력받는다.
2. word를 zr, zc만큼 늘려서 출력한다.
'''

r, c, zr, zc = map(int, input().split())
word = [list(input()) for _ in range(r)]

# 테스트
# r, c, zr, zc = 3, 3, 1, 2
# word = [
#     ['.', 'x', '.'],
#     ['x', '.', 'x'],
#     ['.', 'x', '.']
# ]
# '''
# out
#     ..xx..
#     xx..xx
#     ..xx..
# '''
# r, c, zr, zc = 3, 3, 2, 1
# word = [
#     ['.', 'x', '.'],
#     ['x', '.', 'x'],
#     ['.', 'x', '.']
# ]
# '''
# out
#     .x.
#     .x.
#     x.x
#     x.x
#     .x.
#     .x.
# '''

res = []
for i in range(r):
    temp = ''

    for j in word[i]:
        temp += j * zc
    for j in range(zr):
        res.append(temp)

for i in res:
    print(i)
