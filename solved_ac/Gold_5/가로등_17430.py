# 백준 - 골드5 - 가로등 - 17430 - 자료 구조(해시) 문제
'''
자료 구조(해시) 문제

풀이 과정
    - 테스트 케이스(t) 만큼 입력을 받으면서 다음의 과정을 계산한다.
    - 가로등의 개수(n)를 입력받고, 가로등의 위치(num_li)를 입력받는다.
    - num_li를 정렬한다.
    - idx를 n - 1로 초기화한다.
    - num_li의 길이만큼 반복하면서 다음의 과정을 계산한다.
        - num_li[i][0]과 num_li[i + 1][0]이 같지 않다면, idx를 i로 변경한다.
    - one_unit에 num_li[i][1]을 저장한다.
    - k에 one_unit의 길이를 저장한다.
    - idx + 1부터 n까지 반복하면서 다음의 과정을 계산한다.
        - num_li[i][1]과 one_unit[i % k]이 같지 않다면, NOT BALANCED를 출력하고 반복문을 종료한다.
    - 반복문이 종료되면, BALANCED를 출력한다.

in
    2
    6
    2 3
    2 -3
    2 1
    -2 3
    -2 1
    -2 -3
    6
    2 4
    2 -3
    2 1
    -2 3
    -2 1
    -2 -3
out
    BALANCED
    NOT BALANCED
'''

t = int(input())
for _ in range(t):
    n = int(input())
    num_li = sorted(tuple(map(int, input().rstrip().split())) for _ in range(n))
    idx = n - 1

    for i in range(n - 1):
        if num_li[i][0] != num_li[i + 1][0]:
            idx = i
            break

    one_unit = [num_li[i][1] for i in range(idx + 1)]
    k = len(one_unit)

    for i in range(idx + 1, n):
        if num_li[i][1] != one_unit[i % k]:
            print('NOT BALANCED')
            break
    else:
        print('BALANCED')
