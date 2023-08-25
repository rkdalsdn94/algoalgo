# 백준 - 브론즈1 - 애너그램 - 6996 - 단순 구현, 문자열, 정렬 문제
'''
단순 구현, 문자열, 정렬 문제

Counter 함수를 이용해서 풀었는데, 정렬을 사용해서도 풀 수 있다.
단순히 sorted(a) == sorted(b) 이렇게 해도 된다.

in
    3
    blather reblath
    maryland landam
    bizarre brazier
out
    blather & reblath are anagrams.
    maryland & landam are NOT anagrams.
    bizarre & brazier are anagrams.
'''

from collections import Counter

t = int(input())
for _ in range(t):
    a, b = input().split()

    if Counter(a) == Counter(b):
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')
