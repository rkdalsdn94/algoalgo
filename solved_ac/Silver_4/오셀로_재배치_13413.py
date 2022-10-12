# 백준 - 오셀로 재배치 - 13413 - 실버4 - 문자열, 그리디 문제
'''
문자열, 그리디 문제

초기 문자열과, 목표 문자열을 입력받은 후
두 문자열이 다를 때마다 temp에 append한다. 그리고, temp에서 W와 B의 개수를 센 다음
W가 크거나 같으면 W의 개수를 출력하고, B가 더 크면 B의 개수를 출력하면 된다.

in
    3
    5
    WBBWW
    WBWBW
    7
    BBBBBBB
    BWBWBWB
    4
    WWBB
    BBWB
out
    1
    3
    2
'''

t = int(input())

for _ in range(t):
    n = int(input())
    initial_status = input()
    goal_status = input()
    temp = []
    res = 0

    for i in range(n):
        if initial_status[i] != goal_status[i]:
            temp.append(initial_status[i])
    
    if temp.count('W') >= temp.count('B'):
        res = temp.count('W')
    else:
        res = temp.count('B')

    print(res)
