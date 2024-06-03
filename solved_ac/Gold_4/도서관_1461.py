# 백준 - 골드4 - 도서관 - 1461 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

풀이 과정
 1. 음수와 양수를 나누어서 정렬한다.
 2. 음수와 양수를 m개씩 묶어서 거리를 계산한다.
 3. 거리를 정렬하고, 가장 먼 거리를 빼고, 2배를 더한다.
 4. 결과를 출력한다.
'''

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, m = 7, 2
# n_list = [-37, 2, -6, -39, -29, 11, -28] # 131
# n, m = 8, 3
# n_list = [-18, -9, -4, 50, 22, -26, 40, -45] # 158
# n, m = 6, 2
# n_list = [3, 4, 5, 6, 11, -1], # 29
# n, m = 1, 50
# n_list = [1] # 1

plus = []
minus = []

for i in n_list:
    if i > 0:
        plus.append(i)
    else:
        minus.append(i)

distance = []
minus.sort()
plus.sort(reverse=True)

for i in range(len(minus) // m):
    distance.append(abs(minus[i * m]))
if len(minus) % m != 0:
    distance.append(abs(minus[len(minus) - len(minus) % m]))

for i in range(len(plus) // m):
    distance.append(plus[i * m])
if len(plus) % m != 0:
    distance.append(plus[len(plus) - len(plus) % m])

distance.sort()
res = distance.pop() + (2 * sum(distance)) # 마지막에 pop을 해주는 이유는 마지막 위치는 0으로 안 돌아와도 되기 때문이다.
print(res)
