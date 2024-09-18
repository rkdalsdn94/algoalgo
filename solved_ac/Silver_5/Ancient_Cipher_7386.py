# 백준 - 실버5 - Ancient Cipher - 7386 - 구현, 문자열, 정렬 문제
'''
구현, 문자열, 정렬 문제

처음에 문제가 잘 이해되지 않아 여러 번 다시 읽은 문제이다.
문제 이해만 되면 쉽게 구할 수 있는 문제인데, 영어를 잘 몰라 오래 걸렸다..
최종적인 풀이는 각각의 문자를 카운트한 리스트를 만들어 정렬한 결과가 같은지 비교하면 된다.

풀이 과정
    - first_word, second_word를 입력받는다.
    - word_cnt 함수를 만들어 각각의 문자를 카운트한 리스트를 반환한다.
    - first_ck, second_ck에 word_cnt 함수를 적용한다.
    - first_ck와 second_ck를 비교하여 같으면 YES, 다르면 NO를 출력한다.
'''

first_word, second_word = input(), input(),

# 테스트
# first_word, second_word = 'JWPUDJSTVP', 'VICTORIOUS' # YES
# first_word, second_word = 'MAMA', 'ROME' # NO
# first_word, second_word = 'HAHA', 'HEHE' # YES
# first_word, second_word = 'AAA', 'AAA' # YES
# first_word, second_word = 'NEERCISTHEBEST', 'SECRETMESSAGES' # NO

def word_cnt(word):
    word_list = [0] * 26

    for i in word:
        word_list[ord(i) - 65] += 1

    return sorted(word_list)

first_ck, second_ck = word_cnt(first_word), word_cnt(second_word)
print('YES' if first_ck == second_ck else 'NO')
