# 백준 - 실버5 - 진짜 메시지 - 9324 - 구현, 문자열, 파싱 문제
'''
구현, 문자열, 파싱 문제

입력받은 문자열을 완전 탐색으로 검사하면 된다.

모두 대문자로 들어오기 때문에 word_list 를 26 크기로 배열을 만든다.
입력받은 글자를 한 글자씩 보면서, 해당 글자와 같은 글자가 해당 글자의 수가 3이 됐을 때, (word_list로 확인한다.)
그 글자가 마지막 글자이거나, 다음 글자와 다르다면 FAKE 이다.
위의 경우가 아니라면 가능한 것이므로 OK 를 출력하면 된다.

in
    3
    BAPC
    AABA
    ABCABCBBAAACC
out
    OK
    FAKE
    OK
'''

t = int(input())

for _ in range(t):
    word = input()
    word_list = [ 0 for _ in range(26) ]
    flag = False
    res = 'OK'

    for i in range(len(word)):
        if flag:
            flag = False
            continue

        word_list[ord(word[i]) % 65] += 1
        if word_list[ord(word[i]) % 65] == 3:
            if i == len(word) - 1:
                res = 'FAKE'
                break
            elif word[i] != word[i + 1]:
                res = 'FAKE'
                break
            flag = True
            word_list[ord(word[i]) % 65] = 0

    print(res)
