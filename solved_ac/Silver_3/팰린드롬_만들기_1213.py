'''
구현, 문자열, 그리디(?) 문제

Counter - (이터러블한 객체를 key(글자): value(해당 글자의 수) 형태로 반환하는 자료구조)
Counter 자료 구조를 활용해서 word의 한 글자씩 돌면서
홀수라면 아래와 같이 실행한다..
 - ck(팰린드롬이 가능한지 하는 체크 변수),
 - center(출력할 때 가운데 글자)
 - 가운데 글자를 word에서 제거한다. -> 나중에 res에 답을 담을 때 섞이지 않기 위해
홀수가 아니면 홀수일 경우가 1이 넘는지를 확인한다.

마지막 반복문으로 res변수를 word에 2범위로 담은 후 center랑 합쳐서 출력하면 된다.
'''

from collections import Counter

word = sorted(input())

# 테스트
# word = sorted('AABB') # ABBA
# word = sorted('AAABB') # ABABA
# word = sorted('ABACABA') # AABCBAA
# word = sorted('ABCD') # I'm Sorrty Hansoo
# word = sorted('AABBCC') # ABCCBA

temp = Counter(word)
ck = 0
center = ''
res = ''

for i in temp:
    if temp[i] % 2 != 0:
        ck += 1
        center += i
        word.remove(i)

    if ck > 1: # 홀수가 여러개일 경우 팰린드롬을 만들수 없다.
        print("I'm Sorry Hansoo")
        exit()

for i in range(0, len(word), 2):
    res += word[i]

print(res + center + res[::-1])
