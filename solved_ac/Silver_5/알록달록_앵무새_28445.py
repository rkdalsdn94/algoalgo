# 백준 - 실버5 - 알록달록 앵무새 - 28445 - 구현, 문자열, 정렬 문제
'''
구현, 문자열, 정렬 문제

알고리즘 분류에서 '트리를 사용한 집합과 맵, 자료 구조'도 있지만 내 풀이에선 set을 단순하게 사용하는 거라 안 적었다.
itertools 모듈 중 product 함수를 사용해서 쉽게 풀 수 있다. 해당 함수의 사용법을 모른다면 아래 링크를 보면 된다.
    - https://stackstackstack.tistory.com/entry/python-순열-조합-함수-product-permutations-combinations
    - product 뿐 아니라 itertools 전반적으로 사용하는 방식에 대해 다룬다. (짧게 설명되어 있음)
    - product를 간단하게 요약하면 다음과 같다.
    - 데카르트 곱(cartesian product), 중첩된 for 루프와 동등합니다.

입력으로 '아빠 새의 두 가지 색', '엄마 새의 두 가지 색' 이렇게 주어지므로 product 두 번째 인자인 repeat을 2로 주면 된다.
후에 중복을 제거하기 위해 set()을 사용하고 해당 값들을 list로 변환한 뒤 정렬 후 출력하면 된다.
'''

from itertools import product

father_list = list(input().split())
mother_list = list(input().split())

# 테스트
# father_list = ['blue', 'purple']
# mother_list = ['green', 'green']
'''
    blue blue
    blue green
    blue purple
    green blue
    green green
    green purple
    purple blue
    purple green
    purple purple
'''
# father_list = ['white', 'purple']
# mother_list = ['yellow', 'purple']
'''
    blue blue
    blue purple
    blue white
    blue yellow
    purple blue
    purple purple
    purple white
    purple yellow
    white blue
    white purple
    white white
    white yellow
    yellow blue
    yellow purple
    yellow white
    yellow yellow
'''

color_list = father_list + mother_list
res = list(set(product(color_list, repeat = 2)))
for i in sorted(res):
    print(*i)
