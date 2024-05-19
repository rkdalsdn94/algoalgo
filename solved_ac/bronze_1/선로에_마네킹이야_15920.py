# 백준 - 브론즈1 - 선로에 마네킹이야 - 15920 - 구현 문제
'''
구현 문제

풀이 과정
 1. 입력을 받고, train을 0으로 초기화한다.
 2. 반복문을 돌면서 train이 2가 되면 res를 출력하고, 반복문을 종료한다.
 3. train이 1이면 res를 6으로 변경하고, W가 나오면 train을 1 증가시키고, P가 나오면 res를 변경한다.
 4. train이 1이면 res를 6으로 변경하고, P가 나오면 res를 1로 변경한다.
 5. train이 0이면 res를 5로 변경한다.
 6. 위 반복문 중의 종료되지 않으면 0을 출력한다.
'''

n = int(input())
s = input()

# 테스트
# n = 8
# s = 'PPPWWWPP' # 1
# n = 7
# s = 'PPPWPPP' # 0
# n = 4
# s = 'WPPW' # 6

res = 5
train = 0

for char in s:
    if char == "W":
        train += 1

        if train == 2:
            print(res)
            break
    else:
        if train == 1:
            res = 6
        elif res == 5:
            res = 1
        elif res == 1:
            res = 5
else:
    print(0)
