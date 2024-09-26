# 백준 - 브론즈2 - Ragaman - 14043 - 구현, 문자열 문제
'''
구현, 문자열 문제

단순히 문자의 개수를 세어서 '*'의 개수를 빼면 된다.
이때 '*'의 개수가 0보다 작다면 'N'을 출력하고, 아니라면 'A'를 출력하면 된다.

풀이 과정
    1. word1, word2를 입력받는다.
    2. word1_counter, word2_counter를 만들어 각각의 문자의 개수를 센다.
    3. star_cnt를 word2에서 '*'의 개수를 센다.
    4. word1_counter를 돌면서 word2_counter보다 작다면 word1_counter - word2_counter를 한 값을 star_cnt에서 뺀다.
        4.1. star_cnt가 0보다 작다면 'N'을 출력하고 종료한다.
    5. 'A'를 출력한다.
'''

from collections import Counter

word1, word2 = input(), input()

# 테스트
# word1, word2 = 'abbc', 'baaa' # N
# word1, word2 = 'cccrocks', 'socc*rk*' # A

word1_counter, word2_counter = Counter(word1), Counter(word2)
star_cnt = word2.count('*')

for i in word1_counter:
    if word2_counter[i] < word1_counter[i]:
        star_cnt -= word1_counter[i] - word2_counter[i]

        if star_cnt < 0:
            print('N')
            exit(0)
print('A')
