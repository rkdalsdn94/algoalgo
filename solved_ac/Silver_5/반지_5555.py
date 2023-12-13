# 백준 - 실버5 - 반지 - 5555 - 문자열, 완전 탐색 문제
'''
문자열, 완전 탐색 문제

입력으로 들어오는 문자열 리스으(n_list)에서 에서 word가 몇 번 나오는지 확인하면 되는 문제이다.
단, 시작과 긑이 연결되어 있는 부분을 '단어' + '단어' 이렇게 만들어서 ('abc'라면 'abcabc' 이렇게) 존재한다면 1씩 더하면 되는 문제이다.
'''

word = input()
n = int(input())
n_list = [input() for _ in range(n)]

# 테스트
# word = 'ABCD'
# n = 3
# n_list = ['ABCDXXXXXX', 'YYYYABCDXX', 'DCBAZZZZZZ'] # 2
# word = 'XYZ'
# n = 1
# n_list = ['ZAAAAAAAXY'] # 1
# word = 'PQR'
# n = 3
# n_list = ['PQRAAAAPQR', 'BBPQRBBBBB', 'CCCCCCCCCC'] # 2

res = 0
for i in n_list:
    temp = i + i

    if word in temp:
        res += 1

print(res)
