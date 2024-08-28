# 백준 - 실버2 - 다음 다양한 단어 - 16923 - 구현, 문자열 문제
'''
구현, 문자열 문제

풀이 과정
    1. 입력을 받는다.
    2. alphabet을 만들어 각 알파벳의 개수를 센다.
    3. alphabet에 1이 있는지 확인한다.
        3.1. 1이 있다면 해당 알파벳을 추가해준다.
    4. alphabet을 뒤에서부터 돌면서 s[i] > s[i - 1]인 경우를 찾는다.
        4.1. temp에 s[i - 1:]을 정렬해준다.
        4.2. temp에서 s[i - 1]의 index를 찾아서 그 다음 값을 res에 넣어준다.
    5. res를 출력한다.
'''

s = input()

# 테스트
# s = 'codeplus' # codeplusa
# s = 'abc' # abcd
# s = 'zyxwvutsrqponmlkjihgfedcba' # -1
# s = 'abcdefghijklmnopqrstuvwzyx' # abcdefghijklmnopqrstuvx

res = -1
alphabet = [1] * 26

for i in range(len(s)):
    alphabet[ord(s[i]) - ord('a')] -= 1

if 1 in alphabet:
    res = s + chr(alphabet.index(1) + ord('a'))
else:
    for i in range(25, 0, -1):
        if s[i] > s[i - 1]:
            temp = sorted(s[i - 1:])
            idx = temp.index(s[i - 1]) + 1
            res = s[:i - 1] + temp[idx]
            break
print(res)
