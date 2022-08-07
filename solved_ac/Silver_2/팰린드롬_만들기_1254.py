'''
문자열, 완전 탐색 문제

팰린드롬을 구하는 문제랑 유사하지만 조금 더 응용해야 풀 수있는 문제이다.
문자(s)를 입력 받은 후 입력받은 문자의 길이 만큼 반복하면서 slicing을 활용하여 풀었다.
과정 1. s에서 반복되는 범위부터 시작해서 하나랑
    2. 똑같이 시작하는걸 반대로 비교하는거 하나에서 같다면
    3. 문자열의 길이에서 얼만큼 반복됐는지 더하고 출력하면 된다.
'''

s = input()

for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        print(len(s) + i)
        break


# 테스트
# for j in ['abab','abacaba','qwerty','abdfhdyrbdbsdfghjkllkjhgfds']:
#     s=j
#     for i in range(len(s)):
#        # print(s[i:][::-1])
#         if s[i:]==s[i:][::-1]:
#             print(len(s) + i)
#             break # 5, 7, 11. 38