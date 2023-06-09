# 백준 - 실버1 - 쿼드 트리 - 1992 - 분할 정복, 재귀 문제
'''
분할 정복, 재귀 문제

전에 풀었던 '백준 - 종이의 개수(1720)' 문제에서 풀이를 조금 참고하고 해당 문제를 풀었다.
해당 문제 파일에 있는 '프로그래머스 - 쿼드압축 후 개수 세기' 문제도 내일까지 풀어보려고 한다.

이 문제의 풀이는 종이의 개수 'Silver_2/종이의_개수_1780.py' 여기 파일에서 보면 된다.

반복문 도중 board와 temp가 다를 때 res에 '('를 추가하고, new_n으로 나눈 재귀를 통과한 뒤 ')' 괄호를 닫아준다.
그리고 반복문이 끝났을 시점에서 temp를 res에 추가하면 된다.
'''

n = int(input())
board = [ input() for _ in range(n) ]

# 테스트
# n = 8
# board = [ 
#     '11110000',
#     '11110000',
#     '00011100',
#     '00011100',
#     '11110000',
#     '11110000',
#     '11110011',
#     '11110011'
# ] # ((110(0101))(0010)1(0001))

res = ''

def recursive(x, y, n):
    global res
    temp = board[x][y]
    new_n = n // 2 # n 의 범위를 절반씩 줄이기 위한 new_n 변수

    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != temp:
                res += '('

                recursive(x, y, new_n)
                recursive(x, y + new_n, new_n)
                recursive(x + new_n, y, new_n)
                recursive(x + new_n, y + new_n, new_n)

                res += ')'
                return
    res += temp # 반복문이 끝나면 숫자가 모두 같은 숫자이므로 temp를 res에 추가한다.

recursive(0, 0, n)
print(res)
