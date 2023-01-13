# 백준 - 실버2 - 크로스워드 퍼즐 쳐다보기 - 3005 - 구현, 문자열, 파싱 문제
'''
구현, 문자열, 파싱 문제

다른 사람 풀이를 보니까 '#'을 기준으로 슬라이스를 진행한 후에 푼거 같은데, 나는 뭔가 생각나는대로 풀었다.
세로줄과 가로줄 검사를 따로 하고, 각각 2중 반복문을 돌면서 '#'을 검사한다.
 - '#'이 아니면 temp에 추가하다가 한 줄에 대한 반복문이 끝나면 temp의 길이가 2보다 크거나 같으면 res에 추가한다.
 - '#'이 맞으면 이 전에 글자들의 길이(temp의 len)가 2를 넘거나 같으면 res에 추가 후 temp를 빈 문자열로 바꾼다.
위 방법으로 진행한 후 res에 가장 길이가 짧은걸 출력하면 된다.
'''

r, c = map(int, input().split())
word_list = [ input() for _ in range(r) ]

# 테스트
# r, c = 4, 4
# word_list = [ 'luka', 'o#a#', 'kula', 'i#a#' ] # kala
# r, c = 4, 4
# word_list = [ 'luka', 'o#a#', 'kula', 'i#as' ] # as
# r, c = 4, 5
# word_list = [ 'adaca', 'da##b', 'abb#b', 'abbac' ] # abb

res = []

# 가로줄 검사
for i in range(r):
    temp = ''

    for j in word_list[i]:
        if j != '#':
            temp += j
        else:
            if len(temp) >= 2:
                res.append(temp)
            else:
                temp = ''
    if len(temp) >= 2:
        res.append(temp)

# 세로줄 검사
for i in range(c):
    temp = ''

    for j in range(r):
        if word_list[j][i] != '#':
            temp += word_list[j][i]
        else:
            if len(temp) >= 2:
                res.append(temp)
            else:
                temp = ''
    if len(temp) >= 2:
        res.append(temp)

print(sorted(res)[0])
