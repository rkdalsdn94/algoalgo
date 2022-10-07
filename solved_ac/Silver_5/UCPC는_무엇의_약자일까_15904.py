# 백준 - UPCP는 무엇의 약자일까 - 15904 - 실버5 - 문자열, 그리디 문제
'''
문자열, 그리디 문제

입력으로 들어온 문자에서 공백을 제거한 후 반복문으로 해당 문자를 한 글자씩 확인하면서 'UCPC'인지 확인하면 된다.
'UCPC'인지 확인하는 방법은 index를 확인하기 위한 temp 변수를 하나 만든 후 U가 나온 다음 C, P, C 순서대로 나오는지 확인하면 된다.
사이에 다른 문자들이 나온다면 무시한다. 최종적으로 'UCPC' 가능한가 순서만 확인하면 된다.
'UCPC'라는 글자를 만들 수 있으면, res를 True로 바꾼 후 반복문을 종료하면서 'I love UCPC'를 출력하고,
만들 수 없으면 'I hate UCPC'를 출력하면 된다.
'''

UCPC = 'UCPC'

word_list = input().split()

# 테스트
# word_list = 'Union of Computer Programming Contest club contest'.split() # I love UCPC
# word_list = 'University Computer Programming'.split() # I hate UCPC
# word_list = 'UCPC'.split() # I love UCPC
# word_list = 'CPUC'.split() # I hate UCPC

res = False
temp = 0

for i in word_list:
    for j in i:
        if j == UCPC[temp]:
            temp += 1
        if temp == 4:
            res = True
            break
    if res:
        break

if res:
    print('I love UCPC')
else:
    print('I hate UCPC')
