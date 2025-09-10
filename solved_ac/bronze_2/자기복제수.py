# 백준 - 브론즈2 - 자기복제수 - 2028 - 단순 수학 문제
"""
단순 수학 문제

[핵심 아이디어]
    어떤 수의 제곱이 그 수로 끝나는지를 확인하는 문제
    문자열로 변환하여 제곱 결과가 원래 수로 끝나는지 확인

[풀이 과정]
    1. 입력받은 수의 제곱을 계산
    2. 제곱 결과를 문자열로 변환
    3. 제곱 결과의 끝부분이 원래 수의 문자열과 일치하는지 확인
    4. 일치하면 "YES", 그렇지 않으면 "NO" 출력
"""

n = int(input())
n_list = [int(input()) for _ in range(n)]

# 테스트
# n = 4
# n_list = [1, 6, 76, 89]  # YES \ YES \ YES \ NO

for num in n_list:
    square = num * num
    str_num = str(num)
    str_square = str(square)

    if str_square.endswith(str_num):
        print("YES")
    else:
        print("NO")
