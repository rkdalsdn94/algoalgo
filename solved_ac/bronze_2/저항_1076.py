'''
완전 단순 구현이다.

문제의 표에서 곱을 보면 규칙이 생기는데,
규칙은 갑에서 10을 거듭제곱한 값이랑 똑같다.
'''

one, two, three = input(), input(), input()

# 테스트
# one, two, three = 'yellow', 'violet', 'red' # 4700
# one, two, three = 'orange', 'red', 'blue' # 32000000 -> 32,000,000
# one, two, three = 'white', 'white', 'white' # 99000000000 -> 99,000,000,000

resistance = {
    'black': 0, 'brown': 1, 'red': 2,
    'orange': 3, 'yellow': 4, 'green': 5,
    'blue': 6, 'violet': 7, 'grey': 8,
    'white': 9
}

print((resistance[one] * 10 + resistance[two]) * 10 ** resistance[three])
