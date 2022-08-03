'''
단순 구현 문제

입력이 안들어오는 순간을 try catch 잡고 풀면 된다. -> 파이썬은 try except 이다.
'''

while 1:
    try:
        print(input())
    except:
        break