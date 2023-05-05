# 백준 - 실버5 - 가지 산사태 - 27940 - 그리디, 애드 훅 문제
'''
그리디, 애드 훅 문제

처음에 맞게 짠거 같은데 왜 안되지 하면서 1시간 가량 고민을 했었다. (해당 코드는 제일 아래 있다.)
근데, 정답을 제출했을 때 '틀렸습니다.'가 아니라 '시간 초과'가 나와서 풀이 방식이 잘못된거 같아 문제를 다시 보다가 아래 조건을 보고 방법이 생각났다.
 - i번째 비가 온 직후 처음으로 무너지는 층이 발생할 때, 첫째 줄에 i와 '무너지는 층을 아무거나 하나' 출력한다.
'무너지는 층을 아무거나 하나'가 핵심이였다.

처음 코드는 t, r 들어올 떄 1 ~ t 까지 r을 더해서 무너지는 층이 생기는지 검사하는 방식으로 풀었었다.
단순하게 반복문의 시간 복잡도만 생각해도 최악의 경우 O(m^n)이 걸린다. (n과 m의 범위가 10 ^ 6 안에 값이 1 ~ n 까지 최악의 경우로 들어왔을 때)
 - max() 함수까지 계산하면 더 느려진다.

상술한 코드를 문제를 잘 이해하고 해석하면 어떤 층이 무너지면 '1층은 반드시 무너지게 된다' 라는 결론이 나온다.
 - (1층부터 t_i층이 동시에 빗물을 각각 r_i만큼 받게 된다.)
따라서, 빗물의 양을 기록할 temp로 r을 더하면서 해당 temp가 k가 넘어가는지만 검사하면 된다.

시간을 더 줄이고 싶으면 m_list를 미리 입력 받지 말고, m만큼 반복하면서 temp에 값을 추가하고 k보다 큰지 작은지 검사하면 좀 더 빠르다.

n : 농장의 층수
m : 비가 오는 횟수
k : 버틸 수 있는 빗물의 양
m_list : m개의 줄에 걸쳐 비의 정보를 나타내는 정수 t, r
'''

import sys; input=sys.stdin.readline

n, m, k = map(int, input().split())
m_list = [ list(map(int, input().split())) for _ in range(m) ]

# 테스트
# n, m, k = 5, 4, 5
# m_list = [ [3,3], [2,2], [5,1], [2,3] ] # 3 2  --> 3 1
# n, m, k = 5, 4, 8
# m_list = [ [2,2], [1,1], [4,3], [5,2] ] # -1   --> -1
# n, m, k = 10, 3, 10
# m_list = [ [3,1], [4,20], [1,2] ] # 2 3        --> 2 1

temp = 0

for cnt, i in enumerate(m_list):
    t, r = i
    temp += r

    if temp > k:
        print(cnt + 1, 1)
        exit(0)
print(-1)


# 실패 코드
'''
n, m, k = map(int, input().split())
m_list = [ list(map(int, input().split())) for _ in range(m) ]
temp = [0] * (n + 1)
flag = False
cnt = 1

for t, r in m_list:
    for i in range(1, t + 1):
        temp[i] += r

    if max(temp) > k:
        res = temp.index(max(temp))
        flag = True
        break
    cnt += 1

if flag:
    print(cnt, res)
else:
    print(-1)
'''
