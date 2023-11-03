# 백준 - 브론즈1 - 열 순서 - 16495 - 수학, 문자열, 사칙연산 문제
'''
수학, 문자열, 사칙연산 문제

단순하지만 구현이 바로 떠오르진 않았다.

풀이 과정
- 입력으로 들어오는 word의 글자 수만큼 반속한다.
- 반복문 내에서 해당하는 글자들을 ord 함수를 이용해 해당 유니코드의 숫자 값을 64로 뺀다. ('A'는 65부터 시작)
- 위에서 구한 값과 pow 함수를 사용해 총 글자인 26의 제곱수를 word의 글자 - i - 1 의 승수의 곱을 res에 더한다.
- res를 출력한다.

https://pythontutor.com/visualize.html#mode=edit 여기서 코드를 하나 씩 돌려보는게 훨씬 이해하기 쉽다.
'''

word = input()

# 테스트
# word = 'X' # 24
# word = 'AZ' # 52

res = 0

for i in range(len(word)):
    unicord = ord(word[i]) - 64
    multiplier = pow(26, len(word) - i - 1)
    res += unicord * multiplier

print(res)
