'''
단순 구현, 문자열 문제

입력값의 형식을 보면 '-' 을 기준으로 입력값이 들어온다.
'-'을 기준으로 split 한 후 해당 글자의 앞글자를 res에 담고 출력 하면 된다.
'''

name_list = input().split('-')

# 테스트
# name_list = 'Knuth-Morris-Pratt'.split('-') # KMP
# name_list = 'Mirko-Slavko'.split('-') # MS
# name_list = 'Pasko-Patak'.split('-') # PP

res = ''.join([ i[0] for i in name_list ])
print(res)
