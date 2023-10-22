# 백준 - 브론즈1 - 이상한 암호코드 - 18129 - 구현, 문자열 문제
'''
구현, 문자열 문제

exist_word_check 함수를 통해 이미 검사했던 단어인지 확인한다. (이미 존재하면 False 반환, 없다면 True)
검사했던 단어가 아니고, 이전 글자와 다르다면
    temp의 값이 k 이상이면 '1' 아니면 '0'을 res에 추가한다.
검사했던 단어이거나, 이전 글자와 같다면
    temp를 1씩 증가 시킨다.
'''

s, k = input().split()
s, k = s.upper(), int(k)

# 테스트
# s, k = 'AAAABBBC'.upper(), 3 # 110
# s, k = 'aaabaaaaa'.upper(), 3 # 10
# s, k = 'QQqqqqwwwffFAACCvvVaaaAhhHMOSS'.upper(), 8 # 0000000000

res = ''
temp = 1
word_temp = set()

def exist_word_check(idx):
    return False if s[idx] in word_temp else True

for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        if exist_word_check(i - 1):
            if temp >= k:
                res += '1'
            else:
                res += '0'
            word_temp.add(s[i - 1])
        temp = 1
    else:
        temp += 1

if exist_word_check(len(s) - 1):
    if temp >= k:
        res += '1'
    else:
        res += '0'

print(res)
