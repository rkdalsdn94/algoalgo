# 백준 - 실버4 - 접미사 배열 - 11656 - 정렬, 문자열 문제
'''
정렬, 문자열 문제

문자열을 한 글자씩 빼면서 res에 추가한 후
정렬한 res를 출력하면 된다.
'''

s = input()

# 테스트
# s = 'baekjoon' # aekjoon  baekjoon  ekjoon  joon  kjoon  n  on  oon

res = []

for i in range(len(s)):
    res.append(s[i::])

for i in sorted(res):
    print(i)
