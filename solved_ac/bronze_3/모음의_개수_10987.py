# 백준 - 브론즈3 - 모음의 개수 - 10987 - 단순 구현, 문자열 문제
'''
단순 구현, 문자열 문제

입력으로 들어온 문자에서 (a, e, i, o, u) 의 개수를 다 합친 후 출력하면 된다.

다른 사람의 풀이를 참고하면 아래처럼 푸는게 함수형 느낌으로 좋은거 같다.
res = sum(map(word.count, 'aeiou'))
'''

word = input()

# 테스트
# word = 'baekjoon' # 4

res = 0
res += word.count('a')
res += word.count('e')
res += word.count('i')
res += word.count('o')
res += word.count('u')

print(res)
