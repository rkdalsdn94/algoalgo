# 백준 - 단어 나누기 - 실버5 - 1251 - 구현, 문자열, 완전 탐색, 정렬 문제
'''
구현, 문자열, 완전 탐색, 정렬 문제

2중 for문과 list slicing을 이용해서 문제를 풀면 된다.
입력으로 들어온 문자열을 list형으로 바꾼다. (reverse() 함수를 쓰기 위해)
문제에 '주어진 단어를 세 개의 더 작은 단어로 나누는 것이다. 각각은 적어도 길이가 1 이상인 단어여야 한다.' 라는 조건을 만족하기 위해
첫 번째 반복문을 1 부터 시작하고 slicing을 활요하기 위해 두 번째 반복문은 i + 1로 시작하면 된다.
그 다음 a = word[:i], b = word[i:j], c = word[j:]로 슬라이싱을 이용한다.
문자열을 다 뒤집은 후 res에 다 담고, 출력하기 전에 정렬을 한 후 출력하면 된다.
'''

word = list(input())

# 테스트
# word = list('mobitel') # bometil

res = []

for i in range(1, len(word)):
    for j in range(i + 1, len(word)):
        a, b, c = word[:i], word[i:j], word[j:]
        a.reverse(); b.reverse(); c.reverse()
        res.append(a + b + c)

print(''.join(sorted(res)[0]))
