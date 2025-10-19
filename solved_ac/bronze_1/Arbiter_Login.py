# 백준 - 브론즈1 - Arbiter Login - 9388 - 구현, 문자열, 많은 조건 분기 문제
"""
구현, 문자열, 많은 조건 분기 문제

[핵심 아이디어]
    사용자가 비밀번호를 입력할 때 발생할 수 있는 실수를 체크:
    1. Caps Lock ON: 사용자가 타이핑할 때 대소문자가 반대로 입력됨
    2. Num Lock OFF: 사용자가 숫자를 타이핑했지만 입력되지 않음

    원본 비밀번호를 변환하여 입력된 비밀번호와 비교:
    - 원본 그대로 = 입력 → 성공
    - 원본의 대소문자 반전 = 입력 → Caps Lock 문제
    - 원본에서 숫자 제거 = 입력 → Num Lock 문제
    - 원본에서 숫자 제거 후 대소문자 반전 = 입력 → 둘 다 문제

[풀이 과정]
    1. 원본과 입력이 완전히 같으면 로그인 성공
    2. 원본에서 숫자를 제거한 후:
       - 입력과 같으면 Num Lock 문제
       - 대소문자를 반전했을 때 입력과 같으면 Caps Lock + Num Lock 문제
    3. 원본의 대소문자를 반전했을 때 입력과 같으면 Caps Lock 문제
    4. 모두 아니면 일반 오류

in
    6
    aaBBccDD aaBBccDD
    aaBBccDD aaBBccDD9
    aaBBccDD aaBBCCDD
    aaBBccDD AAbbCCdd
    a4B3c2D1 aBcD
    a4B3c2D1 AbCd
out
    Case 1: Login successful.
    Case 2: Wrong password.
    Case 3: Wrong password.
    Case 4: Wrong password. Please, check your caps lock key.
    Case 5: Wrong password. Please, check your num lock key.
    Case 6: Wrong password. Please, check your caps lock and num lock keys.
"""

def swap_case(s):
    """문자열의 모든 영문자 대소문자를 반전"""
    result = []
    for char in s:
        if char.isupper():
            result.append(char.lower())
        elif char.islower():
            result.append(char.upper())
        else:
            result.append(char)
    return ''.join(result)

def remove_digits(s):
    """문자열에서 모든 숫자 제거"""
    return ''.join(char for char in s if not char.isdigit())

n = int(input())

for i in range(1, n + 1):
    original, entered = input().split()

    # 케이스 1: 완전히 동일 -> 로그인 성공
    if original == entered:
        print(f"Case {i}: Login successful.")
        continue

    # 원본에서 숫자를 제거한 버전
    original_no_digits = remove_digits(original)

    # 케이스 2: 원본(대소문자 반전) == 입력 -> Caps Lock 문제
    if swap_case(original) == entered:
        print(f"Case {i}: Wrong password. Please, check your caps lock key.")
        continue

    # 케이스 3: 원본(숫자 제거) == 입력 -> Num Lock 문제
    if original_no_digits == entered:
        print(f"Case {i}: Wrong password. Please, check your num lock key.")
        continue

    # 케이스 4: 원본(숫자 제거 + 대소문자 반전) == 입력 -> 둘 다 문제
    if swap_case(original_no_digits) == entered:
        print(f"Case {i}: Wrong password. Please, check your caps lock and num lock keys.")
        continue

    # 케이스 5: 모두 해당 없음 -> 일반 오류
    print(f"Case {i}: Wrong password.")
