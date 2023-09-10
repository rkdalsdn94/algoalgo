# 백준 - 브론즈1 - 변수명 - 16205 - 구현, 문자열, 파싱 문제
'''
구현, 문자열, 파싱 문제

최대 글자의 길이가 100 밖에 안되므로 한 글자 씩 더하는 방식으로 풀었다.
입력받은 문자열을 카멜, 스네이크, 파스칼 표기법으로 출력하면 된다.
카멜, 스네이크, 파시칼 표기법을 각각의 함수로 따로 구현했다.

코드만 보고도 파악하기 쉬우므로 따로 설명은 안 적으려고 한다.
한 스텝씩 단계를 확인하고 싶으면 다음의 링크에서 아래 코드를 복사한 뒤 한 단계 씩 확인해보면 된다.
https://pythontutor.com/visualize.html#mode=edit
'''

num, word = input().split()


# 테스트
# num, word = '2', 'variable_n' # variableN  \  variable_n  \  VariableN
# num, word = '1', 'camelCase' # camelCase  \  camel_case  \  CamelCase
# num, word = '3', 'HowToSolveThisProblem' # howToSolveThisProblem  \  how_to_solve_this_problem  \  HowToSolveThisProblem
# num, word = '2', 'good' # good  \  good  \  Good

def camel_case(num, word):
    word = word[0].lower() + word[1:]
    res = ''

    if num == '1' or num == '3':
        res = word
    elif num == '2':
        flag = False

        for i in range(len(word)):
            if word[i] == '_':
                res += word[i + 1].upper()
                flag = True
                continue
            if flag:
                flag = False
                continue
            res += word[i]

    return res

def snake_case(num, word):
    res = ''

    if num == '1':
        for i in range(len(word)):
            if word[i].isupper():
                res += '_' + word[i].lower()
                continue
            res += word[i]
    elif num == '2':
        res = word
    elif num == '3':
        word = word[0].lower() + word[1:]

        for i in range(len(word)):
            if word[i].isupper():
                res += '_' + word[i].lower()
                continue
            res += word[i]

    return res

def pascal_case(num, word):
    word = word[0].upper() + word[1:]
    res = ''

    if num == '1' or num == '3':
        res = word
    elif num == '2':
        flag = False

        for i in range(len(word)):
            if word[i] == '_':
                res += word[i + 1].upper()
                flag = True
                continue
            if flag:
                flag = False
                continue
            res += word[i]

    return res

print(camel_case(num, word))
print(snake_case(num, word))
print(pascal_case(num, word))
