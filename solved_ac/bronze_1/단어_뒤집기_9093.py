'''
단순 구현, 문자열 문제

문자를 입력받고 입력 받은 문자열을 ' '기준으로 split 한 후
각 단어를 돌면서 해당 단어를 뒤집은 채로 res에 append 하고,
res 출력

in
    2
    I am happy today
    We want to win the first prize
out
    I ma yppah yadot
    eW tnaw ot niw eht tsrif ezirp
'''

t = int(input())

for _ in range(t):
    a = input().split()
    res = []
    
    for i in a:
        res.append(i[::-1])
    
    print(*res)
