# 백준 - 브론즈1 - 제자리 - 25400 - 단순 그리디 문제
'''
단순 그리디 문제

입력받은 리스트가 1 부터 오름차 순으로 증가할 때 까지 몇 번 pop해야 되는지 계산하면 된다.
처음에 부분 성공으로 나와서 왜 그렇지 하고 생각해보니까 list에서 pop(0) 가 시간이 많이 걸려서 그런가 싶어
deque을 사용하니까 괜찮아졌다. 제일 아래 부분 성공 코드에서 deque을 활용하면 된다.

1. input 값들을 잘 입력 받는다. -> n과 n_list
2. while 반복문으로 입력받은 n_list에서 처음 값을 꺼내서 1로 초기화된 temp와 값이 같은지 비교한다.
    2.1. 다를때마다 res를 1씩 증가시킨다.
    2.2. 같으면 temp에 1을 더하고 새로운 값을 꺼내 다시 비교한다.
3. res를 출력한다.
'''

from collections import deque

n = int(input())
n_list = deque(list(map(int, input().split())))

# 테스트
# n = 1
# n_list = [1]
# n = 8
# n_list = [6, 1, 2, 3, 2, 4, 5, 10] # 3
# n = 6
# n_list = [3, 4, 6, 10, 2, 5] # 6

res = 0
temp = 1

while n_list:
    n_list_num = n_list.popleft()

    if temp != n_list_num:
        res += 1
    else:
        temp += 1

print(res)


'''
부분 성공 코드

n = int(input())
n_list = list(map(int, input().split()))
res = 0
temp = 1

while n_list:
    n_list_num = n_list.pop(0)

    if temp != n_list_num:
        res += 1
    else:
        temp += 1

print(res)

'''
