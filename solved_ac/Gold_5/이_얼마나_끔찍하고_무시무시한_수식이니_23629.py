# 백준 - 골드5 - 이 얼마나 끔찍하고 무시무시한 수식이니 - 23629 - 구현, 문자열 문제
'''
구현, 문자열 문제

문자열을 입력받아서 숫자로 변환한 후 연산자를 찾아서 연산을 수행하고, 출력 형시에 맞춰 출력하면 된다.
https://pythontutor.com/render.html#mode=display 해당 사이트에서 코드를 돌려보면 이해가 잘 된다.

풀이 과정
    1. 문자열을 입력받는다.
    2. num_list를 만든다.
    3. word에서 num_list의 값을 찾아서 숫자로 바꾼다.
    4. 연산자를 찾아서 stack에 넣는다.
    5. stack에서 연산을 수행한다.
        5.1. 이때 나눗셈 처리 방식을 예제에 나와 있듯이 신경 써야 한다.
            ```
                정수 나눗셈의 처리 방식은 C의 방식을 따른다.
                즉, '0'에 가까운 정수를 취한다. 이는 Python의 정수 나눗셈 처리 방식(floordiv)과 다르다.
            ```
    6. 결과를 출력한다.
'''

from math import ceil, floor

word = input()

# 테스트
# word = 'ONETWOTHREEFOUR+FIVESIXSEVEN=' # 1234+567=  \  ONEEIGHTZEROONE
# word = 'FIVEZEROxTWOTWO-ONEONEONEONE=' # 50x22-1111=  \  -ONEONE
# word = 'ONE-SIX/THREE=' # 1-6/3=  \  -ONE
# word = 'ONE+-THREE=' # Madness!
# word = 'ONETWOFIVENINEEIGHTSEVEN=' # 125987=  \  ONETWOFIVENINEEIGHTSEVEN

num_list = [
    'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE'
]
operation_stack = []

for i in range(len(num_list)):
    word = word.replace(num_list[i], str(i))

temp = word
for i in '+-x/':
    temp = temp.replace(i, ' ')

for i in word:
    if i in '+-x/':
        operation_stack.append(i)

try:
    temp_list = temp[:-1].split()
    res_total = int(temp_list[0])

    for i in range(len(operation_stack)):
        if operation_stack[i] == '+':
            res_total += int(temp_list[i + 1])
        elif operation_stack[i] == '-':
            res_total -= int(temp_list[i + 1])
        elif operation_stack[i] == 'x':
            res_total *= int(temp_list[i + 1])
        elif operation_stack[i] == '/':
            res_total /= int(temp_list[i + 1])

            if res_total < 0:
                res_total = ceil(res_total)
            else:
                res_total = floor(res_total)

    res_total = str(res_total)
    for i in res_total:
        if i in '+-x/':
            continue
        res_total = res_total.replace(i, num_list[int(i)])

    print(word)
    print(res_total)
except:
    print('Madness!')
