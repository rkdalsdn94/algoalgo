# 백준 - 브론즈2 - 좋은놈 나쁜놈 - 4447 - 단순 구현, 문자열 문제
'''
구현, 문자열 문제

단순 구현과 문자열 문제이다. (count만 하면 됨)

입력으로 들어온 값 중 다음을 계산한다.
    'g'의 개수 + 'G'의 개수(g_cnt)
    'b'의 개수 + 'B'의 개수(b_cnt)
g_cnt, b_cnt 두 값 중 g_cnt 값이 더 크면 '원래 문자열' + 'is GOOD'
g_cnt, b_cnt 두 값 중 b_cnt 값이 더 크면 '원래 문자열' + 'is A BADDY'
g_cnt, b_cnt 두 값이 값이 같다면 '원래 문자열' + 'is NEUTRAL' 을 출력하면 된다.
'''
n = int(input())
word_list = [input() for _ in range(n)]

# 테스트
# n = 8
# word_list = [
#     'Algorithm Crunching Man',
#     'Green Lantern',
#     'Boba Fett',
#     'Superman',
#     'Batman',
#     'Green Goblin',
#     'Barney',
#     'Spider Pig'
# ]
# '''
# out
#     Algorithm Crunching Man is GOOD
#     Green Lantern is GOOD
#     Boba Fett is A BADDY
#     Superman is NEUTRAL
#     Batman is A BADDY
#     Green Goblin is GOOD
#     Barney is A BADDY
#     Spider Pig is GOOD
# '''

for i in word_list:
    g_cnt = i.count('g')
    g_cnt += i.count('G')
    b_cnt = i.count('b')
    b_cnt += i.count('B')

    if g_cnt > b_cnt:
        print(f'{i} is GOOD')
    elif b_cnt > g_cnt:
        print(f'{i} is A BADDY')
    else:
        print(f'{i} is NEUTRAL')

