# 백준 - 브론즈1 - Historical TV Remote Control - 25871 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

완전 탐색 방식으로 res를 0부터 시작해 1 더하고 1 빼고 값으로 답을 구해가면 된다.
아래 코드를 https://pythontutor.com/visualize.html#mode=edit 에서 실행하면서 보면 이해하기 쉽다.

풀이 과정
    1. n, *n_list를 입력받는다.
    2. target_num을 입력받는다.
    3. res를 0으로 초기화한다.
    4. minus_num, plus_num를 만들어 target_num - res, target_num + res를 넣는다.
    5. minus_num이 0보다 크거나 같다면
        5.1. flag를 True로 초기화한다.
        5.2. minus_num을 돌면서 n_list에 있는지 확인한다.
        5.3. n_list에 없다면 flag를 False로 바꾸고 break한다.
        5.4. flag가 True라면 res를 출력하고 break한다.
    6. plus_num이 999보다 작거나 같다면
        6.1. flag를 True로 초기화한다.
        6.2. plus_num을 돌면서 n_list에 있는지 확인한다.
        6.3. n_list에 없다면 flag를 False로 바꾸고 break한다.
        6.4. flag가 True라면 res를 출력하고 break한다.
    7. res에 1을 더하고 4번으로 돌아간다.
'''

n, *n_list = list(input().split())
target_num = int(input())

# 테스트
# n, n_list = '3', ['0', '8', '9']
# target_num = 35 # 0
# n, n_list = '4', ['1', '2', '5', '9']
# target_num = 250 # 50

res = 0
while 1:
    minus_num, plus_num = target_num - res, target_num +  res

    if minus_num >= 0:
        flag = True

        for i in str(minus_num):
            if i in n_list:
                flag = False
                break
        if flag:
            print(res)
            break

    if plus_num <= 999:
        flag = True

        for i in str(plus_num):
            if i in n_list:
                flag = False
                break
        if flag:
            print(res)
            break
    res += 1
