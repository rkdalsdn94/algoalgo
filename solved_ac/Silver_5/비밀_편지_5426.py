# 백준 - 실버5 - 비밀 편지 - 5426 - 수학, 구현, 문자열 문제
'''
수학, 구현, 문자열 문제

풀이 과정
 1. 테스트 케이스를 입력받는다.
 2. 문자열을 입력받고, 문자열의 길이의 제곱근을 구한다.
 3. 제곱근을 이용하여 문자열을 해독한다.
 4. 해독한 문자열을 출력한다.

in
    3
    RSTEEOTCP
    eedARBtVrolsiesuAoReerles
    EarSvyeqeBsuneMa
out
    TOPSECRET
    RosesAreRedVioletsAreBlue
    SquaresMayBeEven
'''

t = int(input())
for _ in range(t):
    word = input()
    square_root = int(len(word) ** (1 / 2))

    decord_word = ''
    for i in range(square_root, 0, -1):
        for j in range(i, square_root * square_root + 1, square_root):
            decord_word += word[j - 1]

    print(decord_word)
