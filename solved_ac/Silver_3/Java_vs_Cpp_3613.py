'''
구현, 문자열, 많은 조건 분기, 파싱 문제

괜히 많은 조건 분기가 들어간게 아닌거 같다.
생각보다 단순하면서 조건 처리해야 될 부분이 너무 많았다.
그래서 풀다가 잘 안풀려 질문 게시판에서 반례를 좀 찾아본 후에 찾을 수 있었다....

아래 테스트로 적어논 각 조건을 풀다보면 문제를 풀 수 있다.
'''

name = input()

# 테스트
# name = 'long_and_mnemonic_identifier' # longAndMnemonicIdentifier
# name = 'longAndMnemonicIdentifier' # long_and_mnemonic_identifier
# name = 'name' # 'name'
# name = 'C_c' # 'Error!'
# name = 'asd_' # Error! 
# name = '_asd' # Error!
# name = 'as__asd' # Error!
# name = 'Aasd' # Error!
# name = 'asdAasd_asd' # Error! ---> 여기서 에러가 난다.
# name = 'fadfadfadsf' # fadfadfadsf
# name = 'asdasdASDASD' # asdasd_a_s_d_a_s_d

ck = 0 # cpp인지 java인지 체크 -> 0 = cpp, 1 = java
res = ''

for i in name: # cpp인지 자바인지 체크
    if i.isupper():
        ck = 1
        break

def cpp_to_java(name): # cpp에서 자바로
    global res

    for i in range(1, len(name)): # '_'가 연속으로 나오는지 체크
        if name[i-1] == name[i] == '_':
            res = 'Error!'
            return
    if name[0] == '_' or name[-1] == '_': # 처음과 마지막이 '_'인지 체크
        res = 'Error!'
        return

    name = name.split('_')

    for i in name:
        if not i.isalnum(): # 알파벳이나 숫자가 아니면 에러
            res = 'Error!'
            return
        if i.lower() != i:
            res = 'Error!'
            return

    for i in range(len(name)):
        if i != 0:
            res += name[i][0].upper() + name[i][1:]
        else:
            res += name[i]
    return

def java_to_cpp(name): # 자바에서 cpp로
    global res

    for i in range(len(name)):
        if name[i] == '_': # 한 글자라고 '_'가 있으면 에러
            res = 'Error!'
            return

    temp = name[0]
    if temp.isupper(): # 첫 글자가 대문자인지
        res = 'Error!'
        return
    
    for i in range(1, len(name)):
        if name[i].isupper():
            temp += '_'
            temp += name[i].lower()
        else:
            temp += name[i]
    
    res = temp
    return

if ck:
    if name.lower() == name:
        print(name)
    else:
        java_to_cpp(name) # java에서 cpp로
else:
    cpp_to_java(name) # cpp에서 java로

print(res)