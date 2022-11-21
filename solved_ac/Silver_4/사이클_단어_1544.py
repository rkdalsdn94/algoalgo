# 백준 - 사이클 단어 - 실버4 - 1544 - 구현, 자료 구조(deque), 문자열, 완전 탐색, 집합 문제
'''
구현, 자료 구조(deque), 문자열, 완전 탐색, 집합 문제

입력으로 들어온 각각의 단어마다 한 글자씩 바꿔보면서 입력 리스트에 같은 글자가 있는지 확인하면 된다.

풀이 과정
1. n과 n_list라는 변수명으로 입력 조건에 따라 값을 잘 입력 받는다. -> n은 숫자, n_list는 문자열 리스트
2. for 반복문을 n 만큼 실행하면서 아래의 과정을 수행한다.
    2.1 현재 반복중인 문자열을 q에 넣고, 비교를 위해 temp라는 빈 문자열 변수를 만든다.
    2.2 temp 변수가 현재 반복중인 문자열(n_list[i])과 같아질 때까지 while 반복문을 실행한다. -> temp != n_list[i]
        2.2.1 q에 있는 단어를 앞에 있는 글자를 꺼내 뒤로 옮겨준다. -> q.append(q.popleft())
        2.2.2 temp로 정했던 변수에 한 글자씩 옮긴 글자를 담는다.
        2.2.3 temp 단어가 입력으로 들어온 단어에 있다면 n_list의 해당 글자를 원본 단어로 바꿔준다.
3. n_list를 set 탑으로 형변환을 진행한 후 해당 길이를 출력하면 된다.
'''

from collections import deque

n = int(input())
n_list = [ input() for _ in range(n) ]

# 테스트
# n = 5
# n_list = [ 'picture', 'turepic', 'icturep', 'word', 'ordw' ] # 2
# n = 7
# n_list = ['ast', 'ats', 'tas', 'tsa', 'sat', 'sta', 'ttt'] # 3
# n = 5
# n_list = [ 'aaaa', 'aaa', 'aa', 'aaaa', 'aaaaa' ] # 4

for i in range(n):
    q = deque(n_list[i])
    temp = ''

    while temp != n_list[i]:
        q.append(q.popleft())
        temp = ''.join(q)

        if temp in n_list:
            n_list[n_list.index(temp)] = n_list[i]


res = set(n_list)
print(len(res))
