# 백준 - 실버1 - 문자열 교환 - 1522 - 완전 탐색, 슬라이딩 윈도우 문제
'''
완전 탐색, 슬라이딩 윈도우 문제

전체 'a'의 개수를 확인, 문자열을 확장, 슬라이딩 윈도우를 적용해서 'b'의 개수를 확인하는 문제이다.

풀이 과정
    1. 문자열을 입력받는다.
    2. 문자열에서 a의 개수를 temp에 저장한다.
    3. 문자열의 길이를 temp만큼 늘려서 word에 저장한다.
    4. res를 무한대로 초기화한다.
    5. word를 순회하면서 word[i: i + temp]에서 b의 개수를 센다.
    6. res에 word[i: i + temp]에서 b의 개수를 저장한다.
    7. res를 출력한다.
'''

word = input()

# 테스트
# word = 'abababababababa' # 3
# word = 'ba' # 0
# word = 'aaaabbbbba' # 0
# word = 'abab' # 1
# word = 'aabbaaabaaba' # 2
# word = 'aaaa' # 0

temp = word.count('a')
word += word[0 : temp - 1]
res = float('inf')

for i in range(len(word) - (temp - 1)): # 슬라이딩 윈도우로 이동하면서 b의 개수를 센다.
    res = min(res, word[i: i + temp].count('b'))

print(res)
