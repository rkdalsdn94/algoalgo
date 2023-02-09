# 백준 - 브론즈2 - 노래 악보 - 1392 - 단순 구현 문제
'''
단순 구현 문제

n과 q의 각각 최대 100, 1000 이므로 시간 초과는 크게 걱정하지 않아도 풀리는 문제이다.
문제를 보면서 아래 코드를
https://pythontutor.com/visualize.html#mode=edit 여기 사이트에서 한 번씩 실행시켜보면 이해가 바로 된다.

풀이를 간단하게 적어보면
악보(n)만큼 반복하면서 해당 악보의 인덱스 값(n_list[i])만큼 temp를 통해 res를 append 한다.
두 번째 반복문이 끝나면 다음 악보로 넘어간 것이므로 temp에 1을 더해준다.
res에 전체 악보를 노래하는 시간을 구했으므로 q_list를 돌면서 해당 번째 인덱스를 출력하면 된다.
'''

n, q = map(int, input().split())
n_list = [ int(input()) for _ in range(n) ]
q_list = [ int(input()) for _ in range(q) ]

# 테스트
# n, q = 3, 5
# n_list = [2, 1, 3]
# q_list = [2,3,4,0,1] # 2  \  3  \  3  \  1  \  1

res = []
temp = 1

for i in range(n):
    for _ in range(n_list[i]):
        res.append(temp)
    temp += 1

for i in q_list:
    print(res[i])
