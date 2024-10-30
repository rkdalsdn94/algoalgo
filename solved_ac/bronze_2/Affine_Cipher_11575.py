# 백준 - 브론즈2 - Affine Cipher - 11575 - 구현, 문자열 문제
'''
구현, 문자열 문제

아핀 암호는 암호학에서 사용되는 암호화 기법 중 하나이다.
아핀 암호는 다음과 같은 식으로 이루어진다.
        E(x) = (ax + b) mod 26
여기서 E(x)는 암호화된 문자, x는 평문 문자, a와 b는 암호화에 사용되는 키이다.

풀이 과정
    1. 테스트 케이스의 개수를 입력받는다.
    2. 테스트 케이스의 개수만큼 반복하면서 a, b, word를 입력받는다.
    3. word를 순회하면서 아핀 암호를 적용한다.
    4. 아핀 암호를 적용한 결과를 출력한다.

in
    2
    3 1
    IAMSPY
    5 3
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
out
    ZBLDUV
    DINSXCHMRWBGLQVAFKPUZEJOTY
'''

def affine_cipher(a, b, word):
    res = ''
    for w in word:
        res += chr((a * (ord(w) - ord('A')) + b) % 26 + ord('A'))
    return res

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    word = input()
    print(affine_cipher(a, b, word))
