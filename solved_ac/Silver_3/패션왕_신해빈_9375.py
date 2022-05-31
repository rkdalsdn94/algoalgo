'''
수학, 자료 구조 문제 (set을 사용해서 풀 수 있을거 같다.)

' 해빈이는 패션에 매우 민감해서 한번 입었던 옷들의 조합을 절대 다시 입지 않는다.
예를 들어 오늘 해빈이가 안경, 코트, 상의, 신발을 입었다면, 다음날은 바지를 추가로 입거나 안경대신 렌즈를 착용하거나 해야한다.
해빈이가 가진 의상들이 주어졌을때 과연 해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까? '

위에 문제를 잘 풀어보면 아래와 같이 해석할 수 있다.
1 종류 이상의 의상 착용 + 같은 종류의 의상은 하나씩만 착용
문제 중 예를 보면 '안경, 코트, 상의, 신발' -> 주어졌을 때 안경만 쓰거나, 코트만 입거나, 상의만 입는 등.. 한 종류 이상만 착용하면 된다.
그래서 식으로 세워보면 각 종류의 의상을 입는 경우의 수를 곱해주면 된다.
(a 종류 의상 + 1) * (b 종류 의상 + 1) ...  마지막에서 - 1

- 1은 모든 의상을 착용하지 않았을 경우 제외
+ 1은 해당 종류의 의상을 착용할지 안할지 때문이다.

in
    2
    3
    hat headgear
    sunglasses eyewear
    turban headgear
    3
    mask face
    sunglasses face
    makeup face
out
    5
    3
'''

from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    robe = []

    for i in range(n):
        robe_name, robe_kind = input().split()
        robe.append(robe_kind)

    robe_counter = Counter(robe)
    res = 1

    for i in robe_counter:
        res *= robe_counter[i] + 1

    print(res - 1)
