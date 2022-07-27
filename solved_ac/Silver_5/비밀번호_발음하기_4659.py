'''
구현, 문자열 문제

출력할때 마침표가 있는지 확인해야 된다...
모음, 자음을 체크할 숫자 변수 하나씩, Counter 자료 구조를 활용한 vowels_cnt
모음이 1개라도 있는지 확인하기 위해 모음 vowels_cnt
최종 확인을 위한 flag

나머지는 단어를 한 글자씩 돌면서 연속되는 모음과 자음이 있는지 확인한다.
e와 o는 2글자씩 나올수 있으므로 예외로 둔다.

in
    a
    tv
    ptoui
    bontres
    zoggax
    wiinq
    eep
    houctuh
    end
out
    <a> is acceptable.
    <tv> is not acceptable.
    <ptoui> is not acceptable.
    <bontres> is not acceptable.
    <zoggax> is not acceptable.
    <wiinq> is not acceptable.
    <eep> is acceptable.
    <houctuh> is acceptable.
'''

from collections import Counter

while 1:
    word = input()
    flag = True
    vowels_ck = Counter(word)
    vowels_cnt = 0
    temp = ''
    vowels_repeated_cnt, consonants_repeated_cnt = 0, 0

    if word == 'end':
        break

    for vowel in list('aeiou'): # Counter 자료 구조로 글자를 분리한 후 dict에서 해당 키에 숫자가 있으면 더해준다
        if vowels_ck[vowel] != 0:
            vowels_cnt += 1

    if vowels_cnt == 0: # 모음이 없으면 vowels_cnt가 0이므로 더 실행하지 않고 다음 입력을 받는다.
        print(f'<{word}> is not acceptable.')
    else:
        for i in word: # 입력받은 단어를 돌면서
            if i in list('aeiou'): # 모음인지 확인
                vowels_repeated_cnt += 1
                consonants_repeated_cnt = 0

                if vowels_repeated_cnt > 2: # 모음이 연속으로 3번 들어오는지 체크
                    flag = False
                    break
                if temp == i: # 모음일때 이전 글자가 e, o는 허용
                    if i == 'e' or i == 'o':
                        pass
                    else:
                        flag = False
                        break
            else: # 자음인 상황
                consonants_repeated_cnt += 1
                vowels_repeated_cnt = 0

                if consonants_repeated_cnt > 2: # 자음이 연속으로 3번 들어오는지 체크
                    flag = False
                    break
                if temp == i: # 연속으로 같은 글자가 들어오는지
                    flag = False
                    break
            temp = i

        if flag:
            print(f'<{word}> is acceptable.')
        else:
            print(f'<{word}> is not acceptable.')