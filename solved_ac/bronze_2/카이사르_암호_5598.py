# 백준 - 브론즈2 - 카이사르 암호 - 5598 - 단순 구현, 문자열 문제
'''
단순 구현, 문자열 문제

입력으로 들어온 문자열을 아스키 코드로 3을 뺀 값을 res에 담고 res를 출력하면 된다.
단, 65보다 작아질 경우엔 26을 더하는 부분만 신경쓰면 된다.
'''

word = input()

# 테스트
# word = 'MRL' # 'JOI'
# word = 'FURDWLD' # 'CROATIA'
# word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # XYZABCDEFGHIJKLMNOPQRSTUVW

res = ''

for i in word:
    idx = ord(i)

    if idx - 3 < 65:
        idx += 26
    
    res += chr(idx - 3)

print(res)
