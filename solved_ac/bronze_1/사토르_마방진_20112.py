# 백준 - 브론즈1 - 사토르 마방진 - 20112 - 구현, 문자열 문제
'''
구현, 문자열 문제

ck 변수를 n * n의 범위로 만든 후 입력받은 문자열의 세로 부분(열)을 가로(행) 담는다. (2중 for 문을 통해)
그리고 ck와 입력받은 문자(word)를 같은지 비교한 뒤, 같다면 'YES', 다르면 'NO'를 출력하면 된다.

문제를 다 풀고 다른 사람들은 어떻게 풀었을 지 보다가 좋은 코드가 있어 가져왔다.
zip 함수를 활용해서 세로줄을 가로줄로 만들어 비교한다.
해당 코드는 제일 아래 줄에 있다.
'''

n = int(input())
word = [list(input()) for _ in range(n)]

# 테스트
# n = 3
# word = [list('AAB'), list('ACD'), list('BDE')] # YES
# n = 4
# word = [list('APPL'), list('PPAP'), list('PADD'), list('LPOV')] # NO

ck = [[0] * n for _ in range(n)]
for i in range(n): # 입력받은 문자를 가로로 읽으면서 ck 변수에는 세로로 담는다.
    for j in range(n):
        ck[j][i] = word[i][j]

if word == ck:
    print('YES')
else:
    print('NO')

'''
도움이 됐던 다른 사람(deight8311 - 백준 아이디)의 코드 (약간 수정함)

n = int(input())
word = [list(input()) for _ in range(n)]
zip_word = list(zip(*word))

for i in range(n):
    if word[i] != list(zip_word[i]):
        print('NO')
        exit(0)
print('YES')
'''
