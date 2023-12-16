# 백준 - 브론즈1 - Pen Pineapple Apple Pen - 15881 - 단순 구현, 그리디 문제
'''
단순 구현, 그리디 문제

단순히 입력으로 들어오는 단어에서 count 함수를 사용하면 된다.
count 함수의 인자로는 'pPAp' 를 사용하고, count 함수의 결과를 출력하면 되는 단순한 문제이다.
'''

n = int(input())
word = input()

# 테스트
# n = 15
# word = 'ApPApPpAPpApPAp' # 2
# n = 7
# word = 'pPApPAp' # 1

res = word.count('pPAp')
print(res)
