'''
구현, 문자열, 투 포인터 문제

left, right 변수로 각 단어의 시작과 끝을 돌면서
중간에 return하는 부분이 없으면 원래 단어가 회문이므로 0을 return한다.
중간에 다른 부분이 나오면 왼쪽, 오른쪽에 있는 한 글자 뺀 뒤에(temp) 원래 글자(word)랑 같은지 검사한다.
이때 한 글자 빼고 word랑 temp랑 같으면 1 리턴 다르면 2를 리턴 한다.

2023년 2월 7일
17609번 - 회문 문제가 재채점 되었습니다.  (재채점 이유: 데이터 추가) 14:59
백준에서 재채점 되었을 때 틀려서 '왜 그렇지?' 하고 질문 게시판을 확인해보니 아래와 같이 입력이 들어올 때 문제가 발생했다.
in
    1
    abca
out
    1 --> 나의 원래 코드에선 2가 나왔다.

위에 있는 데이터를 가지고 디버깅을 해보니, left < right -1 여기와 left + 1 < right 부분이 문제였다.
위 조건에서 작거나 같을 때 즉, '='를 추가하니까 통과한다. (전에는 왜 생각을 못했지...?)

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
            if left <= right - 1:
                temp = word[:right] + word[right + 1:]
                if temp == temp[::-1]:
                    return 1
            if left + 1 <= right:
                temp = word[:left] + word[left + 1:]
                if temp == temp[::-1]:
                    return 1
            return 2
    return 0

for _ in range(t):
    word = input()
    res = palindrome_ck(word)
    print(res)