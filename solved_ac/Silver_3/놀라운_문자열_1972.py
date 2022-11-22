# 백준 - 놀라운 문자열 - 1972 - 실버3 - 문자열, 자료 구조(set), 구현 문현
'''
문자열, 자료 구조(set), 구현 문제

풀이 과정
1. word가 '*'이 될 때까지 while 반복문을 실행한다.
2. word의 길이를 1부터 len(word) - 1 까지 반복한다.
    2.1 매 반복 때마다 word_set이라는 변수를 set타입으로 만든다.
    2.2 단어를 쪼개기 위해 len(word) - i 이 전 반복분의 값을 뺀 값으로 다시 반복한다.
    2.3 divide_word 라는 변수에 입력으로 주어진 단어를 쪼개 만들어준다.
    2.4 쪼갠 단어가 word_set에 있으면 놀라운 문자열이 아니므로 출력하고 break를 한 다음 반복문을 진행한다.
3. len(word) - 1 길이까지 다 통과했으면 놀라운 문자열이 맞으므로 해당 값을 출력하면 된다.

in
    ZGBG
    X
    EE
    AAB
    AABA
    AABB
    BCBABCC
    *
out
    ZGBG is surprising.
    X is surprising.
    EE is surprising.
    AAB is surprising.
    AABA is surprising.
    AABB is NOT surprising.
    BCBABCC is NOT surprising.
'''

while 1:
    word = input().rstrip()

    if word == '*':
        break

    for i in range(1, len(word) - 1):
        word_set = set()

        for j in range(len(word) - i):
            divide_word = word[j] + word[i + j]

            if divide_word in word_set:
                print(f'{word} is NOT surprising.')
                break
            else:
                word_set.add(divide_word)
        else:
            continue
        break
    else:
        print(f'{word} is surprising.')
