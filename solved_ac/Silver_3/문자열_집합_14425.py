# 백준 - 문자열 집합 - 14425 - 실버3 - 자료 구조, 문자열 문제
'''
자료 구조, 문자열 문제

set을 활용해서 문제를 풀었다.

처음 n 만큼 set 자료 구조로 input을 입력받고, (words)
다음 m 만큼 list로 input을 입력 받는다. (check_word)
그 다음 check_word에 한 글자씩 꺼내면서 words에 있는지 확인하고 있으면 + 1을 한다. (res)
마지막으로 1씩 추가한 res를 출력하면 된다.
'''

n, m = map(int, input().split())
words = set( input() for _ in range(n) )
check_word = [ input() for _ in range(m) ]

# 테스트
# n, m = 5, 11
# words = { 'baekjoononlinejudge', 'codingsh', 'codeplus', 'sundaycoding', 'startlink' }
# check_word = [ 'baekjoon', 'codeplus', 'codeminus', 'startlink', 'starlink',
#     'sundaycoding', 'codingsh', 'codinghs', 'sondaycoding', 'startrink', 'icerink' ] # 4

res = 0

for i in check_word:
    if i in words:
        res += 1

print(res)
