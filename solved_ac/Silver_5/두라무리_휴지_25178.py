# 백준 - 실버5 - 두라무리 휴지 - 25178 - 구현, 문자열 문제
'''
구현, 문자열 문제

문제에서 주어진 조건들을 구현하면 되는 문제이다. 아래 문제의 조건이 있다.
 조건1 - 한 단어를 재배열해 다른 단어를 만들 수 있어야 한다.
 조건2 - 두 단어의 첫 글자와 마지막 글자는 서로 동일해야 한다.
 조건3 - 각 단어에서 모음(a, e, i, o, u)을 제거한 문자열은 동일해야 한다.

처음에 문제를 풀 때 조건1이 이해가 잘 안돼서 질문 게시판을 찾았는데 아래 링크에 있는 질문의 답변이 이 문제를 푸는데 도움이 됐다
답변의 내용만 보면 아래와 같다.
> "다른"이 그런 의미의 다른이 아닌 것 같습니다. A랑 B가 있을 때 A를 "한"으로 지칭하면 보통 B를 "다른"이라고 지칭합니다. <
질문 글의 주소는 여기이다. https://www.acmicpc.net/board/view/97601

즉, word_a와 word_b의 글자 수가 같아야지 조건1을 달성할 수 있다. -> 따라서 Counter를 사용했다.
'''

from collections import Counter

n = int(input())
word_a, word_b = input(), input()

# 테스트
# n = 8
# word_a, word_b = 'durumari', 'duramuri' # YES
# n = 8
# word_a, word_b = 'durumari', 'darmurui' # YES
# n = 8
# word_a, word_b = 'durumari', 'dumurari' # NO
# n = 8
# word_a, word_b = 'durumari', 'darumari' # NO
# n = 8
# word_a, word_b = 'durumari', 'abcdefgh' # NO

res = 'NO'

word_a_cnt, word_b_cnt = Counter(word_a), Counter(word_b)
vowels = ['a', 'e', 'i', 'o', 'u']
new_word_a = [ ''.join(i) for i in word_a if i not in vowels ]
new_word_b = [ ''.join(i) for i in word_b if i not in vowels ]

if word_a_cnt == word_b_cnt: # 조건1 - 한 단어를 재배열해서 다른 단어로 만드려면 각가의 단어들이 갖고있는 글자가 맞아야 된다.
    if word_a[0] == word_b[0] and word_a[-1] == word_b[-1]: # 조건2 - 두 단어의 첫 글자와 마지막 글자는 서로 동일해야 된다.
        if new_word_a == new_word_b: # 조건3 - 각 단어에서 모음을 제거한 문자열은 동일해야 된다.
            res = 'YES'

print(res)
