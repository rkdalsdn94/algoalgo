# 백준 - 실버5 - 귀걸이 - 1380 - 구현, 문자열 문제
'''
구한, 문자열 문제

풀이 과정
 - 귀걸이에 대한 정보(압수당했거나, 돌려줬거나)에서 뒤의 문자는 중요하지 않다.
 - 즉, 입력 받을 때 앞의 숫자만 earring_list에 적어놓고, 정렬을 한다.
 - 0부터 earing_list의 길이 - 1 까지 step을 2로 둔 상태로 for 문을 돈다.
    - for 문 내에서 현재 반복중인 i가 earring_list의 마지막 이거나, 이 전의 값이 같은 숫자가 아니라면
      되돌려받지 못한 상황이므로, cnt와 해당 숫자에서 1을 뺀 값으로 n_list의 값을 출력하면 된다.
 - 다음 반복을 위해 cnt를 1씩 증가 시킨다.
 - 입력의 종료가 언제 될 지 모르므로 try except 문을 사용해서 구현했다.

in
    3
    Betty Boolean
    Alison Addaway
    Carrie Carryon
    1 B
    2 A
    3 B
    3 A
    1 A
    2
    Helen Clark
    Margaret Thatcher
    1 B
    2 B
    2 A
    0

out
    1 Alison Addaway
    2 Helen Clark
'''

cnt = 1

while 1:
    try:
        n = int(input())
        n_list = [input() for _ in range(n)]
        earring_list = sorted([int(list(input().split())[0]) for _ in range(2 * n - 1)])

        for i in range(0, len(earring_list), 2):
            if i == len(earring_list) - 1 or earring_list[i] != earring_list[i + 1]:
                print(cnt, n_list[earring_list[i] - 1])
                break
        cnt += 1
    except:
        break
