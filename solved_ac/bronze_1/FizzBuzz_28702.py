# 백준 - 브론즈1 - FizzBuzz - 28702 - 단순 수학, 문자열 문제
'''
단순 수학, 문자열 문제

단순한 수학과 문자열을 이용해서 문제를 풀면 된다.

풀이 과정
    1. word_list를 입력받는다.
    2. word_list를 순회하며 Fizz, Buzz, FizzBuzz가 아닌 것을 찾는다.
    3. 찾은 것을 res에 저장하고 종료한다.
    4. res가 3과 5로 나누어 떨어지면 FizzBuzz를 출력한다.
    5. res가 3으로 나누어 떨어지면 Fizz를 출력한다.
    6. res가 5로 나누어 떨어지면 Buzz를 출력한다.
    7. 그 외의 경우 res를 출력한다.
'''

word_list = [input() for _ in range(3)]

# 테스트
# word_list = ['Fizz', 'Buzz', '11'] # Fizz
# word_list = ['980803', '980804', 'FizzBuzz'] # 980806

res = 0
for i in range(len(word_list)):
    if word_list[i] not in ['Fizz', 'Buzz', 'FizzBuzz']:
        word_idx = word_list.index(word_list[i])
        res = int(word_list[i]) + 3 - word_idx
        break

if res % 3 == 0 and res % 5 == 0:
    print('FizzBuzz')
elif res % 3 == 0:
    print('Fizz')
elif res % 5 == 0:
    print('Buzz')
else:
    print(res)
