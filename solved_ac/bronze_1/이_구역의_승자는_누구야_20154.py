# 백준 - 브론즈1 - 이 구역의 승자는 누구야?! - 20154 - 구현, 문자열 문제
'''
구현, 문자열 문제

solved 분류 상 수학도 있지만 간단한 사칙연산이라 뺐다.

문자열로 들어온 값(word)을 각 횟수들의 리스트(res)로 만들어 준다.
res들의 합이 홀수인지 짝수인지 체크만 하면 된다.
'''

word = input()

# 테스트
# word = 'ABCDE' # I'm a winner!
# word = 'AECF' # You're the winner?

number_of_strokes = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

res = []
for i in range(len(word)):
    res.append(number_of_strokes[ord(word[i]) - 65])

if sum(res) % 2 != 0:
    print("I'm a winner!")
else:
    print("You're the winner?")
