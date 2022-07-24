'''
단순 구현, 문자열 문제

주어진 문자열을 한글자씩 돌면서 해당 문자의 범위가
A ~ Z 사이 또는 a ~ z 사이 일때 ord를 통해 13을 더한 후(temp)
temp의 범위가 글자의 범위를 넘어가면 26을 빼서 문자로 만들고, res에 더한 후 출력하면 된다.
'''

s = input()

# 테스트
# s = 'Baekjoon Online Judge' # Onrxwbba Bayvar Whqtr
# s = 'One is 1' # Bar vf 1

res = ''

for i in s:
    if 'a' <= i <= 'z':
        temp = ord(i) + 13
        
        if temp > 122:
            temp -= 26        
        res += chr(temp)
    elif 'A' <= i <= 'Z':
        temp = ord(i) + 13
        
        if temp > 90:
            temp -= 26
        res += chr(temp)
    else:
        res += i
print(res)