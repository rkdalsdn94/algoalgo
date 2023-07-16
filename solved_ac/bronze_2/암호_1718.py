# 백준 - 브론즈2 - 암호 - 1718 - 단순 구현, 문자열 문제
'''
단순 구현, 문자열 문제

문자열을 계산할 수 있으면 쉽게 풀 수 있는 문제이다.
word_conver_num 함수를 사용해서 문자들의 차를 구했고, 해당 값이 0보다 작아지면 26을 더하는 부분만 신경쓰면 된다.
'''

word = input()
key = input()

# 테스트
# word = 'nice day'
# key = 'love' # btgz oet

res = ''

def word_convert_num(n):
    return ord(n) - ord('a')

for i in range(len(word)):
    if word[i] == ' ':
        res += ' '
        continue

    temp = word_convert_num(word[i]) - word_convert_num(key[i % len(key)]) - 1
    if temp < 0:
        temp += 26
    res += chr(temp + 97)

print(res)
