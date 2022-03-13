'''
문자열을 입력받고, 다른 문자면 무시하고 p랑 y의 수만 구하는 문제이다.
근데 문자가 대문자일지 소문자일지는 몰라서 소문자로 바꾸고 count했다.
p랑 y의 수가 같으면 True 다르면 False를 구하는 문제이다.
'''
def solution(s):
    answer = True
    p_num = 0
    y_num = 0

    for i in s:
        i = i.lower()
        if i == 'p':
            p_num += 1
        elif i == 'y':
            y_num += 1

    if p_num == y_num:
        return True
    else:
        return False
