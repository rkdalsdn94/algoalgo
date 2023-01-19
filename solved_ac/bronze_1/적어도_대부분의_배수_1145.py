# 백준 - 브론즈1 - 적어도 대부분의 배수 - 1145 - 단순 구현, 완전 탐색 문제
'''
단순 구현, 완전 탐색 문제

1부터 시작해서 number_list 의 값들 중 나머지가 0이 되는 수가 3개일 때 반복문을 종료하면 된다.
'''

number_list = list(map(int, input().split()))

# 테스트
# number_list = [30, 42, 70, 35, 90] # 210
# number_list = [1, 2, 3, 4, 5] # 4
# number_list = [30, 45, 23, 26, 56] # 1170
# number_list = [3, 14, 15, 92, 65] # 195

res = 1
flag = True

while flag:
    temp = 0

    for i in number_list:
        if res % i == 0:
            temp += 1

        if temp == 3:
            flag = False
            break
    res += 1

print(res - 1)
