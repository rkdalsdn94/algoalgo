# 백준 - 브론즈1 - Odd Palindrome - 15104 - 문자열, 완전 탐색 문제
"""
문자열, 완전 탐색 문제

[핵심 아이디어]
    1. 짝수 길이의 palindrome이 존재하는지 확인해야 함
    2. 가장 간단한 짝수 길이 palindrome은 연속된 같은 문자 2개 (예: "aa", "bb")
    3. 문자열에 연속된 같은 문자가 있으면 짝수 길이 palindrome이 존재함
    4. 연속된 같은 문자가 없으면 모든 palindrome이 홀수 길이

[풀이 과정]
    1. 문자열을 순회하면서 현재 문자와 다음 문자가 같은지 확인
    2. 연속된 같은 문자가 발견되면 "Or not." 출력
    3. 끝까지 연속된 같은 문자가 없으면 "Odd." 출력
"""

s = input()

# 테스트
# s = 'amanaplanacanalpanama' # Odd. (연속된 같은 문자 없음)
# s = 'madamimadam' # Odd. (연속된 같은 문자 없음)
# s = 'annamyfriend' # Or not. ("nn"이 있음)
# s = 'nopalindromes' # Odd. (연속된 같은 문자 없음)

# 연속된 같은 문자가 있는지 확인
res = False
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        res = True
        break

if res:
    print('Or not.')
else:
    print('Odd.')
