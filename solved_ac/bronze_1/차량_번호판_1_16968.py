# 백준 - 브론즈1 - 차량 번호판 1 - 16968 - 수학, 조합론 문제
'''
수학, 조합론 문제

'c'는 문자(26개), 'd'는 숫자(10개)로 이루어진 차량 번호판이 있다.
차량 번호판의 길이가 n이라면 차량 번호판의 경우의 수를 구하는 문제이다.

풀이 과정
    1. 차량 번호판을 입력받는다.
    2. 차량 번호판의 첫 번째 값이 'c'라면 res를 26으로 초기화한다.
    3. 차량 번호판의 첫 번째 값이 'd'라면 res를 10으로 초기화한다.
    4. 차량 번호판을 돌면서 다음을 확인한다.
        4.1. 차량 번호판이 'c'라면
            4.1.1. 차량 번호판의 이전 값이 c라면 res에 25를 곱한다.
            4.1.2. 차량 번호판의 이전 값이 d라면 res에 26을 곱한다.
        4.2. 차량 번호판이 d라면
            4.2.1. 차량 번호판의 이전 값이 d라면 res에 9를 곱한다.
            4.2.2. 차량 번호판의 이전 값이 c라면 res에 10을 곱한다.
    5. res를 출력한다.
'''

car_number = input()

# 테스트
# car_number = 'dd' # 90
# car_number = 'cc' # 650
# car_number = 'dcdd' # 23400

if car_number[0] == 'c':
    res = 26
else:
    res = 10

for i in range(1, len(car_number)):
    if car_number[i] == 'c':
        if car_number[i - 1] == 'c':
            res *= 25
        else:
            res *= 26
    else:
        if car_number[i - 1] == 'd':
            res *= 9
        else:
            res *= 10

print(res)
