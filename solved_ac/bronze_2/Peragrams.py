# 백준 - 브론즈2 - Peragrams - 11195 - 구현, 문자열, 에드 훅 문제
"""
구현, 문자열, 에드 훅 문제

[핵심 아이디어]
    palindrome이 되기 위한 조건은 홀수 개인 문자가 최대 1개만 존재해야 함
    각 문자의 개수를 세어서 홀수 개인 문자의 개수를 파악하고, 홀수 개인 문자가 2개 이상이면 그 중 일부 제거

[풀이 과정]
    1. 입력 문자열의 각 문자별 개수를 딕셔너리로 카운트
    2. 홀수 개인 문자의 개수를 계산
    3. 홀수 개인 문자가 1개 이하면 제거할 필요 없음 (이미 palindrome 가능)
    4. 홀수 개인 문자가 2개 이상이면 (홀수 개수 - 1)만큼 제거 필요
"""

s = input().strip()

# 테스트
# s = 'abc' # 2
# s = 'aab' # 0

# 각 문자의 개수를 세기
count = {}
for char in s:
    count[char] = count.get(char, 0) + 1

# 홀수 개인 문자의 개수 세기
odd_count = 0
for char_count in count.values():
    if char_count % 2 == 1:
        odd_count += 1

# palindrome이 되려면 홀수 개인 문자가 최대 1개만 있어야 함
# 홀수 개인 문자가 2개 이상이면 (홀수 개수 - 1)만큼 제거
if odd_count <= 1:
    print(0)
else:
    print(odd_count - 1)
