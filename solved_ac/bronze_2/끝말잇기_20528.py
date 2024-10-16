# 백준 - 브론즈2 - 끝말잇기 - 20528 - 문자열, 에드 훅 문제
'''
문자열, 에드 훅 문제

문자열을 입력받아, 모든 단어의 첫 글자가 같으면 1을 출력하고, 그렇지 않으면 0을 출력하는 문제이다.

풀이 과정
    1. n을 입력받는다.
    2. words를 입력받는다.
    3. words의 첫 글자를 저장한다.
    4. words의 첫 글자와 다른 첫 글자가 있으면 0을 출력하고 종료한다.
    5. 그렇지 않으면 1을 출력한다.
'''

n = int(input())
words = list(input().split())

# 테스트
# n = 3
# words = ['pqqp', 'pqpqp', 'pbbbp'] # 1
# n = 3
# words = ['aba', 'c', 'dd'] # 0

first = words[0][0]
for word in words:
    if word[0] != first:
        print(0)
        exit(0)

print(1)
