# 백준 - 브론즈1 - 히든 넘버 - 8595 - 문자열, 파싱 문제
'''
문자열, 파싱 문제

입력으로 들어온 문자에서 isnumeric 함수를 통해 숫자면 temp에 담는다.
숫자가 아니고, temp의 값이 있다면 res에 int값으로 바꾼 뒤 temp를 빈 문자열로 다시 만든다.
위 과정을 n 길이만큼 반복한다.

처음에 이렇게 풀었을 때 5% 정도에서 틀렸었다. 질문 게시판에도 관련된 얘기가 없어서 고민하다 반례를 생각했다.
반례는 다음과 같다. 'word 자체가 숫자로 이루어졌을 경우' (또는, 마지막에 추가되지 못한 숫자들)

in
    5
    12345
out
    12345

이렇게 된 경우 temp 에만 값이 들어가고 res에는 추가되지 않은 상황이므로 for 문이 끝난 뒤 temp가 값이 있는지 검사한 후 res에 값을 추가해야 된다.
'''

n = int(input())
word = input()

# 테스트
# n = 14
# word = 'ab13c9d07jeden' # 29

res = 0
temp = ''

for i in range(n):
    if word[i].isnumeric():
        temp += word[i]
    elif temp:
        res += int(temp)
        temp = ''

if temp:
    res += int(temp)

print(res)
