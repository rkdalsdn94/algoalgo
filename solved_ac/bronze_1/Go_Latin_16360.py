# 백준 - 브론즈1 - Go Latin - 16380 - 구현, 문자열, 많은 조건 분기 문제
'''
구현, 문자열, 많은 조건 분기 문제

단순하게 마지막 글자만 확인한 뒤 해당 글자의 대응하는 글자로 변경하면 된다.
단, 일치하는 마지막 글자가 없을 경우 'us'를 추가해야 된다.
'''

n = int(input())
n_list = [list(input()) for _ in range(n)]

# 테스트
# n = 2
# n_list = [list('toy'), list('engine')] # toios  \  engine
# n = 3
# n_list = [list('cup'), list('water'), list('cappuccino')] # capus  \  wateres  \  cappuccinos

for i in n_list:
    temp = ''.join(i)

    if temp[-1] == 'a':
        i[-1] = 'as'
    elif temp[-1] == 'i' or temp[-1] == 'y':
        i[-1] = 'ios'
    elif temp[-1] == 'l':
        i[-1] = 'les'
    elif temp[-2:] == 'ne':
        i[-2:] = 'anes'
    elif temp[-1] == 'n':
        i[-1] = 'anes'
    elif temp[-1] == 'o':
        i[-1] = 'os'
    elif temp[-1] == 'r':
        i[-1] = 'res'
    elif temp[-1] == 't':
        i[-1] = 'tas'
    elif temp[-1] == 'u':
        i[-1] = 'us'
    elif temp[-1] == 'v':
        i[-1] = 'ves'
    elif temp[-1] == 'w':
        i[-1] = 'was'
    else:
        i += 'us'

    print(''.join(i))
