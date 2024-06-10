# 백준 - 브론즈2 - Aromatic Numbers - 6769 - 구현, 문자열, 사칙연산 문제
'''
구현, 문자열, 사칙연산 문제

영어를 해석하는게 어려웠다..
음수가 되는 조건을 잘못 해석해서 한 번 틀렸다.
    음수가 되는 조건 : 현재 로만의 값이 다음 로만보다 작을 경우

예제로 확인해 보면 다음 처럼 계산하면 된다.
roman_list = ['I',  'I',   'X',    'V',    'X']
               1  <  1  <   10   >  5   <  10
               +     -      +       -       +
               2    -3     20     -45      10
               2    -1     19     -26     -16    => -16

처음부터 보면 현재 로만인 'I'는 다음 로만인 'I'보다 작지 않으므로 (+)
    그 다음 'I'는 'X'보다 작으므로 (-)
    그 다음 'X'는 'V'보다 크므로 (+)
    그 다음 'V'는 'X'보다 작으므로 (-)
                .
                .
        이런 식으로 구하면 된다.

풀이 과정
    1. 입력을 받고, 로만의 값과 로마 숫자를 딕셔너리로 만든다.
    2. res, temp, num_cnt, pre_roman, num_len을 초기화한다.
    3. 로마 숫자를 돌면서 조건에 맞게 계산한다.
    4. 결과를 출력한다.
'''

number = input()

# 테스트
# number = '3M1D2C' # 3700
# number = '3X2I4X' # 68
# number = '2I3I2X9V1X' # -16

roman_number = {
    'I': 1, 'V': 5,'X': 10,
    'L': 50, 'C': 100,'D': 500,
    'M': 1000
}

res = 0
temp = 0
num_len = len(number)

for i in range(0, len(number), 2):
    temp = int(number[i]) * roman_number[number[i + 1]]

    if i < num_len - 3 and roman_number[number[i + 1]] < roman_number[number[i + 3]]:
        temp *= -1

    res += temp

print(res)
