# 백준 - 브론즈2 - 재귀의 귀재 - 25501 - 재귀, 구현, 문자열 문제
'''
재귀, 구현, 문자열 문제

재귀 문제들의 기초를 쌓기 위해 당분간 재귀 문제들만 풀려고 한다.
문제의 답이 있는데 안보고 풀 수 있는 정도다.
Palindrome 인지 검사하는 수와 recursive 함수가 몇 번 호출 됐는지 출력하면 된다.
함수가 몇 번 호출 됐는지 검사하는 방법은 테스트 케이스 내에서 cnt를 0으로 초기화하고, recursive 함수에서 global로 된 cnt를 1씩 증가시키면 된다.
'''

t = int(input())

def recursive(word, left, right):
    global cnt
    cnt += 1

    if left >= right:
        return 1
    elif word[left] != word[right]:
        return 0
    return recursive(word, left + 1, right - 1)

def isPalindrome(s):
    return recursive(s, 0, len(s) - 1)

for _ in range(t):
    cnt = 0
    s = input()
    print(isPalindrome(s), cnt)
