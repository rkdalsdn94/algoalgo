# 백준 - 실버3 - 카드 문자열 - 13417 - 그리디, 정렬, 자료 구조(덱) 문제
'''
그리디, 정렬, 자료 구조(덱) 문제

처음엔 정렬하고 출력하면 되는줄 알았는데, 예제2 번을 보니 단순 정렬 문제가 아니였다.
그래서 문제를 다시 살펴보니 입력으로 주어진 값을 변경하면 안되고, 제일 왼쪽에 있는 값으로 다음 값들을 하나씩 비교하는 방식이였다.

풀이 과정
1. input 값들을 잘 입력 받은 후, 출력할 때 사용한 res를 deque 자료 구조로 만든다.
2. res에 input으로 들어온 문자 중 첫 번째 글자를 담는다.
3. 첫 번째 글자는 temp에 담은 후, 첫 번째 글자를 제외한 n_list에서 다음 글자들을 하나씩 꺼내보면서 res[0] 번째 담긴 글자와 비교한다.
    3.1. temp(res[0])의 값이 n_list의 값보다 작으면 res의 제일 끝에 append
    3.2. temp(res[0])의 값이 n_list의 값보다 크거나 같으면 res의 제일 왼쪽에 append 한다.
4. res를 문자열로 합치고 출력한다.
'''

from collections import deque

t = int(input())
for _ in range(t):
    _ = int(input())
    n_list = list(input().split())
    res = deque( [n_list[0]] )

    for i in n_list[1:]:
        temp = res[0]

        if temp >= i:
            res.appendleft(i)
        else:
            res.append(i)

    print(''.join(res))