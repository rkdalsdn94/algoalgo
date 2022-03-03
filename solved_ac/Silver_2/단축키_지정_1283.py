'''
문자열, 구현 문제이다.
주어진 조건대로 차근차근 풀면 된다.
근데 ck로 들어와 있는지 체크를 할때 upper를 하지 않아서 몇 번 틀렸었다.
'''

n = int(input())
n_list = [ input() for _ in range(n) ]
# print(n, n_list)

# 테스트
# n, n_list = 5, ['New', 'Open', 'Save', 'Save As', 'Save All']
# out: [N]ew \n [O]pen \n [S]ave \n Save [A]s \n Sa[v]e All
# n, n_list = 8, ['New window', 'New file', 'Copy', 'Undo', 'format', 'Font', 'Cut', 'Paste']
# out: [N]ew window \n New [f]ile \n [C]opy \n [U]ndo \n F[o]rmat \n Fon[t] \n Cut \n [P]aste \n

res = []
ck = []

for word in n_list:
    word_split = word.split()
    flag = True
    word_temp = ''

    for i in word_split:
        if i[0].upper() not in ck and flag:
            ck.append(i[0].upper())
            word_temp += '[' + i[0] + ']' + i[1:]
            flag = False
        else:
            word_temp += i
        word_temp += ' '

    if flag:
        for i, j in enumerate(word):
            if j.upper() not in ck and j != ' ':
                word_temp = word[:i] + '[' + word[i] +']' + word[i+1:]
                ck.append(j.upper())
                break

    res.append(word_temp)

print(*res, sep='\n')

