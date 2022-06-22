'''
구현, 문자열, 그리디 문제

처음에 문제를 어떻게 풀어야 될지 고민을 많이 했다..
안될거 알지만 그래도 혹시나 하는 마음으로 완전 탐색으로 풀었다가 역시나 시간 초과가 나왔다..
그러다 다른 사람의 코드는 안보고 풀이를 참고했을 때 반대로 접근하면 된다고 해서
그리디하게 풀었다. 끝글자가 'A'면 pop 'B'면 pop후 reverse 방식으로 풀었다.

다음에 다른 문제들을 풀때, 뒤에서 접근하는 것도 놓치면 안될거 같다.
'''

s, t = list(input()), list(input())

# 테스트
# s, t = list('B'), list('ABBA') # 1
# s, t = list('AB'), list('ABB') # 0

flag = False

while len(t) != len(s):
    if t[-1] == 'A':
        t.pop(-1)
    elif t[-1] == 'B':
        t.pop(-1)
        t.reverse()
    
    if s == t:
        flag = True
        break


if flag: print(1)
else: print(0)
