# 백준 - 서로 다른 부분 물자열의 개수 - 실버3 - 11478 - 자료 구조, 문자열, 집합(set)
'''
자료 구조, 문자열, 집합(set)

set 자료 구조와 리스트 슬라이싱을 활용해서 문제를 풀면 된다.
'''

s = input()

# 테스트
# s = 'ababc' # 12

res = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        res.add(s[i:j + 1])

print(len(res))
