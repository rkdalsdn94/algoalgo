# 백준 - 김식당 - 14612 - 실버4 - 구현, 정렬, 시뮬레이션 문제
'''
구현, 정렬, 시뮬레이션 문제

입력받은 조건에 따라 잘 구현하면 된다. 크게 어렵진 않은 문제이다.

풀이 과정
1. n, m을 입력 받고, order_list 라는 이름으로 정렬과 입력 과정에 따라 수행할 빈 리스트를 만든다.

2. n만큼 반복하면서 a라는 이름으로 input을 리스트 형식으로 입력 받는다.
    2.1. a의 0번째 인덱스가 order면
        2.1.1. a를 a, b, c 로 쪼갠 후 b와 c를 int형으로 바꾼다.
        2.1.2. b와 c를 단순 정렬을 하기 위해 [c, b] 이런 식으로 order_list에 append 한다.
    2.2. a의 0번째 인덱스가 sort면
        2.2.1. order_list를 정렬한다. -> c를 먼저 추가한 상태라 입력받아서 단순 정렬만 한다.
    2.3. a의 0번째 인덱스가 complete 면
        2.3.1. d, x로 a를 쪼갠 후 x를 int형으로 형변환을 진행한다.
        2.3.2. order_list의 길이만큼 반복하면서 반복중인 order_list의 1번째 인덱스의 값이 x와 같으면
                idx라는 이름으로 현재 반복중인 값인 i를 담고, 해당 idx를 order_list에서 pop한 후 종료한다

3. n만큼 반복하는 반복문 안에서 반복문마다 초기화 하면서 정답으로 출력할 res 리스트를 만든다
    3.1. order_list가 있다면
        3.1.1. order_list 만큼 반복하면서, res에 1번째 인덱스를 추가한다.
        3.1.2. res를 출력한다.
    3.2. order_list가 없다면
        3.2.1. 'sleep'를 출력한다.

in
    7 3
    order 1 4
    order 2 2
    order 3 3
    sort
    complete 3
    complete 2
    complete 1
out
    1
    1 2
    1 2 3
    2 3 1
    2 1
    1
    sleep
'''

n, m = map(int, input().split())
order_list = []

for _ in range(n):
    a = list(input().split())

    if 'order' in a:
        a, b, c = a
        b, c = int(b), int(c)
        order_list.append([c, b])
    elif 'sort' in a:
        order_list.sort()
    elif 'complete' in a:
        d, x = a
        x = int(x)

        for i in range(len(order_list)):
            if order_list[i][1] == x:
                idx = i
                order_list.pop(idx)
                break
    res = []
    if order_list:
        for i in order_list:
            res.append(i[1])
        print(*res)
    else:
        print('sleep')
