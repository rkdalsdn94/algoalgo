# 백준 - 브론즈1 - 핸드폰 번호 궁합 - 17202 - 구현, 문자열, 시뮬레이션, dp(?) 문제
'''
구현, 문자열, 시뮬레이션, dp(?) 문제

문제 분류에 dp가 들어가는데 dp는 왜 있는지 잘 모르겠다.

zip 함수를 이용해 입력받은 두 문자열을 한 글자씩 number_list에 담은 후,
while 문으로 number_list의 len이 2글자 이하가 될 때까지 반복하면서 (while문 조건)
    1부터 number_list의 길이까지 for 문을 시작하고 해당 for 문 안에서 두 수의 합의 % 10한 값을 temp에 append 한다.

number_list의 길이가 2 글자가 됐을 경우 while문을 멈추고 해당 리스트를 join을 이용해 출력하면 된다.
'''

a, b = input(), input()

# 테스트
# a, b = '74759336', '36195974' # 26
# a, b = '01234567', '12345678' # 02

number_list = []
for i, j in zip(a, b):
    number_list.append(i)
    number_list.append(j)
number_list = list(map(int, number_list))

while len(number_list) > 2:
    temp = []

    for i in range(1, len(number_list)):
        num = (number_list[i - 1] + number_list[i]) % 10
        temp.append(num)

    number_list = temp

print(*number_list, sep='')
