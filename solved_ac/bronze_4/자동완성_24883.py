# 백준 - 브론즈4 - 자동완성 - 24883 - 단순 구현 문제
'''
단순 구현 문제

입력으로 들어온 단어가 'N', 'n' 인지 검사하고 출력 하면 된다.
'N'또는 'n'일 때는 'Naver D2' 아닐 경우 'Naver Whale'을 출력하면 된다.
'N'과 'n'의 검사는 해당 글자를 소문자로 바꾼 후 진행했다.
'''

print('Naver D2') if input().lower() == 'n' else print('Naver Whale')
