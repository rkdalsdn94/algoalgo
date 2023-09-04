# 백준 - 브론즈1 - 딱지놀이 - 14696 - 구현 문제
'''
구현 문제

단순 구현 문제이다.
처음에 4, 3, 2, 1 모두 직접 카운트 함수를 통해 숫자를 센 후 문제를 해결했는데, 반복문을 활용하면 중복을 제거할 수 있을거 같아 수정했다.
또한 a_list, b_list를 n으로 반복하는 중에 입력받을 수 있도록 개선했다.

풀이는 딱히 어렵지 않다. count 할 때 0번째 인덱스는 무시해야 된다는 부분만 주의하면 된다.
'''

n = int(input())

for i in range(n):
    a_list, b_list = list(map(int, input().split())), list(map(int, input().split()))
    flag = True

    for j in range(4, 0, -1):
        if a_list[1:].count(j) > b_list[1:].count(j):
            print('A')
            flag = False
            break
        elif b_list[1:].count(j) > a_list[1:].count(j):
            print('B')
            flag = False
            break
    if flag:
        print('D')

'''
처음 코드

n = int(input())
a_list, b_list = [], []

for _ in range(n):
    a_list.append(list(map(int, input().split())))
    b_list.append(list(map(int, input().split())))
# print(a_list, b_list)

# 테스트
# n = 5
# a_list = [[1, 4], [4, 3, 3, 2, 1], [5, 2, 4, 3, 2, 1], [4, 4, 3, 3, 1], [4, 3, 2, 1, 1]]
# b_list = [[4, 2, 3, 2, 1], [4, 4, 3, 2, 1], [3, 4, 3, 2], [5, 4, 4, 2, 3, 1], [5, 4, 2, 4, 1, 3]]
#
#     A
#     B
#     B
#     A
#     D
# 
# n = 4
# a_list = [[4, 4, 3, 2, 1], [4, 3, 3, 2, 1], [4, 4, 3, 3, 3], [4, 3, 2, 1, 1]]
# b_list = [[4, 1, 4, 3, 2], [4, 4, 3, 3, 3], [4, 3, 4, 3, 2], [3, 3, 2, 1]] # D  \  B  \  A  \  A

for i, j in zip(a_list, b_list):
    a_star_cnt = i[1:].count(4)
    b_star_cnt = j[1:].count(4)
    a_circle_cnt = i[1:].count(3)
    b_circle_cnt = j[1:].count(3)
    a_square_cnt = i[1:].count(2)
    b_square_cnt = j[1:].count(2)
    a_triangle_cnt = i[1:].count(1)
    b_triangle_cnt = j[1:].count(1)

    if a_star_cnt > b_star_cnt:
        print('A')
    elif b_star_cnt > a_star_cnt:
        print('B')
    elif a_circle_cnt > b_circle_cnt:
        print('A')
    elif b_circle_cnt > a_circle_cnt:
        print('B')
    elif a_square_cnt > b_square_cnt:
        print('A')
    elif b_square_cnt > a_square_cnt:
        print('B')
    elif a_triangle_cnt > b_triangle_cnt:
        print('A')
    elif b_triangle_cnt > a_triangle_cnt:
        print('B')
    else:
        print('D')
'''
