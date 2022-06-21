'''
구현, 문자열, 투 포인터 문제

left, right 변수로 각 단어의 시작과 끝을 돌면서
중간에 return하는 부분이 없으면 원래 단어가 회문이므로 0을 return한다.
중간에 다른 부분이 나오면 왼쪽, 오른쪽에 있는 한 글자 뺀 뒤에(temp) 원래 글자(word)랑 같은지 검사한다.
이때 한 글자 빼고 word랑 temp랑 같으면 1 리턴 다르면 2를 리턴 한다.

in
    7
    abba
    summuus
    xabba
    xabbay
    comcom
    comwwmoc
    comwwtmoc
out
    0
    1
    1
    2
    2
    0
    1
'''

t = int(input())

def palindrome_ck(word):
    left, right = 0, len(word) - 1

    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            if left < right - 1:
                temp = word[:right] + word[right + 1:]
                if temp == temp[::-1]:
                    return 1
            if left + 1 < right:
                temp = word[:left] + word[left + 1:]
                if temp == temp[::-1]:
                    return 1
            return 2
    return 0

for _ in range(t):
    word = input()
    res = palindrome_ck(word)
    print(res)