# 백준 - 실버3 - 여우는 어떻게 울지? - 9536 - 구현, 문자열, 파싱 문제
'''
구현, 문자열, 파싱 문제

문자열을 파싱하여 출력하는 문제이다.

풀이 과정
1. 테스트 케이스의 수를 입력받고, 테스트 케이스의 수만큼 반복한다.
2. 녹음된 소리를 입력받는다.
3. 동물 소리를 입력받는다. (중복을 제거하기 위해 set 사용)
    3.1. 동물 소리를 입력받을 때까지 반복한다. (마지막 글자가 say?가 될 때까지)
4. 녹음된 소리를 동물 소리와 비교하여 출력한다.
    4.1. 녹음된 소리가 동물 소리에 포함되어 있으면 continue
    4.2. 그렇지 않다면 출력한다.

in
    1
    toot woof wa ow ow ow pa blub blub pa toot pa blub pa pa ow pow toot
    dog goes woof
    fish goes blub
    elephant goes toot
    seal goes ow
    what does the fox say?v
out
    wa pa pa pa pa pa pow
'''

t = int(input())
for _ in range(t):
    sounds = list(input().split())
    animals = set()

    while 1:
        sound = input().split()[-1]

        if sound == 'say?':
            break

        animals.add(sound)

    for i in sounds:
        if i in animals:
            continue
        print(i, end=' ')
