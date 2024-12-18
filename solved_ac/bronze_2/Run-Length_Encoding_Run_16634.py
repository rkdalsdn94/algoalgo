# 백준 - 브론즈2 - Run-Lenght Encoding, Run! - 16634 - 구현, 문자열 문제
'''
구현, 문자열 문제

단순한 문자열 구현 문제이다.

풀이 과정
    1. 입력값을 받는다.
    2. 입력값이 E인 경우 압축을 수행한다.
        2.1. cnt, temp, res를 초기화한다.
        2.2. word의 길이만큼 반복한다.
        2.3. word[i]가 temp와 같은 경우 cnt를 증가시킨다.
        2.4. word[i]가 temp와 다른 경우 res에 temp와 cnt를 추가하고 temp와 cnt를 초기화한다.
    3. 입력값이 D인 경우 압축을 해제한다.
        3.1. res를 초기화한다.
        3.2. word의 길이만큼 반복한다.
        3.3. word[i]가 숫자인 경우 word[i-1]을 int(word[i])만큼 res에 추가한다.
    4. res를 출력한다.
'''

operation, word = input().split()

# 테스트
# operation, word = 'E HHHeellloWooorrrrlld!!'.split() # H3e2l3o1W1o3r4l2d1!2
# operation, word = 'D H3e2l3o1W1o3r4l2d1!2'.split() # HHHeellloWooorrrrlld!!

word = word + ' '
res = ''

if operation == 'E':
    cnt = 1
    temp = word[0]

    for i in range(1, len(word)):
        if word[i] == temp:
            cnt += 1
        else:
            res += temp + str(cnt)
            temp = word[i]
            cnt = 1
else:
    for i in range(len(word)):
        if word[i].isdigit():
            res += word[i - 1] * int(word[i])

print(res)
