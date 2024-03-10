# 백준 - 실버3 - queuestack - 24511 - 자료 구조(스택, 덱, 큐) 문제
'''
자료 구조(스택, 덱, 큐) 문제

a_list의 값 중
 - 0이면 큐, 1이면 스택
 - 큐일 경우만 고려하면 된다. (스택은 원소를 삽입하고 바로 빼냄 즉, 의미가 없다.)
 - 스택의 경우도 고려하려면 2중 for 문이 생기는데, 이때 시간 초과가 발생한다.

풀이 과정
 - a_list의 값을 보면서 해당 인자가 큐(0)인지 스택(1)인지 구별한 뒤, 큐일 때만 res 덱에 append 한다. (이때 appendleft로 해야 됨)
    - 스택이 들어오면 사실 의미가 없다. (원소를 삽입한 뒤 바로 빼야 됨)
 - 그 후 res가 비어 있으면 입력받은 c_list를 그대로 출력한다.
 - res(큐)가 비어있지 않다면 큐 이후의 c_list를 추가한다. (extend 함수를 이용)
 - 마지막으로 res를 출력하는데 deque은 list slice를 사용할 수 없으므로 list로 형변환 후 슬라이싱을 이용해 0부터 m까지를 출력하면 된다.
'''

from collections import deque

n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
m = int(input())
c_list = list(map(int, input().split()))

# 테스트
# n = 4
# a_list = [0, 1, 1, 0]
# b_list = [1, 2, 3, 4]
# m = 3
# c_list = [2, 4, 7] # 4 1 2
# n = 5
# a_list = [1, 1, 1, 1, 1]
# b_list = [1, 2, 3, 4, 5]
# m = 3
# c_list = [1, 3, 5] # 1 3 5

res = deque()
for i in range(n):
    if a_list[i] == 0: # a_list에서 큐만 뽑는 과정
        res.appendleft(b_list[i])

if not res: # q가 비어있으면 c_list 출력
    print(*c_list)
    exit(0)

res.extend(c_list) # q에서 c_list 초기 상태 append
print(*list(res)[:m])
