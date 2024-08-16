# 백준 - 실버3 - 토크나이저 - 27649 - 구현, 문자열, 파싱 문제
'''
구현, 문자열 파싱 문제

처음에 reaplce 함수가 문자열 전체를 바꿔 주는지 기억이 잘 안나 단순하게 완전 탐색으로 풀었다가 시간 초과가 나왔다.
    - 전체를 다 바꿔준다.
    - ex) 'aaaaaabbbbccc' 라는 문자열에서 replace('a', '가') 로 바꾸면 'a' 모두가 '가'로 바뀐다.
위 방식으로 다 풀고 정규 표현식을 공부해보려고 검색하면서 방식을 찾았다.

풀이 과정
    1. 입력을 받는다.
    2. replace를 활용하여 '<', '>', '&&', '||', '(', ')'를 ' < ', ' > ', ' && ', ' || ', ' ( ', ' ) '로 바꾼다.
    3. ' '를 기준으로 split하여 ' '.join을 이용해 출력한다.
'''

'''
replace를 활용한 풀이
'''
word = input()
# 테스트
# word = 'grep skku   <infile> outfile' # grep skku < infile > outfile
# word = '(exit $?  )||expr $? + $?' # ( exit $? ) || expr $? + $?
# word = 'grep Wall <Makefile|| echo NotSetCflagsWall>outfile' # grep Wall < Makefile || echo NotSetCflagsWall > outfile

conditions = ['<', '>', '&&', '||', '(', ')']
for i in word:
    word = word.replace(op, f' {i} ')
print(' '.join(word))

### 정규 표현식 풀이
'''
정규 표현식 풀이
'''
import re

word = input()
# 테스트
# word = 'grep skku   <infile> outfile' # grep skku < infile > outfile
# word = '(exit $?  )||expr $? + $?' # ( exit $? ) || expr $? + $?
# word = 'grep Wall <Makefile|| echo NotSetCflagsWall>outfile' # grep Wall < Makefile || echo NotSetCflagsWall > outfile

pattern = r'(\|\||&&|[<>()[\]])'
word = re.sub(pattern, r' \1 ', word)
res = re.sub(r'\s+', ' ', word).strip()

print(res)
