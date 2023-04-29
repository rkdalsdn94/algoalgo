# 백준 - 브론즈1 - 세준세비 - 1524 - 구현, 정렬, 시뮬레이션 문제
'''
구현, 정렬, 시뮬레이션 문제

문제에서 제일 약한 병사가 죽는다고 되어있다. 그래서 완전 탐색 방식으로 입력받은 list들의 원소를 하나하나 비교했었는데, 굳이 그럴필요가 없다.
제일 '약한' 병사를 신경쓰지말고, 제일 '강한' 병사가 어느쪽에 있는지만 검사하면 되는 문제다.
그리고 'C'를 출력하는 부분에서 else문으로 처리했었는데, 애초에 'C'가 출력될 일은 없는 문제라고 한다. (질문 게시판에서 보면 나옴)

in
    2

    1 1
    1
    1

    3 2
    1 3 2
    5 5
out
    S
    B
'''

t = int(input())
for _ in range(t):
    input()
    n, m = map(int, input().split())
    max_s = max(list(map(int, input().split()))) # 세준이의 병사 중 제일 큰 값
    max_b = max(list(map(int, input().split()))) # 세비의 병사 중 제일 큰 값

    if max_s >= max_b:
        print('S')
    elif max_s < max_b:
        print('B')
    else:
        print('C') # 여기가 출력될 일은 없다.
