# 백준 - 실버1 - 볼 모으기 - 17615 - 그리디 문제
'''
그리디 문제

전형적인 그리디 문제이다.

풀이 과정
 - 파란색 볼과 빨간색 볼을 각각 왼쪽, 오른쪽으로 밀어 놓은 뒤 남은 볼의 갯수를 count 하면 된다.
 - 오른쪽으로 미는 방법은 rstip 함수를 통해 오른쪽 글자를 제거한 뒤, 남은 R의 갯수를 세는 방식으로 풀었다.
 - 왼쪽은 위 방법에서 반대로 하면 된다.
 - 또한, 'R'과 'B' 따로따로 count 해야 된다.
'''

n = int(input())
word = input()

# 테스트
# n = 9
# word = 'RBBBRBRRR' # 2
# n = 8
# word = 'BBRBBBBR' # 1

# 우측으로 레드를 모으는 과정
right_r_word = word.rstrip('R')
right_r_cnt = right_r_word.count('R')

# 우측으로 블루를 모으는 과정
right_b_word = word.rstrip('B')
right_b_cnt = right_b_word.count('B')

# 좌측으로 레드를 모으는 과정
left_r_word = word.lstrip('R')
left_r_cnt = left_r_word.count('R')

# 좌측으로 블루를 모으는 과정
left_b_word = word.lstrip('B')
left_b_cnt = left_b_word.count('B')

print(min(right_b_cnt, right_r_cnt, left_b_cnt, left_r_cnt))
