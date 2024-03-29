# 백준 - 실버2 - 아이들과 선물 상자 - 23757 - 자료 구조(우선순위 큐) 문제
'''
자료 구조(우선순위 큐) 문제

선물의 개수 : c_list
아이들이 원하는 선물의 개수 : w_list

아이들이 원하는 선물의 개수를 얻지 못할 경우 0을 출력하고
아이들이 원하는 선물의 개수를 얻을 수 있는 경우 1을 출력한다.

풀이 과정
 - heapq의 heapify를 이용해서 선물의 개수를 heap으로 만든다.
    - heap으로 만들 때 선물의 개수를 음수로 바꿔서 만들어야 된다. (python은 min heap만 지원하기 때문)
 - 아이들이 원하는 선물의 개수를 하나씩 빼서 선물의 개수와 뺀 선물의 개수를 다시 heap으로 만든다.
    - 이때 아이들이 원하는 선물의 개수와 가지고 있는 선물의 개수의 차가 0보다 작아진다면 0을 출력하고 종료한다.
 - 프로그램이 종료되지 않으면 아이들이 모두 원하는 선물의 개수를 가진것이다. 즉, 1을 출력하면 된다.
'''

import heapq as hq

n, m = map(int, input().split())
c_list = list(map(int, input().split()))
w_list = list(map(int, input().split()))

# 테스트
# n, m = 4, 4
# c_list = [4, 3, 2, 1]
# w_list = [3, 1, 2, 1] # 1
# n, m = 4, 3
# c_list = [4, 3, 2, 1]
# w_list = [3, 1, 5] # 0

c_list = [-i for i in c_list]
hq.heapify(c_list)

for i in w_list:
    temp = -hq.heappop(c_list)

    if temp - i < 0: # 선물을 다 못 주는 경우
        print(0)
        exit(0)

    hq.heappush(c_list, -(temp - i))

print(1)
