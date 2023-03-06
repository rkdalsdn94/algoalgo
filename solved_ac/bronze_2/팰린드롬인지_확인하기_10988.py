# 백준 - 브론즈2 - 팰린드롬인지 확인하기 - 10988 - 구현, 문자열 문제
'''
구현, 문자열 문제

아래 코드 방식은 0번째 인덱스에서 증가하고, 마지막 인덱스에서 감소하면서 서로를 직접 비교했다.
0번째 인덱스와 마지막 인덱스 둘 사이에 다른 글자가 나오면 res를 False로 만들고 '0'을 출력한다.
다른 글자가 안나온다면 '1'을 출력한다.
'''

word = input()

# 테스트
# word = 'level' # 1
# word = 'baekjoon' # 0

word_cnt = 1
res = True

for i in range(len(word) // 2):
    if word[i] != word[-word_cnt]:
        res = False
        break
    word_cnt += 1

if res:
    print(1)
else:
    print(0)
