# 백준 - 브론즈1 - 크로스워드 만들기 - 2804 - 구현, 문자열 문제
'''
구현, 문자열 문제

행(x)과 열(y)만 구할 수 있으면 되는 문제이다.
주의할 점으로 행과 열을 구할 때 a글자 부터 구해야 된다.
즉, 첫 번째 for 문의 range 를 a 길자의 길이부터 해야 된다. (b 글자의 len 부터 했다가 틀렸다...)

행과 열을 구하는 방법은
a 글자의 길이부터 시작해 b 글자들을 반복하면서 둘이 같은 글자가 만났을 때, i는 행, y는 열로 구하면 된다.
그 후 res 배열을 a와 b 글자의 길이로 ['.']으로 초기화 한 변수에
행 열에 맞춰 각각 글자를 넣어준 뒤, res 배열을 문자열로 출력하면 된다.
'''

a, b = input().split()

# 테스트
# a, b = 'BANANA', 'PIDZAMA'
# '''
# out
#     .P....
#     .I....
#     .D....
#     .Z....
#     BANANA
#     .M....
#     .A....
# '''
# a, b = 'MAMA', 'TATA'
# '''
# out
#     .T..
#     MAMA
#     .T..
#     .A..
# '''
# a, b = 'REPUBLIKA', 'HRVATSKA'
# '''
# out
#     H........
#     REPUBLIKA
#     V........
#     A........
#     T........
#     S........
#     K........
#     A........
# '''
# a, b = 'AB', 'BA'
# '''
# out
#     B.
#     AB
# '''
# a, b = 'ABCD', 'DCBA'
# '''
# out
#     D...
#     C...
#     B...
#     ABCD
# '''

res = [['.'] * len(a) for _ in range(len(b))]
x, y = 0, 0
flag = False

for i in range(len(a)): # 여기서 a 글자의 길이를 먼저 해야 된다.
    for j in range(len(b)):
        if a[i] == b[j]:
            x, y = i, j
            flag = True
            break
    if flag: break

for i in range(len(b)):
    res[i][x] = b[i]

for i in range(len(a)):
    res[y][i] = a[i]

for i in res:
    print(''.join(i))
