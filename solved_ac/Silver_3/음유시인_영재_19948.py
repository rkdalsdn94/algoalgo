# 백준 - 음유시인 영재 - 실버3 - 19948 - 구현, 문자열 문제
'''
구현, 문자열 문제

나중에 다시 풀어보자 아래와 같이 풀면 될거 같다.
마지막에 제목으로 입력되는 값도 인덱스에서 빼줘야된다. 그거만 신경써서 풀면 될거 같다.

> 시의 '내용'과 '제목'을 모두 기록할 수 있다면 시의 제목을 출력하고, 만약 키보드의 수명이 다 하여 기록을 완벽하게 못 하게 된다면 -1을 출력하여라. <
위에 있는 요구사항을 잘 분석 후 구현하면 된다. 크게 어렵지 않다.

현재 푼 풀이는 res라는 이름으로 시의 앞 글자를 다 담고 시작한다.
 - 위에 나와 있듯이 '내용'과 '제목' 모두 기록할 수 있어야 가능하기 때문에 미리 앞 글자를 다 담아놓아야 된다.
그 다음 연속된 글자는 키 입력을 연속으로 하는 것이니까 temp로 연속된 글자인지 체크한다.
마지막으로 스페이스 바인지 체크, 해당 글자가 음수로 떨어지는지 체크한 다음
 - 다 통과할 수 있다면 res의 글자를 upper() 메서드로 대문자로 바꾼 후 출력하면 된다.
'''

poem = input()
space_bar_cnt = int(input())
char_cnt = list(map(int, input().split()))

# 테스트
# poem = 'There is no cow level'
# space_bar_cnt = 5
# char_cnt = [ 1, 0, 2, 0, 4, 3, 0, 1, 2, 0, 0, 3, 0, 2, 2, 0, 4, 1, 1, 2, 0, 1, 1, 0, 0, 0 ] # TINCL
# poem = 'Show me the money'
# space_bar_cnt = 2
# char_cnt = [ 0, 1, 0, 4, 3, 0, 0, 2, 0, 0, 0, 0, 4, 1, 2, 0, 0, 0, 1, 2, 0, 0, 1, 0, 1, 2 ] # -1
# poem = 'show me the money'
# space_bar_cnt = 4
# char_cnt = [ 1, 0, 3, 2, 1, 0, 0, 2, 0, 0, 0, 0, 4, 1, 2, 0, 0, 0, 1, 2, 0, 0, 1, 0, 1, 0 ] # -1

res = ''.join([ i[0] for i in poem.split() ])
temp = ''

for i in [poem, res]:
    for j in i:
        if temp == j:
            continue
        elif j == ' ':
            temp = j
            space_bar_cnt -= 1
            continue
        elif j.isalpha():
            temp = j
            char_cnt[ord(j.upper()) % 65] -= 1
        if char_cnt[ord(j.upper()) % 65] < 0 or space_bar_cnt < 0:
            print(-1)
            exit(0)
print(res.upper())
