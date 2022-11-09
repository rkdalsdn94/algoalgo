# 백준 - 실버1 - 시간 관리 - 1263 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

이 문제를 풀 때 제일 아래 같은 방식처럼 문제를 풀고 싶었는데, 해결이 잘 안돼서 방식을 수정했다.
    - 문제를 다 푼 후 다른 사람 코드의 풀이 중 시간이 제일 짧은 코드와 비슷하게 접근하려다가 실패했었다.
    - 대략적인 방식은 비슷한데 통과했던 분의 코드는 s를 역순으로 정렬한 후 제일 오래 걸리는 시간을 기준으로 빼는 방식으로 선택했다.
    - 아마 나는 abs() 함수를 통해 n_list에서 빼는 방식을 절대값으로 계산하려고 했는데, 해당 부분에서 오류가 있었던거 같다.
    - 해당 코드를 참고해서 성공 코드라는 다시 구현해봤다.

풀이 과정
1. 입력받은 명단 중 끝내야 될 시간(s)을 기준으로 정렬을 한다.
2. 모든 n_list를 temp 변수에 t(i)시간을 더하면서 끝내야 되는 시간 s(j)를 넘지 않는지 확인한다.
    2.1 전체 일정을 진행한 후 temp가 s를 넘지 않는다면 res를 1 더해주고 다시 시도해본다. -> 1시간 늦게 잔 후 상황도 다시 살펴봐야 된다.
    2.2 위 과정중 s를 넘긴다면 반복문을 종료하고 res - 1 한 상태로 출력한다. -> 1시간 늦게 일어난 상황중에 실패했으므로 1시간 늦게잔 것을 빼야된다.
3. res를 출력한다.
'''

n = int(input())
n_list = sorted([ list(map(int, input().split())) for _ in range(n) ], key=lambda x: (x[1], x[0]))

# 테스트
# n = 4
# n_list = sorted([[3,5],[8,14],[5,20],[1,16]], key=lambda x: (x[1], x[0])) # 2
# n = 4
# n_list = sorted([[3,4],[1,4],[5,17],[2,20]], key=lambda x: (x[1], x[0])) # 0

res = 0
flag = False

while 1:
    temp = res

    for i, j in n_list:
        if temp + i <= j:
            temp += i
        else:
            flag = True
            break
    if flag:
        break
    res += 1

print(res - 1)

'''
실패 코드

n = int(input())
n_list = sorted([ list(map(int, input().split())) for _ in range(n) ], key=lambda x: (x[1], x[0]))
res = abs(n_list[0][0] - n_list[0][1])
temp = n_list[0][0]

for i in range(1, n):
    if n_list[i][1] != n_list[i - 1][1]:
        break
    temp += n_list[i][0]
    res = min(res, abs(temp - n_list[i][1]))

print(res)
'''
###############################################################
'''
성공 코드

n = int(input())
n_list = sorted([ list(map(int, input().split())) for _ in range(n) ], key=lambda x: -x[1])

res = n_list[0][1] - n_list[0][0]

for i in range(1, n):
    if res > n_list[i][1]:
        res = n_list[i][1] - n_list[i][0]
    else:
        res -= n_list[i][0]

if res >= 0:
    print(res)
else:
    print(-1)

'''
