'''
구현, 재귀 문제이다.

단순한 구현, 재귀 문제이다.
n번 재귀가 실행 됐을 때,
"재귀함수는 자기 자신을 호출하는 함수라네" 를 실행한 후에, return을 하면 된다.
'''

n = int(input())
underbar = '____'

def recursive(cnt):
    print(underbar * (n - cnt) + '"재귀함수가 뭔가요?"')

    if cnt == 0:
        print(underbar * (n - cnt) + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(underbar * (n - cnt) + '라고 답변하였지.')
        return
    
    print(underbar * (n - cnt) + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print(underbar * (n - cnt) + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print(underbar * (n - cnt) + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    recursive(cnt - 1)
    print(underbar * (n - cnt) + '라고 답변하였지.')

print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
recursive(n)
