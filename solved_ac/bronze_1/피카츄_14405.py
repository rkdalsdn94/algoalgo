# 백준 - 브론즈1 - 피카츄 - 14405 - 문자열 문제
'''
문자열 문제

'백준 - 크로아티아 알파벳(2941)' 문제랑 비슷하게 풀 수 있다.

입력받은 문자 s에서 ["pi", "ka", "chu"]를 '#'으로 replace 시킨다.
위 작업을 완료한 뒤 '#'을 빈 문자열로 다시 replace 한다.
이후 값이 남이 있다면 ["pi", "ka", "chu"]로 이루어지지 않은 문자열이므로 'NO'를 출력하고,
빈 문자열로 됐다면 'YES'를 출력하면 된다.

처음에 바로 빈 문자열로 replace 했다가 실패했다.
왜 그런지 이해가 안돼 질문 게시판을 찾아보는 다음과 같은 내용을 발견했다.
    [반례]
    'kpia' - [ 정답 ] NO

"pi" 가 빈 문자열로 replace 되므로 남아 있는 글자는 "ka"로 변한다. 다음 "ka"가 빈 문자열로 replace 되므로 원래는 NO 나와야 되는데 YES가 출력될 수도 있다.
따라서 바로 빈 문자열로 바꾸지 말고, '#' 이든, '~' 든 문제 상에서 사용되지 않을 값으로 바꾼 뒤 최종적으로 replace 하는 것이 좋다.
'''

s = input()

# 테스트
# s = 'pikapi' # YES
# s = 'pipikachu' # YES
# s = 'pikaqiu' # NO
# s = 'piika' # NO
# s = 'chupikachupipichu' # YES
# s = 'kpia' # NO

for i in ['pi', 'ka', 'chu']:
    s = s.replace(i, '#')

s = s.replace('#', '')
if s:
    print('NO')
else:
    print('YES')
