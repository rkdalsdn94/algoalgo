# 백준 - 브론즈1 - Text Roll - 9494 - 구현, 문자열 문제
'''
구현, 문자열 문제

풀이 과정
    1. n을 입력받는다.
    2. n이 0이면 종료한다.
    3. n만큼 문자열을 입력받는다.
    4. 문자열의 공백을 찾아서 temp에 넣는다.
    5. i가 0일 때 res를 temp[0]으로 초기화한다.
    6. temp를 순회하면서 temp[j]가 res보다 크거나 같으면 res에 temp[j]를 넣고 break한다.
    7. res + 1을 출력한다.
'''

while 1:
    n = int(input())

    if n == 0:
        break

    res = 0
    for i in range(n):
        s = input()
        s += ' '

        temp = []
        for j in range(len(s)):
            if s[j] == ' ':
                temp.append(j)

        if i == 0:
            res = temp[0]

        for j in range(len(temp)):
            if temp[j] >= res:
                res = temp[j]
                break

    print(res + 1)
