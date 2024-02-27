# 백준 - 실버3 - iSharp - 3568 - 문자열, 파싱 문제
'''
문자열, 파싱 문제

문제를 잘 읽고 파싱하고, replace를 통해 수정하고 구현하면 되는 문제이다. (난이도가 높은 편은 아님)
처음에 알파벳을 뒤집어서 출력해야 되는데, 이걸 체크해주지 않아 틀렸었다.

풀이 과정
 - 입력으로 들어온 문자열을 띄어쓰기 기준으로 split 한다.
 - split 한 값의 0번째 인덱스는 모두 공통으로 사용될 자료형이므로 data_type 이란 이름으로 담아둔다.
 - 이후 1번째 인덱스부터 for 문을 실행하고, 해당 단어의 ',' 와 ';' 를 제거한다.
 - 해당 단어를 한 글자씩 반복해서 알파벳인지 검사한다.
     - 알파벳이면 alpha 변수에 담아두고, 정답을 출력할 때 뒤집어서 출력하면 된다.
     - 알파벳이 아니면 두 글자('[' 와 ']')만 조심한 뒤 data_type2 라는 변수에 담는다.
        - 위 두 값이면 반대로 담아야 됨, 이 부분은 if 문으로 처리함
 - 각 변수를 적절한 위치에 더하고, 띄어쓰기(' ') 하나와 세미콜론(';')을 합친 뒤 출력하면 된다.
'''

word = input()

# 테스트
# word = 'int& a*[]&, b, c*;' # int&&[]* a;  \  int& b;  \  int&* c;
# word = 'dsafsd adsf[]&[]**&, dsaf&&&****, dsfa**&[]&&, rfsdgf**&&[]*, dasfs;'
# '''
# out
#     dsafsd&**[]&[] adsf;
#     dsafsd****&&& dsaf;
#     dsafsd&&[]&** dsfa;
#     dsafsd*[]&&** rfsdgf;
#     dsafsd dasfs;
# '''

word_list = word.split()
data_type = word_list[0]

for i in word_list[1:]:
    i = i.replace(',', '').replace(';', '')
    alpha = ''
    data_type2 = ''

    for j in i[::-1]:
        if not j.isalpha():
            if j == '[':
                data_type2 += ']'
            elif j == ']':
                data_type2 += '['
            else:
                data_type2 += j
        else:
            alpha += j

    print(data_type + data_type2 + ' ' + ''.join(list(alpha)[::-1]) + ';')
    # print(data_type + data_type2 + alpha + ';') # 처음 틀린 코드
