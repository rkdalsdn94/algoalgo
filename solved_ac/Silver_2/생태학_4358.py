# 백준 - 실버2 - 생태학 - 4358 - 문자열, 자료 구조(해시) 문제
'''
문자열, 자료 구조(해시) 문제

해시(파이썬은 딕셔너리)를 활용하면 되는 문제이다.
딕셔너리를 활용해 이미 있는 단어면 값을 1씩 증가시키고, 없다면 1로 만든다.
해당 값들을 모두 더해서 전체 단어의 개수를 구하고, 단어들을 정렬해서 출력하면 된다.

풀이 과정
    1. 입력을 받고, word_dict를 만든다.
    2. 입력을 받으면서 word_dict에 저장한다.
    3. word_dict의 값을 모두 더해서 total_word_cnt에 저장한다.
    4. word_dict의 key를 정렬해서 word_list에 저장한다.
    5. word_list를 돌면서 각 key의 비율을 계산해서 출력한다.

in
    Red Alder
    Ash
    Aspen
    Basswood
    Ash
    Beech
    Yellow Birch
    Ash
    Cherry
    Cottonwood
    Ash
    Cypress
    Red Elm
    Gum
    Hackberry
    White Oak
    Hickory
    Pecan
    Hard Maple
    White Oak
    Soft Maple
    Red Oak
    Red Oak
    White Oak
    Poplan
    Sassafras
    Sycamore
    Black Walnut
    Willow
out
    Ash 13.7931
    Aspen 3.4483
    Basswood 3.4483
    Beech 3.4483
    Black Walnut 3.4483
    Cherry 3.4483
    Cottonwood 3.4483
    Cypress 3.4483
    Gum 3.4483
    Hackberry 3.4483
    Hard Maple 3.4483
    Hickory 3.4483
    Pecan 3.4483
    Poplan 3.4483
    Red Alder 3.4483
    Red Elm 3.4483
    Red Oak 6.8966
    Sassafras 3.4483
    Soft Maple 3.4483
    Sycamore 3.4483
    White Oak 10.3448
    Willow 3.4483
    Yellow Birch 3.4483
'''

import sys; input=sys.stdin.readline

word_dict = {}

while 1:
    try:
        word = input().strip()

        if word == '':
            break

        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    except:
        break

total_word_cnt = sum(word_dict.values())
word_list = sorted(word_dict.keys())

for i in word_list:
    average =  word_dict[i] / total_word_cnt * 100
    print(f'{i} {average:.4f}')
