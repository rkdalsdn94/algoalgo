'''
단순 구현, 완전 탐색 문제

n의 범위가 4부터 100만 이라서
n부터 4까지 반복문을 설정한 후에

해당 숫자를 문자로 변환 후 해당 문자를 반복하면서
문자가 4, 7로 만들수 있으면 flag가 True가 되고, i를 출력하면 된다.
'''

n = int(input())

# n = 100 # 77
# n = 75 # 74
# n = 5 # 4
# n = 474747 # 474747

for i in range(n, 3, -1):
    flag = True

    for j in str(i):
        if j != '4' and j != '7':
            flag = False
    if flag:
        print(i)
        break
