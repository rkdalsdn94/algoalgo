# 백준 - 브론즈1 - 카드 바꿔치기 - 18766 - 단순 구현, 정렬 문제
'''
단순 구현, 정렬 문제

list로 입력받고 정렬을 해서 두 값이 같은지 비교하는 단순한 구현 문제이다.
'''

t = int(input())
for _ in range(t):
    n = int(input())
    first_card = list(input().split())
    second_card = list(input().split())

    if sorted(first_card) == sorted(second_card):
        print('NOT CHEATER')
    else:
        print('CHEATER')
