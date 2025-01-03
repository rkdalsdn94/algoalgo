# 백준 - 브론즈1 - 2의 보수 - 24389 - 수학, 비트 마스킹 문제
'''
수학, 비트 마스킹 문제

핵심 아이디어
    - 2의 보수를 계산하는 문제
    - 2의 보수는 1의 보수에 1을 더한 값이다.
    - 1의 보수는 모든 비트를 반전시킨 값이다.
    - 32비트 정수로 표현하기 위해 마스킹을 사용한다.
    - XOR 연산을 통해 다른 비트를 찾는다.
    - 1인 비트의 개수를 센다.

풀이 과정
    1. 정수 n을 입력받는다.
    2. 32비트 정수로 표현하기 위한 마스크를 생성한다.
    3. 2의 보수를 계산한다.
    4. XOR 연산을 통해 다른 비트를 찾는다.
    5. 1인 비트의 개수를 센다.
    6. 결과를 출력한다.
'''

n = int(input())

# 테스트
# n = 2 # 30

def count_different_bits(n):
    # 32비트 정수로 표현
    original = n

    # 32비트 범위로 제한하기 위한 마스크
    MASK_32BIT = (1 << 32) - 1

    # 2의 보수 계산:
    # 1. 모든 비트 반전 (~N)
    # 2. 1을 더함
    # 3. 32비트로 마스킹
    complement = ((~n) + 1) & MASK_32BIT

    # XOR 연산으로 다른 비트 찾기
    # XOR은 두 비트가 다를 때 1을 반환
    xor_res = original ^ complement

    # 1인 비트 개수 세기
    cnt = bin(xor_res).count('1')

    return cnt

print(count_different_bits(n))
